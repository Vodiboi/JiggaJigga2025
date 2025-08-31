from helpers import *
from game import GameConstants as GC
from scipy import signal as sgnl
from bots.spencer import greed
from bots.ian import cracked_charles

class Bot:
    """
    Standard class for a bot in this game
    """
    def __init__(self) -> None:
        pass

    def __call__(self, grid, p) -> tuple[int, int]:
        pass

class RandomBot(Bot):
    """
    makes a random move
    """
    def __call__(self, grid, p) -> tuple[int, int]:
        return random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)

class HeatmapBot(Bot):
    """
    Given a heat map, return a bot that plays to the heat map.
    Prioritizes larger values

    Args:
        heatmap: the heatmap to use
    """
    def __init__(self, heatmap, force=0) -> None:
        self.heatmap = heatmap
        self.force = force
    
    def __call__(self, grid, p):
        mx_spt = None
        for i in range(len(grid)):
            for j in range(len(grid)):
                if (self.force or grid[i][j] == 0) and grid[i][j] != p:
                    if mx_spt == None or self.heatmap[mx_spt[0]][mx_spt[1]] < self.heatmap[i][j]:
                        mx_spt = (i, j)
        if mx_spt is None:
            # in this scenario, game over. 
            return (random.randint(0, len(grid)-1), random.randint(0, len(grid)-1))
        return mx_spt
    
    def readHeatMapFromFile(fp) -> list[list[int]]:
        with open(fp, "r") as f:
            s = [list(map(int, i.split())) for i in f.read().split("\n")]
        return s

def HeatmapFunctionBot(f, size, force=0):
    """
    given a function f(row, col), return a heatmap bot using that function on the grid
    """
    return HeatmapBot([[f(i, j) for j in range(size)] for i in range(size)], force)

class CopyCarl(Bot):
    def __call__(self, grid, p) -> tuple[int, int]:
        lst = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] != 0 and grid[i][j] != p]
        if len(lst) == 0:
            lst = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] != p]
            if len(lst) == 0:
                lst = lst = [(i, j) for i in range(len(grid)) for j in range(len(grid))]
        return random.choice(lst)

class Snakey_Sullivan(Bot):
    def __init__(self) -> None:
        self.q = []

    def __call__(self, grid, p):
        while (len(self.q)):
            pos = self.q[-1]
            s = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(s)
            for dy, dx in s:
                x = wrp((pos[1]+dx), len(grid))
                y = wrp((pos[0]+dy), len(grid))
                if grid[y][x] == 0:
                    self.q.append((y, x))
                    return self.q[-1]
            self.q.pop(-1)
        self.q.append((random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)))
        return self.q[-1]

def adj_andy(grid, p):
    """
    always tries to play next to a spot it already 
    owns. If it can't do that, it resorts to random.
    """
    possible_spots = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == p:
                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    x2 = wrp((j+dx), len(grid))
                    y2 = wrp((i+dy), len(grid))
                    if grid[y2][x2] == 0:
                        possible_spots.append((y2, x2))
    if not len(possible_spots):
        return (random.randint(0, len(grid)-1), random.randint(0, len(grid)-1))
    return random.choice(possible_spots)

def nonadj_nomad(grid, p):
    '''
    always tries to play next to a spot another player
    already owns. If it can't do that, it resorts to random.
    '''
    possible_spots = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] not in [p, 0]:
                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    x2 = wrp((j+dx), len(grid))
                    y2 = wrp((i+dy), len(grid))
                    if grid[y2][x2] == 0:
                        possible_spots.append((y2, x2))
    if not len(possible_spots):
        return (random.randint(0, len(grid)-1), random.randint(0, len(grid)-1))
    return possible_spots[-1]

class Centered_Carter:
    """
    This strategy finds a center and builds around that center all game long.
    It builds around uniformly.
    """
    def __init__(self):
        self.center = None
        self.seen_center = None

    def __call__(self, grid, p):
        # print(*grid, sep="\n")
        if self.center is None:
            while 1:
                y, x = (random.randint(0, len(grid)-1), random.randint(0, len(grid)-1))
                if grid[y][x] == 0:
                    self.center = (y, x)
                    return (y, x)
        elif self.seen_center == None:
            self.pts = [(i, j) for i in range(len(grid)) for j in range(len(grid))]
            random.shuffle(self.pts)
            self.pts.sort(key = lambda a: abs(a[0]-self.center[0]) + abs(a[1]-self.center[1]))
            self.seen_center = 1
        for i, j in self.pts:
            if grid[i][j] == 0:
                return (i, j)
        return (random.randint(0, len(grid)-1), random.randint(0, len(grid)-1))

class MindlessMonstrosity():
    """
    goes where they go
    """
    def __init__(self, r, do_max=1) -> None:
        self.r = r
        self.do_max = do_max
    
    def __call__(self, grid, p):
        mx = -1
        mn = len(grid)**2
        bst_mx = bst_mn = None
        for i in range(len(grid)):
            for j in range(len(grid)):
                if (grid[i][j] != 0): continue
                sm = 0
                for ny in range(max(0, i-self.r), min(len(grid), i+self.r)):
                    for nx in range(max(0, j-self.r), min(len(grid), j+self.r)):
                        sm += 1 if grid[ny][nx] not in [0, p] else 0
                if sm > mx:
                    bst_mx = (i, j)
                    mx = sm
                if sm < mn:
                    bst_mn = (i, j)
                    mn = sm

                
        if (self.do_max and bst_mx is None) or (not self.do_max and bst_mn is None):
            # should never happen, but in case I'm wrong... ah screw it I can't be wrong
            return (0, 0)
        return bst_mx if self.do_max else bst_mn

class Greedy(RandomBot):
    def __call__(self, grid, p) -> tuple[int, int]:
        best_amt = 0
        best_spot = None
        g2 = list([list(i) for i in grid])
        for i in range(len(grid)):
            for j in range(len(grid)):
                if (g2[i][j] != p):
                    # try making it p
                    g2[i][j] = p
                    cnt = 0
                    for y1, x1 in spots_adj((i, j), len(grid)):
                        if g2[y1][x1] != p:
                            cnt1 = 0
                            for y2, x2 in spots_adj((y1, x1), len(grid)):
                                if g2[y2][x2] == p:
                                    cnt1 += 1
                            if (cnt1 > 4 and g2[y1][x1] == 0) or (cnt1 > 6):
                                cnt += 1
                    if (cnt > best_amt):
                        best_amt = cnt
                        best_spot = (i, j)
        if (best_spot == None):
            return super().__call__(grid, p)
        return best_spot

class Stupid(RandomBot):
    def __call__(self, grid, p) -> tuple[int, int]:
        grid = np.array([np.array(i) for i in grid])
        # considering = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                a, b = zip(*spots_adj((i, j), len(grid)))
                vals = grid[a, b]
                cnts = np.bincount(vals)
                mx = np.argmax(cnts)
                if (cnts[mx] > 4 and cnts[mx] <= 6 and mx not in [0, p] and grid[i][j] != p):
                    return(i, j)
        return super().__call__(grid, p)                

class CopyCartioid(Bot):
    def __init__(self, md) -> None:
        super().__init__()
        self.round_nm = 0
        self.md = md
        self.p = -1
    
    def __call__(self, grid, p) -> tuple[int, int]:
        self.round_nm += 1
        if (self.round_nm%self.md == 0 or self.p == -1):
            cnts = defaultdict(int)
            mxvl = 0
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if (grid[i][j] not in [0, p]):
                        cnts[grid[i][j]] += 1
                        if cnts[grid[i][j]] > cnts[mxvl]:
                            mxvl = grid[i][j]
            self.p = mxvl
        lst = []
        grid = np.array([np.array(i) for i in grid])
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == self.p:
                    a, b = zip(*spots_adj((i, j), len(grid)))
                    vals = grid[a, b]
                    cnts = np.bincount(vals)
                    mx = np.argmax(cnts)
                    if not (cnts[mx] > 6 and mx != 0):
                        lst.append((i, j))
        if len(lst) == 0:
            lst = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] != 0 and grid[i][j] != p]
            if len(lst) == 0:
                lst = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] != p]
                if len(lst) == 0:
                    lst = lst = [(i, j) for i in range(len(grid)) for j in range(len(grid))]
        return random.choice(lst)

class CopyWorseCartioid(Bot):
    def __init__(self, md, threshold=10) -> None:
        super().__init__()
        self.round_nm = 0
        self.md = md
        self.p = -1
        self.thresh = threshold
        self.banned = set()
        self.prev_cnt = 0
    
    def __call__(self, grid, p) -> tuple[int, int]:
        self.round_nm += 1
        if (self.round_nm%self.md == 0 or self.p == -1):
            if (self.round_nm%(self.md+3)**3 == 0):
                self.banned = set()
            cnts = defaultdict(int)
            c2 = 0
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if (grid[i][j] not in [0, p]):
                        cnts[grid[i][j]] += 1
                    if grid[i][j] == p: c2 += 1
            if (c2-self.prev_cnt < self.md//5):
                self.banned.add(self.p)
            self.prev_cnt = c2
            self.last = None
            if len(cnts) != 0:
                self.p = min(cnts.items(), key=lambda x: x[1] if x[1] >= self.thresh and x not in self.banned else 1e10*(1+(x in self.banned)))[0]
        lst = []
        grid = np.array([np.array(i) for i in grid])
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == self.p and (i, j) != self.last:
                    a, b = zip(*spots_adj((i, j), len(grid)))
                    vals = grid[a, b]
                    cnts = np.bincount(vals)
                    mx = np.argmax(cnts)
                    if not (cnts[mx] > 6 and mx != 0):
                        lst.append((i, j))
        if len(lst) == 0:
            lst = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] != 0 and grid[i][j] != p]
            if len(lst) == 0:
                lst = [(i, j) for i in range(len(grid)) for j in range(len(grid)) if grid[i][j] != p]
                if len(lst) == 0:
                    lst = lst = [(i, j) for i in range(len(grid)) for j in range(len(grid))]
        return random.choice(lst)
        
