from helpers import *

def random_raja(grid, p):
    """Picks a random cell"""
    return random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)

def row_by_row_rishi(grid, p):
    """
    Goes row by row, tries to convince houses it is yet to convince
    """
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[x][y] != p:
                # either empty or convinced to vote for another player
                return (x, y)
    # no free cells left, just pick a house randomly
    return random_raja(grid, p)

def growing_gukesh(grid, p):
    """
    Tries to convince a house next to a house it already convinced
    """
    valid = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == p:
                # try claiming adjacent to this guy
                for y, x in spots_adj((i, j), grid_size=len(grid)):
                    if grid[y][x] != p:
                        # make sure we aren't reclaiming our own land
                        valid.append((y, x))
    if len(valid) == 0:
        # we have not convinced anyone, so pick randomly
        return random_raja(grid, p)
    # randomly pick a valid cell
    a = random.choice(valid)
    return a


def perimeter_pranav(grid, p):
    '''
    always tries to play next to a house that is 
    convinced to vote for a different politician.
    If it can't do that, it resorts to random.
    '''
    possible_spots = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] not in [p, 0]:
                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    # using the wrp function, which prevents out of bounds
                    # use dy and dx to compute the new y and x coords
                    x2 = wrp((j+dx), len(grid))
                    y2 = wrp((i+dy), len(grid))
                    if grid[y2][x2] == 0:
                        possible_spots.append((y2, x2))
    if len(possible_spots) == 0:
        return (random.randint(0, len(grid)-1), random.randint(0, len(grid)-1))
    return random.choice(possible_spots)



def adj(x, y, size):
    # attempt 2
    # valid_x = [i if 0 <= i and i < size for i in [x-1, x, x+1]]
    # valid_y = [i if 0 <= i and i < size for i in [y-1, y, y+1]]
    # possible_adjacencies = [(x+1, y), (x-1, y),
    #                         (x, y+1), (x+1, y+1), (x-1, y+1),
    #                         (x, y-1), (x+1, y-1), (x-1, y-1)]
    # adjacencies = [(px, py) if (px in valid_x and py in valid_y) for px, py in possible_adjacencies]
    # for px, py in possible_adjacencies:
    #     if px in valid_x and py in valid_y:
    adjacencies = []
    if x + 1 < size: # i can shrink this bc i know it cant be the case that y + 1 > size and y - 1 < 0
        if x - 1 >= 0:
            if y + 1 < size:
                if y - 1 >= 0:
                    adjacencies = [(x+1, y), (x-1, y),
                                            (x, y+1), (x+1, y+1), (x-1, y+1),
                                            (x, y-1), (x+1, y-1), (x-1, y-1)]
                else:
                    adjacencies = [(x+1, y), (x-1, y),
                                            (x, y+1), (x+1, y+1), (x-1, y+1)]
            else:
                if y - 1 >= 0:
                    adjacencies = [(x+1, y), (x-1, y),
                                            (x, y-1), (x+1, y-1), (x-1, y-1)]
                # else:
                #     adjacencies = [(x+1, y), (x-1, y)]
        else:
            if y + 1 < size:
                if y - 1 >= 0:
                    adjacencies = [(x+1, y),
                                            (x, y+1), (x+1, y+1),
                                            (x, y-1), (x+1, y-1)]
                else:
                    adjacencies = [(x+1, y),
                                            (x, y+1), (x+1, y+1)]
            else:
                if y - 1 >= 0:
                    adjacencies = [(x+1, y),
                                            (x, y-1), (x+1, y-1)]
                # else:
                #     adjacencies = [(x+1, y)]
    else:
        if x - 1 >= 0:
            if y + 1 < size:
                if y - 1 >= 0:
                    adjacencies = [(x-1, y),
                                            (x, y+1), (x-1, y+1),
                                            (x, y-1), (x-1, y-1)]
                else:
                    adjacencies = [(x-1, y),
                                            (x, y+1), (x-1, y+1)]
            else:
                if y - 1 >= 0:
                    adjacencies = [(x-1, y),
                                            (x, y-1), (x-1, y-1)]
                # else:
                #     adjacencies = [(x-1, y)]
        # else:
        #     if y + 1 < size:
        #         if y - 1 >= 0:
        #             adjacencies = [(x, y+1), (x, y-1)]
        #         else:
        #             adjacencies = [(x, y+1)]
        #     else:
        #         if y - 1 >= 0:
        #             adjacencies = [(x, y-1)]
        #         else:
        #             adjacencies = []


    # # attempt 1
    # # return the set of indices of adjacent squares of x, y
    # adjacencies = set()
    # for dx in [-1, 0, 1]:
    #     for dy in [-1, 0, 1]:
    #         x2 = wrp((x+dx), len(grid))
    #         y2 = wrp((y+dy), len(grid))
    #         adjacencies.add((x2, y2))
    # adjacencies.remove((x, y))
    return adjacencies


