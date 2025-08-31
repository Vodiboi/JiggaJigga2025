"""
Main game code
Python is not a safe language. You can in theory cheat in the game by tampering with the contents of this file from your code.
All bots will be checked before the tournament for this sort of code, and if found, will be barred for participating.
Please don't cheat. It's no fun that way, and this contest is purely for fun.
"""
from helpers import *
class JiggaJiggaGame():
    """
    More standard class for features that are generalizable to future Jigga Jiggas

    Main Features:
    - A method for running a bot's function and terminating on timeout
    - A method for logging events using PrintRedirectorStream

    Creator: Aayan Arish
    Future Co-Authors:
        (add your name here if you contribute to this when running a future Jigga Jigga)
    """
    def __init__(self, timeout=0.1, logfile="log.txt", timout_err_code=1093024):
        self.round_nm = 0

        self.timeout = timeout
        self.TIMOUT_ERR_CODE = timout_err_code

        self._logged_round = 0
        self.redirector = PrintRedirectorStream(self)
        self.out = logfile
        self._clear_log()

    def _get_move(self, fnc, args):
        """
        Runs a bot's callable and terminates on timeout  
        fnc: the bot's callable to be run  
        args: the standard arguments to be passed into the callable  
        returns: (the bot's move, None) if the bot runs in time, else (TIMEOUT_ERR_CODE, the time it took the bot)

        note: for speed reasons, if the bot takes too long it is terminated mid call, 
        and so the time returned might be less than what the bot would actually take
        """
        t1 = time_ns()
        tmp = run_with_timeout(int(self.timeout+1), fnc, *args)
        t2 = time_ns()
        if (1e-9)*(t2-t1) > self.timeout:
            return self.TIMOUT_ERR_CODE, (1e-9)*(t2-t1)
        return tmp, None

    def _log(self, *args):
        """
        logs the given events to the output file
        (originally by Jasper Ng, modified by Aayan Arish)
        """
        with open(self.out, "a") as log:
            if not self._logged_round:
                self._logged_round = True
                log.write(f"[R{self.round_nm}]\n")
            log.write("".join(f"{arg}\n" for arg in args))
            log.flush()
    
    def _clear_log(self):
        """ clears the log """
        with open(self.out, "w") as f:
            f.write("")
    