class Bickerer(RandomBot):
    def __init__(self) -> None:
        super().__init__()
        self.prev_grid = None
    
    def __call__(self, grid, p) -> tuple[int, int]:
        if self.prev_grid == None:
            self.prev_grid = grid
        for i in range(len(grid)):
            for j in range(len(grid)):
                if self.prev_grid[i][j] == p and grid[i][j] != p:
                    return i, j
        return super().__call__(grid, p)

class BetterGreedy(RandomBot):
    def __init__(self, every=3) -> None:
        super().__init__()
        self.every = every
        self.nm = 0
    def __call__(self, grid, p) -> tuple[int, int]:
        best_amt = 0
        best_spot = None
        self.nm += 1
        if (self.nm%self.every == 0):
            g2 = np.array([np.array(i) for i in grid])
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if (g2[i, j] != p):
                        # try making it p
                        old = g2[i][j]
                        g2[i, j] = p
                        cnt = 0
                        for y1, x1 in spots_adj((i, j), len(grid)):
                            if g2[y1, x1] != p:
                                a, b = zip(*spots_adj((y1, x1), len(grid)))
                                vals = g2[a, b]
                                cnts = np.bincount(vals)
                                mx = np.argmax(cnts)
                                if ((cnts[mx] > 4 and g2[y1, x1] == 0) or cnt > 6):
                                    cnt += 1
                        if (cnt > best_amt):
                            best_amt = cnt
                            best_spot = (i, j)
                        # g2[i, j] = old
            if (best_spot == None):
                return super().__call__(grid, p)
            return best_spot
        return super().__call__(grid, p)

# class BloodThirsty():
#     def __init__(self):
#         # greedy strategy. Find a cell that will convert the most cells, 

class Convolutional_Convolver():
    def __init__(self, heatf):
        self.hbot = HeatmapFunctionBot(heatf, GC.GRID_SIZE, 0)
        self.convertable = np.zeros((GC.GRID_SIZE, GC.GRID_SIZE))
        self.m2 = np.zeros((GC.GRID_SIZE, GC.GRID_SIZE))

    def rng(self, n):
        for i in range(n):
            for j in range(n):
                yield i, j
    def __call__(self, grid, p):
        n = len(grid)
        happened = 0
        for i, j in self.rng(n):
            self.convertable[i][j] = 0
            self.m2[i][j] = 0

            if grid[i][j] == p:
                self.m2[i][j] += 1
            cnt = 0
            for a, b in spots_adj((i, j), n):
                cnt += grid[a][b] == p
            if (cnt == 4 and grid[i][j] == 0) or (cnt == 6 and grid[i][j] not in [0, p]):
                self.convertable[i][j] = 1
                happened = 1
        if not happened:
            return self.hbot(grid, p)
        scores = sgnl.convolve2d(self.convertable, np.ones((3, 3)), mode="same") - 3*self.m2
        pos = np.argmax(scores)
        return pos/n, pos%n

class HmmCombo():
    def __init__(self, thresh=500):
        self.rndnum = 0
        self.thresh = thresh
    
    def __call__(self, grid, p):
        self.rndnum += 1
        if self.rndnum < self.thresh:
            return greed(grid, p)
        return cracked_charles(grid, p)

class Jumpscare():
    def __init__(self):
        pass
    def __call__(self, grid, p):
        return 5/0

# class TforT():
#     def __init__(self):
#         self.n = GC.GRID_SIZE
#         self.prev_grid = [[0]*self.n for _ in range(self.n)]
#         self.stolen = [0]*5
    
#     def __call__(self, grid, p):
#         for i in range(self.n):
#             for j in range(self.n):
#                 if 

class Darth_Bane:
    """
    The weak will always be victims. That is the way of the universe. 
    The strong take what they want, and the weak suffer at their hands. 
    That is their fate; it is inevitable. Only the strong survive, 
    because only the strong deserve to.
    - Darth Bane
    """

    def __init__(self):
        self.n = GC.GRID_SIZE
        self.kernel = np.ones((3, 3))
        self.kernel[1,1] = 0
        # self.kernel[0,0] = 2
        # self.kernel[0,1] = 2
        # self.kernel[1,0] = 2
        self.q = []
        self.rnd_nm = 0
    # def updt_cells(self, grid, nbots):
    #     """
    #     stolen from myself

    #     nbots is max thing in grid
    #     """
    #     new_grid = copy.deepcopy(grid)
    #     kernel = np.ones((3, 3))  # Convolution kernel to count neighbors
    #     kernel[1,1] = 0
    #     neighbor_counts = np.zeros((nbots, self.n+2, self.n+2))
    #     for i in range(1, len(self.bots) + 1):
    #         neighbor_counts[i] = scipy.ndimage.convolve((grid == i).astype(int), kernel, mode='constant', cval=0)
    #     for i in range(1, len(self.bots) + 1):
    #         g2 = (neighbor_counts[i] >= 7) | ((neighbor_counts[i] >= 5) * (grid <= 0))
    #         new_grid[g2] = i
    #     score = [0]*(len(self.bots)+1)
    #     for p in range(1, len(self.bots)+1):
    #         self.score[p] = np.sum(self.grid == p)
    #     return new_grid, score

    def early_fill(self, grid, p):
        nc = scipy.ndimage.convolve((grid == p).astype(int), self.kernel, mode='constant', cval=0)
        vulnerable = (((nc == 4) | (nc == 3)) * (grid == 0)) | (nc == 6)
        good_spots = scipy.ndimage.convolve((vulnerable).astype(int), self.kernel, mode='constant', cval=0)
        good_spots -= (grid==p)*10
        mx = np.max(good_spots)
        if mx == 0: return None
        lst = [(i, j) for i in range(len(grid)) for j in range(len(grid))]
        
        # center of mass
        sum_x = 0
        sum_y = 0
        cnt = 0
        for a, b in lst:
            if grid[a][b] == p:
                sum_y += a
                sum_x += b
                cnt += 1
        sum_y += len(grid)/2
        sum_x += len(grid)/2
        if (cnt):
            avg_y = sum_y/cnt
            avg_x = sum_x/cnt
            lst.sort(key = lambda pos: abs(pos[0]-avg_y) + abs(pos[1]-avg_x))
        for i, j in lst: 
            if grid[i][j] != p:
                if mx == good_spots[i][j]:
                    return i, j

    def think(self, grid, p):
        """
        building the map
        """

        # map based on how many cells it can directly affect, times the values computed for the cells around it
        nc = scipy.ndimage.convolve((grid == p).astype(int), self.kernel, mode='constant', cval=0)
        # a2 = (nc >= 7) | ((nc >= 5) * (grid <= 0))
        vulnerable = (((nc == 4) | (nc == 3)) * (grid <= 0)) | (nc == 6)

        # A lesson learnt from dictators: exploit the vulernerable
        good_spots = scipy.ndimage.convolve((vulnerable).astype(int), self.kernel, mode='constant', cval=0)
        good_spots -= (grid==p)*10
        good_spots *= 2
        good_spots += nc
        # good_spots += (grid != p)*nc
        # places = np.transpose((good_spots>0).nonzero())
        mx = np.argmax(good_spots)
        row, col = np.unravel_index(mx, grid.shape)
        if good_spots[row, col] == 0 or grid[row][col] == p:
            return None
        return row, col
    
    def snake(self, grid, p):
        while (len(self.q)):
            pos = self.q[-1]
            s = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            random.shuffle(s)
            for dy, dx in s:
                x = wrp((pos[1]+dx), len(grid))
                y = wrp((pos[0]+dy), len(grid))
                if grid[y][x] == 0:
                    self.q.append((y, x))
                    return self.q[-1]
            self.q.pop(-1)
        self.q.append((random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)))
        return self.q[-1]
    
    def more_greedy(self, grid, p):
        return greed(grid, p)

    def __call__(self, grid, p):
        self.rnd_nm += 1
        grid = np.array([np.array(x) for x in grid])
        # if self.rnd_nm < 500:
            # return self.early_fill(grid, p)
        pos = self.early_fill(grid, p)
        if pos is None:
            # if random.randint(0, 1):
            return self.snake(grid, p)
            # else:
            #     self.q.append(self.more_greedy(grid, p))
            #     return self.q[-1]
        self.q.append(pos)
        return pos

#####
# o1 bots

