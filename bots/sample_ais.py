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



class SampleAis:
    Raja = name("Random Raja", (250, 100, 50))(random_raja)
    Rishi = name("Row by Row Rishi", (100, 250, 50))(row_by_row_rishi)
    Gukesh = name("Growing Gukesh", (100, 50, 250))(growing_gukesh)
    Pranav = name("Perimeter Pranav", (10, 150, 250))(perimeter_pranav)