class VotingGame(JiggaJiggaGame):
    """
    Main game class
    """
    def __init__(self, n, bots, timeout=0.1, logfile="log.txt") -> None:
        super().__init__(timeout, logfile)
        self.n = n
        self.grid = np.zeros((n+2, n+2), dtype=int)
        self.claimed_auto = np.zeros((n+2, n+2), dtype=int)
        self.bots = bots
        self.bot_clrs = [(0, 0, 0)] + [i._color4game() for i in bots]

        self.score = np.zeros((len(self.bots)+1))
        self.x_diff = np.array([0, 0, -1, -1, -1, 1, 1, 1])
        self.y_diff = np.array([-1, 1, 0, -1, 1, 0, -1, 1])

        self.banned = deque()
        self.banned_set = set()
        self.BAN_THRESH = 50

    def __str__(self) -> str:
        l = [(self.score[i+1], str(self.bots[i])) for i in range(len(self.bots))]
        l.sort(reverse=True)
        return "\n".join([f"{i+1}) {vl[1]} : {vl[0]}" for i, vl in enumerate(l)])
    
    def updt_cells(self):
        """
        By the rules of the game, updates the grid:
        - if an empty cell is adjacent to 5 or more cells of some player, it becomes that player's cell
        - if a taken cell is adjacent to 7 or more cells of some player, it becomes that player's cell
        adjacent is diagonally and orthogonally (the 8 surrounding cells)

        Faster version: credit to Eric
        """
        # self.claimed_auto = np.zeros((self.n+2, self.n+2), dtype=int)
        new_grid = copy.deepcopy(self.grid)
        kernel = np.ones((3, 3))  # Convolution kernel to count neighbors
        kernel[1,1] = 0
        neighbor_counts = np.zeros((len(self.bots) + 1, self.n+2, self.n+2))
        for i in range(1, len(self.bots) + 1):
            neighbor_counts[i] = scipy.ndimage.convolve((self.grid == i).astype(int), kernel, mode='constant', cval=0)
        for i in range(1, len(self.bots) + 1):
            g2 = (neighbor_counts[i] >= 7) | ((neighbor_counts[i] >= 5) * (self.grid <= 0))
            new_grid[g2] = i
            # print(g2.shape)
            g2 = g2 & (self.grid != i)
            g2 = np.swapaxes(g2, 0, 1)
            self.claimed_auto[g2] = 1
        self.grid = new_grid
        for p in range(1, len(self.bots)+1):
            self.score[p] = np.sum(self.grid == p)


    def run_round(self) -> bool:
        """
        Every Round:
        - check for banned bots to unban, and make sure to unban them
        - go thru all players
            - call the function check for timeout
                - ban if timeout
                - process move if no timeout
        """
        self.round_nm += 1
        self._logged_round = 0
        self._unban_bots()
        # shuffle player move order
        l = list(zip(range(1, len(self.bots)+1), self.bots))
        random.shuffle(l)

        for i, b in l:
            if i in self.banned_set:
                continue
            # get player move
            with redirect_stdout(self.redirector) as f:
                f.set_cur_plr(str(b))
                z, tm = self._get_move(b, [self._make_grid_copy(), i])
            # check for timeout
            if z == self.TIMOUT_ERR_CODE:
                self._ban_bot(i)
                self._log(f"Bot {str(b)} took too long, {round(tm, 5)} seconds. They will be banned until round {self.round_nm + self.BAN_THRESH}")
                continue
            if z == None or len(z) != 2: continue
            if z[0] == "Error Raised":
                self._ban_bot(i)
                self._log(f"Bot {str(b)} had the following error: {z[1]}. They will be banned until round {self.round_nm + self.BAN_THRESH}")
                continue
            # check for invalid move
            y, x = z
            y = int(y) + 1
            x = int(x) + 1
            invalid = (y < 1 or y > self.n) or (x < 0 or x > self.n)
            if invalid:
                self._log(f"Bot {str(b)} has returned an invalid move: {y, x} which is out of bounds for grid size {len(self.grid)}. Move will be ignored.")
                continue
            # process move
            if (self.grid[y, x]): self.score[self.grid[y, x]] -= 1
            self.grid[y, x] = i
            self.claimed_auto[y, x] = 0
            self.score[i] += 1
        # run game update
        self.updt_cells()
        return True

    def map_color(self, clr):
        return self.bot_clrs[clr]

    def make_grid_copy_scr(self):
        return tuple([tuple([self.map_color(self.grid[i+1, j+1]) for i in range(self.n)]) for j in range(self.n)])

    def _make_grid_copy(self):
        return [list(self.grid[i, 1:-1]) for i in range(1, self.n+1)]

    def _ban_bot(self, bot_id):
        """ bans a bot """
        self.banned.append((self.round_nm, bot_id))
        self.banned_set.add(bot_id)

    def _unban_bots(self):
        """ unbans the bots that have been banned for long enough """
        while len(self.banned):
            a, b = self.banned[0]
            if self.round_nm-a >= self.BAN_THRESH:
                self._log(f"Bot {str(self.bots[b-1])} is now unbanned")
                self.banned.popleft()
                self.banned_set.remove(b)
            else:
                break