def center_attraction_bot(grid, p):
    """
    Focuses campaigning on houses closer to the center of the 65x65 grid.
    If everything near center is taken, it moves outward.
    """
    size = len(grid)  # 65
    center = size // 2  # 32 for a 65x65 grid
    
    # We’ll search outward in “rings” around the center
    # from distance 0 up to potentially 32.
    for dist in range(size // 2 + 1):
        # We'll iterate in a square ring: center-dist to center+dist
        # Check row/col combos in that bounding box
        top = max(0, center - dist)
        bottom = min(size - 1, center + dist)
        left = max(0, center - dist)
        right = min(size - 1, center + dist)
        
        candidates = []
        for r in range(top, bottom + 1):
            for c in range(left, right + 1):
                if grid[r][c] == 0:  
                    candidates.append((r, c))
        if len(candidates) > 0:
            # Pick a random candidate in this "ring"
            return random.choice(candidates)
    
    # If no undecided remain, just pick any random house
    row = random.randint(0, size - 1)
    col = random.randint(0, size - 1)
    return (row, col)

def corner_focus_bot(grid, p):
    """
    Always starts from top-left corner (row=0, col=0) and scans
    left-to-right, top-to-bottom for the first undecided house.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                return (r, c)
    # If no houses are 0, pick a random house
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

def biggest_cluster_bot(grid, p):
    """
    Finds a house near your existing biggest cluster of supporters.
    Campaign where neighbor influence of your supporters is strongest.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    best_spot = None
    best_supporter_count = -1
    
    # Helper function to get neighbors (8-directional)
    def get_neighbors(r, c):
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    neighbors.append((rr, cc))
        return neighbors
    
    # For each cell, check if it is undecided.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # Count how many of your supporters are among its neighbors
                neighs = get_neighbors(r, c)
                supporter_count = 0
                for (nr, nc) in neighs:
                    if grid[nr][nc] == p:
                        supporter_count += 1
                
                if supporter_count > best_supporter_count:
                    best_supporter_count = supporter_count
                    best_spot = (r, c)
    
    # If we found any undecided spot, use that
    if best_spot is not None:
        return best_spot
    
    # Otherwise, if no undecided left, pick randomly
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

def steal_from_opponent_bot(grid, p):
    """
    Looks for houses near opponent supporters, hoping to flip them or
    influence the region.
    """
    rows = len(grid)
    cols = len(grid[0])

    # Helper to get neighbors
    def get_neighbors(r, c):
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr = r + dr
                cc = c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    neighbors.append((rr, cc))
        return neighbors

    best_spot = None
    best_opponent_count = -1
    
    # Iterate through entire grid
    for r in range(rows):
        for c in range(cols):
            # If this house belongs to an opponent (not ours, not undecided)
            if grid[r][c] != p and grid[r][c] != 0:
                # Check its neighbors for any undecided spots
                neighs = get_neighbors(r, c)
                for (nr, nc) in neighs:
                    if grid[nr][nc] == 0:
                        # Count how many opponent supporters are near that neighbor
                        # (to measure how "contested" it is)
                        opp_count = 0
                        n2 = get_neighbors(nr, nc)
                        for (nnr, nnc) in n2:
                            if grid[nnr][nnc] != p and grid[nnr][nnc] != 0:
                                opp_count += 1
                        if opp_count > best_opponent_count:
                            best_opponent_count = opp_count
                            best_spot = (nr, nc)
    
    # If we found a good spot, do that
    if best_spot is not None:
        return best_spot
    
    # Otherwise, revert to random or fallback
    # e.g. random pick among undecided
    undecided = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                undecided.append((r, c))
    if undecided:
        return random.choice(undecided)
    
    # If no undecided left, pick a random house
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

def improved_infiltrator_bot(grid, p):
    """
    Attempt to expand 'pockets' of your influence deep inside enemy territory.
    1. For each empty cell, we calculate how many neighbors belong to us,
       and what is the maximum number of neighbors belonging to any single opponent.
    2. Score = (# of our neighbors) + 2 * (max # of neighbors from a single opponent).
    3. Pick the empty cell with the highest score.
    4. Fallback: if no empty cell is found, pick a random cell.
    """
    rows = len(grid)
    cols = len(grid[0])

    def get_neighbors(r, c):
        """Return 8-directional neighbors for (r,c)."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    neighbors.append((rr, cc))
        return neighbors
    
    best_spot = None
    best_score = -1
    
    # Scan all cells
    for r in range(rows):
        for c in range(cols):
            # If this cell is undecided, let's evaluate it
            if grid[r][c] == 0:
                neighs = get_neighbors(r, c)
                
                # Count how many neighbors belong to us
                our_neighbors = 0
                
                # Keep track of how many neighbors each opponent has
                opponent_neighbor_counts = {}
                
                for (nr, nc) in neighs:
                    val = grid[nr][nc]
                    if val == p:
                        our_neighbors += 1
                    elif val != 0:  # i.e., belongs to some opponent
                        if val not in opponent_neighbor_counts:
                            opponent_neighbor_counts[val] = 0
                        opponent_neighbor_counts[val] += 1
                
                # Figure out the largest neighbor count among any single opponent
                if opponent_neighbor_counts:
                    max_opponent_neighbors = max(opponent_neighbor_counts.values())
                else:
                    max_opponent_neighbors = 0
                
                # Compute a score
                score = our_neighbors + 2 * max_opponent_neighbors
                
                # Update best pick
                if score > best_score:
                    best_score = score
                    best_spot = (r, c)
    
    # If we found a good spot, use that
    if best_spot is not None:
        return best_spot
    
    # Otherwise, fallback to a random cell if no empty cell is found
    # (meaning the grid is fully decided).
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    return (r, c)

def region_infiltrator_bot(grid, p):
    """
    A "region-based" infiltration bot that:
    1) Finds all pockets of your supporters (connected components).
    2) For each pocket, collects boundary cells (undecided neighbors).
    3) Scores each boundary cell based on infiltration potential:
         score = (# of your neighbors) + 2*(max neighbors from a single opponent)
    4) Picks the cell with the best score among all pockets.

    If no undecided boundary cell exists at all, chooses a random undecided
    (or random cell if none left).
    """
    rows = len(grid)
    cols = len(grid[0])
    
    visited = [[False]*cols for _ in range(rows)]
    
    def get_neighbors(r, c):
        """Return valid 8-directional neighbors for (r,c)."""
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    # --- 1) Find all pockets of your supporters ---
    pockets = []  # list of sets, each set is a connected component of supporters
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == p and not visited[r][c]:
                # BFS or DFS from (r, c)
                pocket_coords = set()
                queue = deque([(r, c)])
                visited[r][c] = True
                
                while queue:
                    rr, cc = queue.popleft()
                    pocket_coords.add((rr, cc))
                    # Explore neighbors that are also ours
                    for nr, nc in get_neighbors(rr, cc):
                        if not visited[nr][nc] and grid[nr][nc] == p:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                
                pockets.append(pocket_coords)
    
    # We'll store a list of candidate boundary cells: (score, (row, col))
    boundary_candidates = []
    
    # --- 2) For each pocket, find boundary cells & compute infiltration score ---
    for pocket in pockets:
        for (rr, cc) in pocket:
            # Check neighbors for undecided
            for nr, nc in get_neighbors(rr, cc):
                if grid[nr][nc] == 0:
                    # That cell is a boundary cell for this pocket
                    # We'll compute infiltration score if we haven't already
                    # But it's possible the same cell is boundary to multiple pockets.
                    # We can either check duplicates or store best score if found multiple times.
                    
                    # Score the boundary cell
                    our_neighbors = 0
                    opponent_neighbor_counts = {}
                    
                    for (nnr, nnc) in get_neighbors(nr, nc):
                        val = grid[nnr][nnc]
                        if val == p:
                            our_neighbors += 1
                        elif val != 0:  # i.e., belongs to some opponent
                            opponent_neighbor_counts[val] = opponent_neighbor_counts.get(val, 0) + 1
                    
                    if opponent_neighbor_counts:
                        max_opponent_neighbors = max(opponent_neighbor_counts.values())
                    else:
                        max_opponent_neighbors = 0
                    
                    score = our_neighbors + 2 * max_opponent_neighbors
                    
                    boundary_candidates.append((score, nr, nc))
    
    # --- 3) Choose the best boundary cell overall ---
    if boundary_candidates:
        # Sort or just pick the max
        best = max(boundary_candidates, key=lambda x: x[0])  # (score, row, col)
        _, br, bc = best
        return (br, bc)
    
    # If we get here, it means either:
    # - We have no pockets (i.e., you have no supporters on the board), or
    # - No undecided cells near any of your supporters.

    # Fallback #1: pick among all remaining undecided
    undecided = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                undecided.append((r, c))
    if undecided:
        return random.choice(undecided)
    
    # Fallback #2: all cells are decided
    # Just pick a random cell (anywhere)
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

def improved_center_attraction_bot(grid, p):
    """
    A refined 'Center-Attraction' bot that:
    1) Prefers cells closer to the center of the board (65x65).
    2) Also considers how many of your supporters are adjacent
       (favoring spots where you already have neighbors).
       
    Score = (64 - manhattan_distance_to_center) + 2 * (# your neighbors).
    Pick the undecided cell with the highest score.
    If no undecided cell remains, choose a random cell.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    center = rows // 2  # 32 for a 65x65
    max_dist = 64       # corner to center (Manhattan) if center=32
    
    def get_neighbors(r, c):
        """Return 8-directional neighbors for (r, c)."""
        neighbors = []
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    neighbors.append((rr, cc))
        return neighbors
    
    best_spot = None
    best_score = -9999  # or float('-inf')
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # Compute Manhattan distance to center
                dist = abs(r - center) + abs(c - center)
                distance_influence = max_dist - dist
                
                # Count how many of your supporters are neighbors
                neighs = get_neighbors(r, c)
                local_support = sum(1 for (nr, nc) in neighs if grid[nr][nc] == p)
                
                # Final score
                score = distance_influence + 2 * local_support
                
                # Update best
                if score > best_score:
                    best_score = score
                    best_spot = (r, c)
    
    if best_spot:
        return best_spot
    
    # If no undecided cells remain, pick a random cell
    r = random.randint(0, rows - 1)
    c = random.randint(0, cols - 1)
    return (r, c)

class CopycatBot:
    """
    A 'copycat' bot that tries to mimic the winning bot's last move,
    while avoiding endless duels and hopeless cells. Stores all last
    moves internally, so you only need to call:

        1) copycat.update_moves(moves_this_turn)
        2) next_move = copycat(grid, my_id)

    across your game loop.
    """
    def __init__(self):
        # Dictionary of {bot_id -> (row, col)} for last moves
        self.last_moves = {}
        
        # Track potential repeated duels over the same cell
        self.last_fight_cell = None
        self.fight_cell_counter = 0

    def update_moves(self, moves_this_turn):
        """
        Update internal record of all bots' last moves after each turn.
        
        moves_this_turn: dict {bot_id -> (row, col)}
                         indicating where each bot just campaigned.
        """
        for bot_id, coords in moves_this_turn.items():
            self.last_moves[bot_id] = coords

    def __call__(self, grid, my_id):
        """
        Decide our move, given the current grid and our bot ID.
        
        grid: 2D list/array (e.g., 65x65) where grid[r][c] = 0 or (1..N) for a bot.
        my_id: Our bot's ID.

        Returns:
            (row, col) for our next campaign.
        """
        rows = len(grid)
        cols = len(grid[0])

        # 1) Count how many cells each bot controls, to find who is "winning."
        counts = {}
        for r in range(rows):
            for c in range(cols):
                owner = grid[r][c]
                if owner != 0:
                    counts[owner] = counts.get(owner, 0) + 1
        
        if not counts:
            # If the board is entirely undecided, there's no winner yet
            return self._random_undecided(grid)

        max_support = max(counts.values())
        # The set of all bots that tie for that highest count:
        winners = [bot_id for bot_id, ccount in counts.items() if ccount == max_support]

        # If there's exactly one winner and it's not us, we consider copying them
        winner = None
        if len(winners) == 1:
            winner = winners[0]
        if winner == my_id:
            # If we ourselves are the sole winner, no need to copy
            winner = None

        # 2) Attempt to copy the sole winner's last move
        if winner is not None and winner in self.last_moves:
            (wr, wc) = self.last_moves[winner]
            
            # (a) Check for repeated duel
            if (wr, wc) == self.last_fight_cell:
                self.fight_cell_counter += 1
            else:
                self.last_fight_cell = (wr, wc)
                self.fight_cell_counter = 1
            
            # If we've tried flipping the same cell fewer than ~4 times:
            if self.fight_cell_counter <= 3:
                # (b) Check if that cell is too strongly influenced by winner
                if not self._is_cell_too_strong_for_opponent(grid, my_id, wr, wc, winner):
                    # If feasible, copy their move
                    return (wr, wc)

        # 3) Otherwise, do a fallback (e.g., infiltration)
        return self._infiltration_fallback(grid, my_id)

    # --------------------------------------------------------------------------
    # Helper Methods
    # --------------------------------------------------------------------------

    def _random_undecided(self, grid):
        """
        Return a random (row, col) among all undecided cells.
        If none remain, return a random cell anywhere.
        """
        rows = len(grid)
        cols = len(grid[0])
        undecided = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    undecided.append((r, c))
        if undecided:
            return random.choice(undecided)
        else:
            return (random.randint(0, rows - 1), random.randint(0, cols - 1))

    def _infiltration_fallback(self, grid, my_id):
        """
        A simple fallback infiltration strategy:
        Pick an undecided cell with the most neighbors that are yours.
        If no undecided remain, pick a random cell.
        """
        rows = len(grid)
        cols = len(grid[0])
        
        best_cell = None
        best_count = -1

        def neighbors(r, c):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        yield rr, cc
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # count how many neighbors belong to us
                    count_ours = 0
                    for (nr, nc) in neighbors(r, c):
                        if grid[nr][nc] == my_id:
                            count_ours += 1
                    if count_ours > best_count:
                        best_count = count_ours
                        best_cell = (r, c)
        
        if best_cell is not None:
            return best_cell
        
        # If no undecided left
        return (random.randint(0, rows - 1), random.randint(0, cols - 1))

    def _is_cell_too_strong_for_opponent(self, grid, my_id, row, col, opp):
        """
        Check if 'opp' has >=5 neighbors around (row,col), making it likely
        they'd flip it right back. Adjust logic as needed.
        """
        rows = len(grid)
        cols = len(grid[0])
        opp_count = 0
        
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = row + dr, col + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if grid[rr][cc] == opp:
                        opp_count += 1
        
        return (opp_count >= 5)

def chain_reaction_bot(grid, p):
    """
    Attempt to exploit the evening flipping rules to convert as many houses
    as possible automatically.
    
    - For each undecided cell (grid[r][c] == 0):
      1) Pretend we campaign at (r, c) this turn (forcing grid[r][c] = p).
      2) Simulate the evening's chain reaction flips:
         - Undecided (0) flips to p if it has >= 5 neighbors for p.
         - A house that belongs to any other player flips to p if it has >= 7 neighbors for p.
         - Each new flip can cause subsequent flips (multi-step).
      3) Count how many houses flipped in total (not counting the forced campaign).
      4) Revert simulation.
    
    - Pick the (r, c) that maximizes that chain reaction score.
    - If no undecided cells remain, pick a random cell.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    best_spot = None
    best_flips = -1
    
    # Quick check: if no undecided left, do fallback
    has_undecided = any(0 in row for row in grid)
    if not has_undecided:
        return _random_cell(rows, cols)
    
    # Otherwise, evaluate each undecided cell
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                flips = _simulate_chain_reaction(grid, p, r, c)
                if flips > best_flips:
                    best_flips = flips
                    best_spot = (r, c)
    
    # If we found a good spot, use it. Otherwise pick random.
    if best_spot is not None:
        return best_spot
    else:
        return _random_cell(rows, cols)

def _simulate_chain_reaction(grid, p, r0, c0):
    """
    Simulate the evening chain reaction if we campaign at (r0, c0).
    Return the total *additional* flips (beyond the forced campaign).
    
    We'll make a deep copy of the grid, set (r0,c0) = p, then repeatedly
    apply the flipping rules in a BFS-like manner until no more flips occur.
    
    1) If an UNDECIDED (0) cell has >=5 neighbors of p, it flips to p.
    2) If a cell that belongs to another player has >=7 neighbors of p,
       it flips to p.
    3) Each new flip can trigger further flips among its neighbors.
    """
    rows = len(grid)
    cols = len(grid[0])
    # Make a copy so we don't mutate the real grid
    grid_copy = [row[:] for row in grid]
    
    # Force our campaign on (r0,c0)
    grid_copy[r0][c0] = p
    
    flipped_count = 1  # includes the forced campaign
    queue = deque()
    queue.append((r0, c0))
    
    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    while queue:
        cr, cc = queue.popleft()
        # For each neighbor of the cell that just flipped,
        # check if that neighbor should now flip as well.
        for nr, nc in neighbors(cr, cc):
            if grid_copy[nr][nc] != p:
                # It's either 0 (undecided) or belongs to another player
                count_p = sum(grid_copy[rn][cn] == p for (rn, cn) in neighbors(nr, nc))
                
                if grid_copy[nr][nc] == 0:
                    # flips if >=5 neighbors for p
                    if count_p >= 5:
                        grid_copy[nr][nc] = p
                        flipped_count += 1
                        queue.append((nr, nc))
                else:
                    # some other player -> flips if >=7 neighbors for p
                    if count_p >= 7:
                        grid_copy[nr][nc] = p
                        flipped_count += 1
                        queue.append((nr, nc))
    
    # We return how many new houses (beyond the forced campaign) were captured
    return flipped_count - 1

def _random_cell(rows, cols):
    """Return a random (row, col) in [0..rows-1], [0..cols-1]."""
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

class FastChainReactionBot:
    """
    A 'fast' approximation of the chain reaction strategy.
    1) Only consider cells that are adjacent to your existing territory
       (i.e., have at least one neighbor who supports you).
    2) For each candidate cell, simulate a limited number (waves) of evening flips.
    3) Choose the cell that yields the largest approximate chain-reaction gain.
    """

    def __init__(self, waves=2):
        """
        :param waves: How many 'waves' of flips to simulate (1 or 2 is usually enough).
        """
        self.waves = waves

    def __call__(self, grid, p):
        """
        The main method to pick your next move.

        :param grid: 2D list representing the board state.
                     grid[r][c] = 0 means undecided, 
                                  1..N means a particular bot controls that cell.
        :param p:    Your bot's ID (e.g., 1, 2, 3, ...)

        :return: (row, col) where you want to campaign.
        """
        rows = len(grid)
        cols = len(grid[0])

        # 1) Gather candidate cells
        candidates = []
        has_undecided = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    has_undecided = True  # Track if there's at least one undecided cell

                # Skip if it's already ours
                if grid[r][c] == p:
                    continue

                # We only consider cells that either:
                #   (a) are 0 (undecided) or belong to another bot (grid[r][c] != p),
                #   (b) AND have at least 1 neighbor who is ours.
                if grid[r][c] == 0 or grid[r][c] != p:
                    if self._has_p_neighbor(grid, r, c, p):
                        candidates.append((r, c))

        # If no candidates or no undecided left, pick a fallback move
        if not candidates or not has_undecided:
            return self._random_undecided_or_any(grid)

        # 2) Evaluate each candidate with partial chain reaction simulation
        best_cell = None
        best_flips = -1
        for (cr, cc) in candidates:
            # It's allowed to "campaign" on an opponent's cell or an undecided cell,
            # depending on your game rules. If you only permit converting 0 => p by talking,
            # then skip (cr, cc) if grid[cr][cc] != 0.
            flips = self._simulate_waves(grid, p, cr, cc, self.waves)
            if flips > best_flips:
                best_flips = flips
                best_cell = (cr, cc)

        # 3) Return the best cell found
        if best_cell is not None:
            return best_cell
        else:
            # Fallback if somehow none was suitable
            return self._random_undecided_or_any(grid)

    # --------------------------------------------------------------------------
    # Helper methods
    # --------------------------------------------------------------------------

    def _has_p_neighbor(self, grid, r, c, p):
        """
        Returns True if cell (r,c) has at least one neighbor belonging to player p.
        8-directional check.
        """
        rows = len(grid)
        cols = len(grid[0])
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if grid[rr][cc] == p:
                        return True
        return False

    def _simulate_waves(self, grid, p, row, col, waves):
        """
        Simulate up to 'waves' expansions of evening flips if we campaign at (row, col).
        This is a partial chain reaction approach (not the full BFS until equilibrium).
        Returns the total number of flips (including the forced campaign).

        Flip rules:
          - If an undecided cell (0) has >=5 neighbors supporting p, it flips to p.
          - If a cell controlled by another player has >=7 neighbors supporting p, it flips to p.

        For efficiency, we only do 'waves' expansions, e.g. 1 or 2, instead of going on indefinitely.
        """
        rows = len(grid)
        cols = len(grid[0])

        # Copy the grid to avoid mutating the original
        grid_copy = [row_[:] for row_ in grid]

        # Force the campaign (convert row,col to p)
        grid_copy[row][col] = p
        flipped = set()
        flipped.add((row, col))

        queue = deque()
        queue.append((row, col))

        def neighbors(r, c):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        yield rr, cc

        # Perform limited BFS expansions
        for _ in range(waves):
            next_queue = deque()
            while queue:
                (r0, c0) = queue.popleft()
                for (nr, nc) in neighbors(r0, c0):
                    if (nr, nc) not in flipped:
                        if grid_copy[nr][nc] != p:
                            # Count p neighbors
                            p_count = sum(grid_copy[a][b] == p
                                          for (a, b) in neighbors(nr, nc))

                            if grid_copy[nr][nc] == 0:
                                # flips if >=5 neighbors for p
                                if p_count >= 5:
                                    grid_copy[nr][nc] = p
                                    flipped.add((nr, nc))
                                    next_queue.append((nr, nc))
                            else:
                                # belongs to an opponent -> flips if >=7 neighbors for p
                                if p_count >= 7:
                                    grid_copy[nr][nc] = p
                                    flipped.add((nr, nc))
                                    next_queue.append((nr, nc))
            queue = next_queue

        return len(flipped)

    def _random_undecided_or_any(self, grid):
        """
        If there's any undecided (0) cell, pick one at random.
        Otherwise, pick any random cell on the board.
        """
        rows = len(grid)
        cols = len(grid[0])
        undecided = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    undecided.append((r, c))
        if undecided:
            return random.choice(undecided)
        else:
            return (random.randint(0, rows - 1), random.randint(0, cols - 1))

class FastChainReactionBot2:
    """
    A 'fast' approximation of the chain reaction strategy, enhanced with a
    'stuck detection' mechanism.

    1) We try the usual partial chain-reaction approach (checking a limited
       number of waves).
    2) If the best chain reaction is below a certain threshold (e.g., <2 flips),
       we assume we're stuck in our current territory.
    3) We then 'start new territory' by picking a cell far from our existing
       supporters, hoping for a more open region to grow.
    """

    def __init__(self, waves=2, stuck_threshold=2):
        """
        :param waves: How many 'waves' of flips to simulate (1 or 2 is usually enough).
        :param stuck_threshold: If the best chain reaction is < this number of flips,
                               we consider ourselves 'stuck' and pick a brand-new area.
        """
        self.waves = waves
        self.stuck_threshold = stuck_threshold

    def __call__(self, grid, p):
        """
        The main method to pick your next move.

        :param grid: 2D list representing the board state.
                     grid[r][c] = 0 means undecided, 
                                  1..N means a particular bot controls that cell.
        :param p:    Your bot's ID (e.g., 1, 2, 3, ...)

        :return: (row, col) where you want to campaign.
        """
        rows = len(grid)
        cols = len(grid[0])

        # 1) Gather candidate cells that are near our current territory
        #    (they have at least one neighbor who is ours).
        candidates = []
        has_undecided = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    has_undecided = True

                # Skip if it's already ours
                if grid[r][c] == p:
                    continue

                # Check if  (r, c)  has a p-neighbor
                # And it's either 0 or belongs to another player (not p).
                if grid[r][c] == 0 or grid[r][c] != p:
                    if self._has_p_neighbor(grid, r, c, p):
                        candidates.append((r, c))

        # If no candidates or no undecided remain, fallback
        if not candidates or not has_undecided:
            return self._random_undecided_or_any(grid)

        # 2) Evaluate each candidate with partial chain reaction simulation
        best_cell = None
        best_flips = -1
        for (cr, cc) in candidates:
            # It's allowed to campaign on an opponent's cell or an undecided cell,
            # depending on your game rules. If you only permit converting 0->p by talking,
            # skip if grid[cr][cc] != 0. Otherwise, keep it.
            flips = self._simulate_waves(grid, p, cr, cc, self.waves)
            if flips > best_flips:
                best_flips = flips
                best_cell = (cr, cc)

        # 3) Check if we appear "stuck"
        if best_flips < self.stuck_threshold:
            # Instead of picking best_cell, let's start new territory
            new_spot = self._start_new_territory(grid, p)
            if new_spot is not None:
                return new_spot
            else:
                # If for some reason we can't find a new territory, just do fallback
                return self._random_undecided_or_any(grid)

        # 4) If we're not stuck, pick the best cell from our partial chain sim
        if best_cell is not None:
            return best_cell
        
        # Fallback if none was suitable
        return self._random_undecided_or_any(grid)

    # --------------------------------------------------------------------------
    # Helper methods
    # --------------------------------------------------------------------------

    def _has_p_neighbor(self, grid, r, c, p):
        """
        Returns True if cell (r,c) has at least one neighbor belonging to player p.
        8-directional check.
        """
        rows = len(grid)
        cols = len(grid[0])
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    if grid[rr][cc] == p:
                        return True
        return False

    def _simulate_waves(self, grid, p, row, col, waves):
        """
        Simulate up to 'waves' expansions of evening flips if we campaign at (row, col).
        This is a partial chain reaction approach (not the full BFS until equilibrium).
        Returns the total number of flips (including the forced campaign).

        Flip rules:
          - If an undecided cell (0) has >=5 neighbors supporting p, it flips to p.
          - If a cell controlled by another player has >=7 neighbors supporting p, it flips to p.
        """
        rows = len(grid)
        cols = len(grid[0])

        # If your rules only allow campaigning on an undecided cell, skip if col != 0
        # We'll assume we can forcibly convert any cell for demonstration.
        
        # Copy the grid to avoid mutating the original
        grid_copy = [row_[:] for row_ in grid]

        # Force the campaign (convert row,col to p)
        grid_copy[row][col] = p
        flipped = set()
        flipped.add((row, col))

        queue = deque()
        queue.append((row, col))

        def neighbors(r, c):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r + dr, c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        yield rr, cc

        # Perform limited BFS expansions
        for _ in range(waves):
            next_queue = deque()
            while queue:
                (r0, c0) = queue.popleft()
                for (nr, nc) in neighbors(r0, c0):
                    if (nr, nc) not in flipped:
                        if grid_copy[nr][nc] != p:
                            # Count p neighbors
                            p_count = sum(grid_copy[a][b] == p
                                          for (a, b) in neighbors(nr, nc))

                            if grid_copy[nr][nc] == 0:
                                # flips if >=5 neighbors for p
                                if p_count >= 5:
                                    grid_copy[nr][nc] = p
                                    flipped.add((nr, nc))
                                    next_queue.append((nr, nc))
                            else:
                                # belongs to an opponent -> flips if >=7 neighbors for p
                                if p_count >= 7:
                                    grid_copy[nr][nc] = p
                                    flipped.add((nr, nc))
                                    next_queue.append((nr, nc))
            queue = next_queue

        return len(flipped)

    def _random_undecided_or_any(self, grid):
        """
        If there's any undecided (0) cell, pick one at random.
        Otherwise, pick any random cell on the board.
        """
        rows = len(grid)
        cols = len(grid[0])
        undecided = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    undecided.append((r, c))
        if undecided:
            return random.choice(undecided)
        else:
            return (random.randint(0, rows - 1), random.randint(0, cols - 1))

    def _start_new_territory(self, grid, p):
        """
        Pick a cell 'far' from our existing supporters, in hopes of finding a more open area.
        
        Basic strategy:
        1) Find all your supporters' locations.
        2) For each undecided cell (grid[r][c] == 0), compute the minimum distance 
           to any of your supporters.
        3) Pick the cell with the *largest* min distance (i.e., farthest from your territory).
           That might be a corner or an isolated region.
        4) If no suitable cell found, return None.
        
        You can refine this with other heuristics, e.g. also consider opponent presence.
        """
        rows = len(grid)
        cols = len(grid[0])
        
        my_cells = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == p:
                    my_cells.append((r, c))
        
        # If we have no supporters, we can't measure distance. Just pick random.
        if not my_cells:
            return self._random_undecided_or_any(grid)
        
        best_cell = None
        best_dist = -1
        
        # We only consider UNDECIDED cells for "starting new territory"
        # If you prefer also flipping an opponent's cell, adapt logic below.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    # compute min distance to any supporter
                    dist = min(abs(r - rr) + abs(c - cc) for (rr, cc) in my_cells)
                    if dist > best_dist:
                        best_dist = dist
                        best_cell = (r, c)
        
        return best_cell

def frontline_pusher_bot(grid, p):
    """
    Focus on cells along the 'frontline' between your territory and opponents.
    1) Collect all cells that are (a) not yours, and (b) have at least one neighbor of yours,
       and (c) also have at least one neighbor belonging to an opponent.
    2) Pick the cell that has the greatest 'flip potential'—the sum of
       (# your neighbors) + (some factor of # opponent neighbors).
    3) If no frontline cells, pick a random undecided cell.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    best_cell = None
    best_score = -1
    has_undecided = False
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                has_undecided = True
            if grid[r][c] != p:  # Potential cell to flip or campaign
                # Check if it has at least 1 neighbor p (your territory)
                # AND at least 1 neighbor from a different (opponent) territory
                neighbor_ours = 0
                neighbor_opponent = 0
                for (nr, nc) in neighbors(r, c):
                    if grid[nr][nc] == p:
                        neighbor_ours += 1
                    elif grid[nr][nc] != 0:
                        neighbor_opponent += 1
                
                # Only consider it "frontline" if it has both your neighbors AND opponent neighbors
                if neighbor_ours > 0 and neighbor_opponent > 0:
                    # Score the cell. For instance:
                    # we might do: score = neighbor_ours * 2 - neighbor_opponent
                    # (meaning we prefer places where we have a big advantage).
                    # Or we keep it simpler, e.g.:
                    score = neighbor_ours - neighbor_opponent
                    if score > best_score:
                        best_score = score
                        best_cell = (r, c)
    
    # If we found a frontline cell, pick it
    if best_cell is not None:
        return best_cell
    
    # Otherwise, pick a random undecided cell (fallback)
    if has_undecided:
        # pick a random undecided
        undecided = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    undecided.append((r, c))
        if undecided:
            return random.choice(undecided)
    
    # If no undecided, pick any cell
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