chosen = []
size = 0

def in_bounds(square):
    return (square[0] < size and square[1] < size)

def basic_loop():
    for i in range(size):
        for j in range(size):
            yield i, j

def spiral_loop(xpos=.5, ypos=.5, direction = (1, 0)):
    current = [int(size*xpos), int(size*ypos)]
    dist = 1
    distance_gone = 0
    while dist <= (size * 2 * max([xpos, 1-xpos, ypos, 1-ypos])):
        if in_bounds(current):
            yield current
        current[0] += direction[0]
        current[1] += direction[1]
        distance_gone += 1
        if distance_gone > dist:
            distance_gone = 0
            dist += abs(direction[0])
            direction = (-direction[1], direction[0])
    pass

def greed(grid, p):
    global chosen, size
    size = len(grid)

    # lets speed things up, make a grid of num adjacencies of all points
    grid_adj_val = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    grid_adj_zeroes = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for i, j in basic_loop():
        if grid[i][j] == p:
            for x, y in adj(i, j, size):
                grid_adj_val[x][y] += 1 # add 1 to all adjacent squares
        if grid[i][j] == 0:
            for x, y in adj(i, j, size):
                grid_adj_zeroes[x][y] += 1 # add 1 to all adjacent squares
    

    # let's speed things up, make a grid of values of all points
    grid_val = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
    for i, j in basic_loop():
        if grid[i][j] == 0:
            if grid_adj_val[i][j] == 4:
                for x, y in adj(i, j, size):
                    grid_val[x][y] += 1 # could consider making this int(grid[x][y] != p)
        elif grid[i][j] != p:
            if grid_adj_val[i][j] == 6:
                for x, y in adj(i, j, size):
                    grid_val[x][y] += 1

    # hopefully at this point we have a grid (grid_val) that, for each square, contains
    # how many adjacent squares would be convinced after that fact to vote for me


    # makes the choice that will give us the most squares in coercion stage
    # notably, doesn't care about if square is 0 or !p, to make it better, slightly prefer !p
    choices = []
    choice = ()
    max_val = -1
    max_os = -1
    for i, j in basic_loop():
        if grid[i][j] != p:
            if max_val < grid_val[i][j]:
                max_val = grid_val[i][j]
                max_os = grid_adj_zeroes[i][j]
                choice = (i, j)

    # maximizing for adjacent empties
    lst = []
    for a, b in spiral_loop():
        lst.append((a, b))
    # lst.reverse()
    # lst = [(i, j) for i in range(size) for j in range(size)]
    
    # center of mass
    # sum_x = 0
    # sum_y = 0
    # cnt = 0
    # for a, b in lst:
    #     if grid[a][b] == p:
    #         sum_y += a
    #         sum_x += b
    #         cnt += 1
    # # sum_y += len(grid)/2
    # # sum_x += len(grid)/2
    # if (cnt):
    #     avg_y = sum_y/cnt
    #     avg_x = sum_x/cnt
    #     lst.sort(key = lambda pos: abs(pos[0]-avg_y) + abs(pos[1]-avg_x))
    for i, j in lst: # choose a better starting point!
                               # maybe center of mass, or place most empty?
        if grid[i][j] != p:
            if max_val == grid_val[i][j]:
                if max_os < grid_adj_zeroes[i][j]:
                    # if chosen.count((i, j)) < 10:
                        max_val = grid_val[i][j]
                        max_os = grid_adj_zeroes[i][j]
                        choice = (i, j)
    # maybe instead of maximizing empties, should play for protected squares when fighting another bot
    

    chosen.append(choice)
    return choice



class SpencerAis:
    Greedy = name("GREEDY BOI", (255, 0, 0))(greed)
    # add your bot here using the format: MyBot = name("My Bot", (bot color rgb))(my_bot_function)
    # then, you can use SampleAis.MyBot in main.py 