class StandardGameDisplay():
    """
    Board display for standard Jigga Jigga game
    """
    def __init__(self, pygame, game, grid_size, size, scr_width, scr_height, block_size, fps, rnds, font='Comic Sans MS', scale=1):
        self.game = game
        self.grid_size = grid_size
        self.size = size
        self.scr_width = scr_width
        self.scr_height = scr_height
        self.block_size = block_size
        self.fps = fps
        self.rnds = rnds
        self.scale = scale
        self.pygame = pygame

        self.pygame.init()
        self.pygame.font.init()
        self.main_font = pygame.font.SysFont(font, 24*self.scale)
        self.scr = pygame.display.set_mode((self.scr_width, self.scr_height))
        self.clock = pygame.time.Clock()
    
    def run_round(self, rnd, do_flip=1):
        """
        Runs & Displays 1 game round
        returns: whether to run another round (False if game is over, else True)
        """
        self.clock.tick(self.fps)
        for event in self.pygame.event.get():
            if event.type == self.pygame.QUIT:
                print(self.game)
                exit(0)
        self.scr.fill(0)
        run_another_round = self.game.run_round()

        # display grid
        grd = self.game.make_grid_copy_scr()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.pygame.draw.rect(self.scr, grd[i][j], self.pygame.Rect(j*self.block_size, i*self.block_size, self.block_size, self.block_size))
                # if self.game.claimed_auto[i+1, j+1]:
                #     pygame.draw.circle(self.scr, (255, 255, 255), (j*self.block_size + self.block_size/2, i*self.block_size + self.block_size/2), self.block_size/3)
        # display scores
        scsum = sum(self.game.score)

        for i in range(len(self.game.bots)):
            t1 = self.main_font.render(f'{self.game.bots[i]} : {self.game.score[i+1]}', False, self.game.bot_clrs[i+1])
            self.scr.blit(t1, (20, self.size + i*24*self.scale))
            rat = (self.game.score[i+1]/scsum)*100*self.scale
            self.pygame.draw.rect(self.scr, self.game.bot_clrs[i+1], self.pygame.Rect(self.grid_size*self.block_size-50-rat, self.size + i*24*self.scale + 5, rat, 20*self.scale))
        # display round
        t1 = self.main_font.render(f'Day : {rnd}', False, (250, 250, 250))
        self.scr.blit(t1, (20, self.size + (i+1)*24*self.scale))
        rat2 = (rnd/self.rnds)*100
        self.pygame.draw.rect(self.scr, (250, 250, 250), self.pygame.Rect(self.grid_size*self.block_size-124, self.size + (i+1)*24*self.scale + 3, 108*self.scale, 28*self.scale))
        self.pygame.draw.rect(self.scr, (0, 0, 0), self.pygame.Rect(self.grid_size*self.block_size-122, self.size + (i+1)*24*self.scale + 5, 104*self.scale, 24*self.scale))
        self.pygame.draw.rect(self.scr, (250, 250, 250), self.pygame.Rect(self.grid_size*self.block_size-120, self.size + (i+1)*24*self.scale + 7, rat2*self.scale, 20*self.scale))

        if do_flip: self.pygame.display.flip()
        return bool(run_another_round)
    
    def stall(self):
        """ Stall game until user quits """
        while 1:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    print(self.game)
                    exit(0)

class GameConstantsC():
    @property
    def SCR_WIDTH(self): return 640
    @SCR_WIDTH.setter
    def SCR_WIDTH(self, val): return
    
    @property
    def SCR_HEIGHT(self): return 900
    @SCR_HEIGHT.setter
    def SCR_HEIGHT(self, val): return
    
    @property
    def SIZE(self): return 640
    @SIZE.setter
    def SIZE(self, val): return

    @property
    def GRID_SIZE(self): return 64
    @GRID_SIZE.setter
    def GRID_SIZE(self, val): return

    @property
    def BLOCK_SIZE(self): return self.SIZE/self.GRID_SIZE
    @BLOCK_SIZE.setter
    def BLOCK_SIZE(self, val): return

    @property
    def FPS(self): return 10000
    @FPS.setter
    def FPS(self, val): return

# if any of the game constants stuff is tampered with during the main round, you will be disqualified. 
# (pretty much, don't say anything like game.GameConstants = 5 or something)
GameConstants = GameConstantsC()

# The above is a more secure version of:
# class GameConstants:
#     SCR_WIDTH = 640
#     SCR_HEIGHT = 900
#     SIZE = 640
#     GRID_SIZE = 64
#     BLOCK_SIZE = SIZE/GRID_SIZE
#     FPS = 10000