def peer_pressure_exploiter_bot(grid, p):
    """
    Look for undecided cells that already have 4 of your supporters as neighbors,
    so that by campaigning there, it ends up with 5 neighbors (including itself)
    and won't flip away easily (and might cause further flips).
    Fallback: pick the cell with the most of your neighbors if none have exactly 4.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    best_cell_4 = None  # cell that has exactly 4 neighbors of ours
    best_cell_4_neighbors_count = -1  # if multiple, pick the one with the highest total adjacency?
    
    fallback_cell = None
    fallback_count = -1  # track best general adjacency
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                # Count how many of your supporters are neighbors
                n_ours = sum(grid[nr][nc] == p for (nr, nc) in neighbors(r, c))
                
                # If it has exactly 4 neighbors of p, that is our prime target
                if n_ours == 4:
                    # we can also factor in total neighbor synergy
                    # but let's keep it simple
                    # we can store the cell that has the *most total neighbors of p*
                    if n_ours > best_cell_4_neighbors_count:
                        best_cell_4_neighbors_count = n_ours
                        best_cell_4 = (r, c)
                
                # track a fallback if none have exactly 4
                if n_ours > fallback_count:
                    fallback_count = n_ours
                    fallback_cell = (r, c)
    
    if best_cell_4 is not None:
        return best_cell_4
    elif fallback_cell is not None:
        return fallback_cell
    
    # if no undecided left, random
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

def inactivity_exploiter_bot(grid, p):
    """
    Looks for 'quiet zones' (large patches of 0 or minimal opponent presence),
    and campaigns near the center of such a quiet zone.
    """
    import random
    rows = len(grid)
    cols = len(grid[0])
    
    # Step 1: We can do a BFS or "region" approach for all 0-cells to find largest patches of unclaimed.
    # For simplicity, let's just pick a random 0 cell that has few neighbors who belong to *anyone*.
    
    best_cell = None
    best_opponent_count = 99999  # we want to minimize how many neighbors are claimed
    
    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    # gather all 0-cells
    zero_cells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                zero_cells.append((r, c))
    
    if not zero_cells:
        # No undecided at all, fallback
        return (random.randint(0, rows - 1), random.randint(0, cols - 1))
    
    # Evaluate each 0-cell: count total neighbors who are any bot
    for (r, c) in zero_cells:
        count_claimed = 0
        for (nr, nc) in neighbors(r, c):
            if grid[nr][nc] != 0:
                count_claimed += 1
        if count_claimed < best_opponent_count:
            best_opponent_count = count_claimed
            best_cell = (r, c)
    
    return best_cell

def inactivity_exploiter_bot_twist(grid, p):
    """
    Looks for 'quiet zones' (large patches of 0 or minimal opponent presence),
    and campaigns near the center of such a quiet zone.
    """
    import random
    rows = len(grid)
    cols = len(grid[0])
    
    # Step 1: We can do a BFS or "region" approach for all 0-cells to find largest patches of unclaimed.
    # For simplicity, let's just pick a random 0 cell that has few neighbors who belong to *anyone*.
    
    best_cell = None
    best_opponent_count = 99999  # we want to minimize how many neighbors are claimed
    
    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    # gather all 0-cells
    zero_cells = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                zero_cells.append((r, c))
    
    if not zero_cells:
        # No undecided at all, fallback
        return (random.randint(0, rows - 1), random.randint(0, cols - 1))
    
    # Evaluate each 0-cell: count total neighbors who are any bot
    for (r, c) in zero_cells:
        count_claimed = 0
        for (nr, nc) in neighbors(r, c):
            if grid[nr][nc] != 0 and grid[nr][nc] != p:
                count_claimed += 1
        if count_claimed < best_opponent_count or random.choice([0]*10 + [1]):
            best_opponent_count = count_claimed
            best_cell = (r, c)
    
    return best_cell

def lookahead_flipper_bot(grid, p):
    """
    For each undecided cell, we do a 1-step look ahead:
      - If we flip it, do we push some neighbors over the threshold to flip?
    Then pick the cell that yields the biggest immediate payoff.
    """
    import random
    rows = len(grid)
    cols = len(grid[0])
    
    def neighbors(r, c):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    best_cell = None
    best_flips = -1
    
    # track if we have any 0
    has_undecided = False
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                has_undecided = True
                
                # Simulate flipping this cell
                flips = 1  # this cell itself
                # Now see if that flip pushes neighbors over the threshold
                for (nr, nc) in neighbors(r, c):
                    val = grid[nr][nc]
                    if val != p:  # either 0 or an opponent
                        # Count how many neighbors of (nr, nc) are p, 
                        # but now (r, c) is also p
                        p_count = sum(
                            grid[x][y] == p or (x == r and y == c) 
                            for (x, y) in neighbors(nr, nc)
                        )
                        
                        if val == 0 and p_count >= 5:
                            flips += 1
                        elif val != 0 and val != p and p_count >= 7:
                            flips += 1
                
                if flips > best_flips:
                    best_flips = flips
                    best_cell = (r, c)
    
    if best_cell is not None:
        return best_cell
    
    if has_undecided:
        # fallback: random 0
        zero_cells = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    zero_cells.append((r, c))
        if zero_cells:
            return random.choice(zero_cells)
    
    # if no 0 left, pick random
    return (random.randint(0, rows - 1), random.randint(0, cols - 1))

class ZigZagBot:
    """
    Moves across the board in a zig-zag (snake) pattern:
      Row 0: left -> right
      Row 1: right -> left
      Row 2: left -> right
      ...
    Picks the first 0 found in that order.
    """
    def __init__(self):
        pass

    def __call__(self, grid, p):
        import random
        rows = len(grid)
        cols = len(grid[0])
        
        for r in range(rows):
            if r % 2 == 0:
                # even row: left to right
                c_range = range(cols)
            else:
                # odd row: right to left
                c_range = range(cols - 1, -1, -1)
            
            for c in c_range:
                if grid[r][c] == 0:
                    return (r, c)
        
        # fallback if no 0 left
        return (random.randint(0, rows - 1), random.randint(0, cols - 1))

class AvoidCrowdBot:
    """
    Always pick an undecided cell that has the fewest 'claimed' neighbors,
    trying to avoid heavily contested areas.
    """
    def __init__(self):
        pass

    def __call__(self, grid, p):
        import random
        rows = len(grid)
        cols = len(grid[0])

        def neighbors(r, c):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    rr = r + dr
                    cc = c + dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        yield rr, cc
        
        best_cell = None
        best_count = 9999  # we want to MINIMIZE the number of claimed neighbors
        
        found_undecided = False
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    found_undecided = True
                    # count how many neighbors belong to ANY player (non-zero)
                    count_claimed = 0
                    for (nr, nc) in neighbors(r, c):
                        if grid[nr][nc] != 0:
                            count_claimed += 1
                    if count_claimed < best_count:
                        best_count = count_claimed
                        best_cell = (r, c)
        
        if best_cell is not None:
            return best_cell
        
        if not found_undecided:
            # fallback if no 0 left
            return (random.randint(0, rows - 1), random.randint(0, cols - 1))
        
        # theoretically won't get here if found_undecided is True, but let's be safe
        return (random.randint(0, rows - 1), random.randint(0, cols - 1))

class CoinFlipTwistBot:
    """
    50% chance: pick a random 0-cell
    50% chance: pick a random opponent cell
    Avoid re-flipping the same cell we did last turn.
    """
    def __init__(self):
        self.last_move = None

    def __call__(self, grid, p):
        rows = len(grid)
        cols = len(grid[0])

        heads_or_tails = random.choice(["heads", "tails"])

        # Let's define a small function for picking a random cell from a list
        def random_pick(cells):
            # filter out the last move if it's in there
            filtered = [c for c in cells if c != self.last_move]
            if not filtered:
                if cells:
                    return random.choice(cells)
                else:
                    return None
            else:
                return random.choice(filtered)

        if heads_or_tails == "heads":
            # pick random 0-cell
            zero_cells = []
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 0:
                        zero_cells.append((r, c))
            choice = random_pick(zero_cells)
            if choice is None:
                # fallback: pick random opponent cell
                choice = self._random_opponent_cell(grid, p)
        else:
            # pick random opponent cell
            choice = self._random_opponent_cell(grid, p)
            if choice is None:
                # fallback: random 0
                choice = self._random_zero_cell(grid)

        if choice is None:
            # if all fails, random anywhere
            choice = (random.randint(0, rows - 1), random.randint(0, cols - 1))

        self.last_move = choice
        return choice

    def _random_opponent_cell(self, grid, p):
        import random
        rows = len(grid)
        cols = len(grid[0])
        opp_cells = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0 and grid[r][c] != p:
                    opp_cells.append((r, c))
        if opp_cells:
            return random.choice(opp_cells)
        return None

    def _random_zero_cell(self, grid):
        import random
        rows = len(grid)
        cols = len(grid[0])
        zero_cells = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    zero_cells.append((r, c))
        if zero_cells:
            return random.choice(zero_cells)
        return None

class EdgesFirstBot:
    """
    Always tries to pick from the edges (outer boundary) of the board
    if there's any undecided cell. Otherwise, picks a random undecided.
    """
    def __init__(self):
        pass

    def __call__(self, grid, p):
        import random
        rows = len(grid)
        cols = len(grid[0])
        
        # top edge
        for c in range(cols):
            if grid[0][c] == 0:
                return (0, c)
        
        # bottom edge
        for c in range(cols):
            if grid[rows-1][c] == 0:
                return (rows-1, c)
        
        # left edge
        for r in range(rows):
            if grid[r][0] == 0:
                return (r, 0)
        
        # right edge
        for r in range(rows):
            if grid[r][cols-1] == 0:
                return (r, cols-1)
        
        # fallback: pick a random 0
        undecided = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    undecided.append((r, c))
        
        if undecided:
            return random.choice(undecided)
        
        # if none is 0, random cell
        return (random.randint(0, rows - 1), random.randint(0, cols - 1))

class WeightedNeighborsBot:
    """
    Among all undecided cells, pick one randomly with probability
    proportional to (1 + # of your neighbors). 
    That means cells with more of your neighbors are more likely,
    but you can still occasionally pick an outlier.
    """
    def __init__(self):
        pass

    def __call__(self, grid, p):
        rows = len(grid)
        cols = len(grid[0])

        # Gather all 0-cells, with weights
        zero_cells = []
        weights = []
        
        def neighbors(r, c):
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r+dr, c+dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        yield rr, cc

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    zero_cells.append((r, c))
                    # count how many neighbors are p
                    count_p = sum(grid[nr][nc] == p for (nr, nc) in neighbors(r, c))
                    w = 1 + count_p
                    weights.append(w)

        if not zero_cells:
            # fallback if no 0 left
            return (random.randint(0, rows-1), random.randint(0, cols-1))
        
        # Weighted random choice
        total_weight = sum(weights)
        pick = random.uniform(0, total_weight)
        
        running = 0
        for (cell, w) in zip(zero_cells, weights):
            running += w
            if pick <= running:
                return cell
        
        # In case of floating precision issues, fallback
        return zero_cells[-1]

def multi_factor_score_bot(grid, p):
    """
    A 'probably good' approach that calculates a composite score for each
    undecided cell based on:
      - yourNeighbors: # of your neighbors
      - maxOpponentBlock: largest # of neighbors from a single opponent
      - centerProximity: optional small bonus for closeness to center

    Score formula (you can tweak the weights):
      score = 3*yourNeighbors + 2*maxOpponentBlock + centerBonus

    Then pick the cell with the highest score.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    center_r = rows // 2
    center_c = cols // 2
    
    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r+dr, c+dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield rr, cc
    
    best_cell = None
    best_score = -999999
    
    # We track if there's any undecided at all
    has_undecided = False

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                has_undecided = True
                
                # Count your neighbors
                your_neighbors = 0
                opponent_counts = {}
                
                for (nr, nc) in neighbors(r, c):
                    val = grid[nr][nc]
                    if val == p:
                        your_neighbors += 1
                    elif val != 0:
                        # belongs to some opponent
                        opponent_counts[val] = opponent_counts.get(val, 0) + 1
                
                max_opponent_block = max(opponent_counts.values()) if opponent_counts else 0
                
                # small bonus for center proximity (larger bonus for being near center)
                dist_center = abs(r - center_r) + abs(c - center_c)
                # could do (some constant - dist_center) or 0 if you prefer
                center_bonus = max(0, 8 - dist_center)  # for example, only a small zone around center
                
                # Score formula - tweak as you wish
                score = (3 * your_neighbors) + (2 * max_opponent_block) + center_bonus
                
                if score > best_score:
                    best_score = score
                    best_cell = (r, c)
    
    if best_cell is not None:
        return best_cell
    
    # fallback if no 0 left
    if not has_undecided:
        # pick random
        return (random.randint(0, rows-1), random.randint(0, cols-1))
    
    # theoretically won't reach here if there's any 0, but just in case:
    return (random.randint(0, rows-1), random.randint(0, cols-1))

def region_infiltrator_multi_step_bot(grid, p, waves=2):
    """
    1) For each opponent, BFS their territory to find big clusters.
    2) For each cluster, gather frontier (undecided) cells next to that cluster.
    3) For each frontier cell, do a partial wave simulation (waves=2).
    4) Pick the cell that yields the largest approximate flips or infiltration effect.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    # Identify which players are opponents
    # We'll store them in a set (1..N except p)
    players = set()
    for r in range(rows):
        for c in range(cols):
            val = grid[r][c]
            if val != 0:
                players.add(val)
    if p in players:
        players.remove(p)  # only keep opponents
    
    # BFS function to find a cluster of a single opponent
    def bfs_cluster(start_r, start_c, opp):
        cluster = []
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        while queue:
            (rr, cc) = queue.popleft()
            cluster.append((rr, cc))
            for (nr, nc) in neighbors(rr, cc):
                if not visited[nr][nc] and grid[nr][nc] == opp:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        return cluster
    
    def neighbors(r, c):
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r+dr, c+dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield (rr, cc)

    # We'll gather frontier cells from all opponent clusters
    frontier_cells = []
    
    visited = [[False]*cols for _ in range(rows)]
    
    for opp in players:
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == opp and not visited[r][c]:
                    # find this entire cluster of opp
                    cluster = bfs_cluster(r, c, opp)
                    # gather frontier for that cluster
                    for (cr, cc) in cluster:
                        for (nr, nc) in neighbors(cr, cc):
                            if grid[nr][nc] == 0:
                                # A frontier cell - adjacent to opponent cluster
                                frontier_cells.append((nr, nc))

    # remove duplicates
    frontier_cells = list(set(frontier_cells))
    
    if not frontier_cells:
        # fallback: if there's no frontier, pick a simpler approach
        # e.g. pick the biggest cluster of ours or random 0
        return _fallback_pick(grid, p)
    
    # Evaluate each frontier cell with a partial wave simulation (waves=2 by default)
    best_cell = None
    best_flips = -1
    for (fr, fc) in frontier_cells:
        # simulate how many flips occur if we campaign on (fr, fc)
        flips = simulate_waves(grid, p, fr, fc, waves)
        if flips > best_flips:
            best_flips = flips
            best_cell = (fr, fc)
    
    return best_cell if best_cell is not None else _fallback_pick(grid, p)

def simulate_waves(grid, p, row, col, waves):
    """
    Quick partial chain-reaction simulation for 'waves' expansions.
    If the chosen cell isn't 0, you might skip or forcibly convert it 
    if your rules allow that. Then count how many total flips happen.
    """
    rows = len(grid)
    cols = len(grid[0])
    
    from collections import deque
    copy_grid = [r[:] for r in grid]
    
    # Force the campaign
    if copy_grid[row][col] != p:
        copy_grid[row][col] = p
    
    flipped = set()
    flipped.add((row, col))
    
    def neighbors(r, c):
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr, cc = r + dr, c + dc
                if 0 <= rr < rows and 0 <= cc < cols:
                    yield (rr, cc)
    
    queue = deque()
    queue.append((row, col))
    
    total_flips = 1
    
    for _ in range(waves):
        next_queue = deque()
        while queue:
            (cr, cc) = queue.popleft()
            for (nr, nc) in neighbors(cr, cc):
                if (nr, nc) not in flipped:
                    if copy_grid[nr][nc] != p:
                        # count p neighbors
                        count_p = sum(copy_grid[x][y] == p for (x,y) in neighbors(nr,nc))
                        # If it's 0 => flip if >=5 neighbors
                        if copy_grid[nr][nc] == 0 and count_p >= 5:
                            copy_grid[nr][nc] = p
                            total_flips += 1
                            flipped.add((nr, nc))
                            next_queue.append((nr, nc))
                        # If it's an opponent => flip if >=7 neighbors
                        elif copy_grid[nr][nc] != 0 and count_p >= 7:
                            copy_grid[nr][nc] = p
                            total_flips += 1
                            flipped.add((nr, nc))
                            next_queue.append((nr, nc))
        queue = next_queue
    
    return total_flips

def _fallback_pick(grid, p):
    """
    Fallback strategy if no frontier found. 
    Just pick any 0 or random if none remain.
    """
    import random
    rows = len(grid)
    cols = len(grid[0])
    zeros = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                zeros.append((r, c))
    if zeros:
        return random.choice(zeros)
    return (random.randint(0, rows-1), random.randint(0, cols-1))

class power_base_infiltration_hybrid_bot:
    def __init__(self, m1=2, m2=3, thresh=30):
        self.m1 = m1
        self.m2 = m2
        self.thresh = thresh
        self.cnt = defaultdict(int)
        self.rnd = 0
    def __call__(self, grid, p):
        """
        A simple hybrid:
        score = 2*(# your neighbors) + 3*(max # neighbors for any one opponent)
        The '2' weight helps expand your cluster;
        The '3' weight encourages flipping opponent territory.
        Then pick the highest-scoring 0-cell.
        """
        rows = len(grid)
        cols = len(grid[0])
        self.rnd += 1

        if self.rnd % 100 == 0: self.cnt.clear()
        def neighbors(r, c):
            for dr in (-1, 0, 1):
                for dc in (-1, 0, 1):
                    if dr == 0 and dc == 0:
                        continue
                    rr, cc = r+dr, c+dc
                    if 0 <= rr < rows and 0 <= cc < cols:
                        yield rr, cc
        
        best_spot = None
        best_score = -1
        has_undecided = False

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != p and self.cnt[(r, c)] <= self.thresh:
                    has_undecided = True
                    # count your neighbors
                    your_neighbors = 0
                    opponents_count = {}
                    for (nr, nc) in neighbors(r, c):
                        val = grid[nr][nc]
                        if val == p:
                            your_neighbors += 1
                        elif val != 0:
                            opponents_count[val] = opponents_count.get(val, 0) + 1
                    max_opp = max(opponents_count.values()) if opponents_count else 0

                    # Weighted sum
                    score = self.m1*your_neighbors + self.m2*max_opp
                    if score > best_score:
                        best_score = score
                        best_spot = (r, c)

        if best_spot:
            self.cnt[best_spot] += 1
            return best_spot
        
        # fallback
        if not has_undecided:
            # all claimed
            return (random.randint(0, rows-1), random.randint(0, cols-1))
        
        # theoretically won't get here if has_undecided is True, but let's be safe
        return (random.randint(0, rows-1), random.randint(0, cols-1))

class AayanBots:
    """
    All of my bots
    """
    Random = name("Random", (121, 19, 161))(RandomBot())
    HeatmapOdd = name("Odd", (200, 30, 255))(HeatmapFunctionBot(lambda i, j: (i+j) * ((i + j) % 2 or i+j >= GC.GRID_SIZE+GC.GRID_SIZE-2), GC.GRID_SIZE, 1))
    Carter = name("Carter", (136, 148, 191))(Centered_Carter())
    # Karter = name("Karter", (191, 48, 108))(HeatmapFunctionBot(lambda i, j: ((abs(i-GC.GRID_SIZE//2) + abs(j-GC.GRID_SIZE//2)) == 0)*100 +  ((abs(i-GC.GRID_SIZE//2) + abs(j-GC.GRID_SIZE//2))%2) * 1/((abs(i-GC.GRID_SIZE//2) + abs(j-GC.GRID_SIZE//2) + 1)), GC.GRID_SIZE, 1))
    Jeff = name("Jeff", (82, 141, 235))(HeatmapFunctionBot(lambda i, j: (i**2 + j**2) , GC.GRID_SIZE))
    # James = name("James", (204, 59, 204))(HeatmapFunctionBot(lambda i, j: -(((abs(i-GC.GRID_SIZE//2) + abs(j-GC.GRID_SIZE//2)) == 0)*100 +  ((abs(i-GC.GRID_SIZE//2) + abs(j-GC.GRID_SIZE//2))%2) * 1/((abs(i-GC.GRID_SIZE//2) + abs(j-GC.GRID_SIZE//2) + 1))), GC.GRID_SIZE, 1))
    HeatmapBarry = name("Heatmap Barry", (102, 232, 63))(HeatmapFunctionBot(lambda i, j: i*j, GC.GRID_SIZE, 1))
    # HeatmapLarry = name("Heatmap Larry", (100, 11, 48))(HeatmapFunctionBot(lambda i, j: ((i-GC.GRID_SIZE//2)**2 + (j-GC.GRID_SIZE//2)**2), GC.GRID_SIZE))
    # Splitter = name("Split", (194, 128, 224))(HeatmapFunctionBot(lambda i, j: (abs(i-GC.GRID_SIZE//2)&(-abs(i-GC.GRID_SIZE//2))) * (abs(j-GC.GRID_SIZE//2)&(-abs(j-GC.GRID_SIZE//2))), GC.GRID_SIZE, 1))
    # Huh = name("Huhh", (33, 51, 22))(HeatmapFunctionBot(lambda i, j: min(-i, -j), GC.GRID_SIZE, 1))
    GapFiller = name("GapFiller", (3, 79, 23))(HeatmapFunctionBot(lambda i, j: (i%3 != 0) or (j%3 != 0), GC.GRID_SIZE, 1))
    Karl = name("Karl", (82, 8, 39))(CopyCarl())
    Andy = name("Andy", (82, 235, 222))(adj_andy)
    Nomad = name("Nomad", (97, 182, 235))(nonadj_nomad)
    Sullivan = name("Sullivan", (136, 48, 191))(Snakey_Sullivan())
    Scared = name("Scared", (92, 62, 48))(MindlessMonstrosity(3, 0))
    # dumb = name("Stupid", (83, 138, 118))(Stupid())
    # Gerald = name("Gerald", (97, 107, 52))(Greedy())
    # Geraldo = name("Geraldo", (97, 107, 52))(BetterGreedy())
    # Cartioid = name("Cartioid", (29, 200, 242))(CopyCartioid(10))
    Cartioid2 = name("Cartioid2", (100, 100, 255))(CopyWorseCartioid(10))
    # NuhUh = name("NuhUh", (180, 219, 156))(Bickerer())
    # HeatmapKumar = name("Kumar", (153, 91, 64))(HeatmapFunctionBot(lambda i, j: bool(i%3) * bool(j%3), GC.GRID_SIZE))
    HeatmapKarthik = name("Karthik", (153, 131, 64))(HeatmapFunctionBot(lambda i, j: (i&1) * (j&1), GC.GRID_SIZE))
    # HeatmapKishore = name("Kishore", (133, 31, 164))(HeatmapFunctionBot(lambda i, j: max(i, j, GC.GRID_SIZE-i-1, GC.GRID_SIZE-j-1), GC.GRID_SIZE))
    # HeatmapKhalid = name("Khalid", (133, 31, 164))(HeatmapFunctionBot(lambda i, j: max((i==0 or j == 0 or i+1==GC.GRID_SIZE or j+1==GC.GRID_SIZE)*10, bool(j%3 or i%2)), GC.GRID_SIZE))
    # Convolver = name("Convoluted", (13, 31, 174))(Convolutional_Convolver(lambda i, j: -abs(i-GC.GRID_SIZE//2)*abs(j-GC.GRID_SIZE//2)))
    Bane = name("Darth Bane", (65, 129, 130))(Darth_Bane())
    HmmCombo = name("Hmmmm", (183, 52, 235))(HmmCombo())
    Junlin = name("Jumpscare Junlin", (5, 5, 5))(Jumpscare())


class OtherBots:
    Attraction = name("Attraction O1", (136, 170, 100))(center_attraction_bot)
    Attraction2 = name("Attraction2 O1", (136, 170, 200))(improved_center_attraction_bot)
    CornerFocus = name("Corner Focus O1", (136, 200, 10))(corner_focus_bot)
    BiggestCluster = name("Biggest Cluster O1", (1, 170, 200))(biggest_cluster_bot)
    # Robber = name("Robber O1", (1, 250, 100))(steal_from_opponent_bot)
    # BetterRobber = name("Robber 2 O1", (200, 250, 100))(improved_infiltrator_bot)
    RegionRobber = name("Robber 3 O1", (150, 250, 200))(region_infiltrator_bot)
    CopyO1 = name("Copier O1", (150, 150, 200))(CopycatBot())
    ChainReaction = name("Chain Reaction O1", (150, 150, 0))(chain_reaction_bot)
    # FastChainReaction = name("???", (150, 0, 50))(FastChainReactionBot(waves=20))
    FastChainReaction = name("Chain Reaction 2 O1", (150, 0, 50))(FastChainReactionBot(waves=20))
    FastUnstuckChainReaction = name("Chain Reaction 3 O1", (150, 0, 150))(FastChainReactionBot2(waves=10, stuck_threshold=10))
    Frontline = name("Frontline O1", (252, 186, 3))(frontline_pusher_bot)
    PeerPressure = name("Peer Pressure O1", (252, 50, 30))(peer_pressure_exploiter_bot)
    InactivityExploiter = name("Inactivity Exploiter O1", (252, 50, 130))(inactivity_exploiter_bot)
    # InactivityExploiter2 = name("???", (22, 150, 230))(inactivity_exploiter_bot_twist)
    InactivityExploiter2 = name("Inactivity Exploiter w O1", (22, 150, 230))(inactivity_exploiter_bot_twist)
    # LookaheadFlipper = name("Lookahead Flipper O1", (191, 255, 0))(lookahead_flipper_bot)
    ZigZag = name("ZigZag O1", (190, 0, 0))(ZigZagBot())
    CrowdAvoider = name("Crowd Avoider O1", (0, 180, 0))(AvoidCrowdBot())
    CoinFlipper = name("Coin Flipper O1", (13, 200, 49))(CoinFlipTwistBot())
    EdgesFirst = name("Edges First O1", (13, 100, 149))(EdgesFirstBot())
    WeightedNeighbors = name("Weighted Neighbors O1", (152, 86, 30))(WeightedNeighborsBot())
    MultiFact = name("MultiFact O1", (52, 186, 30))(multi_factor_score_bot)
    # RegionInfril = name("RegionInfril O1", (82, 126, 50))(region_infiltrator_multi_step_bot)
    # WeightedStrategy = name("???", (82, 226, 100))(power_base_infiltration_hybrid_bot(4, 2))
    WeightedStrategy = name("Weighted Strategy O1", (82, 226, 100))(power_base_infiltration_hybrid_bot(4, 2))