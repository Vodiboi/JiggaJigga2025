from helpers import *
from bisect import bisect_left as binary_search
# preliminary bots, functions are called by cracked charles occasionally
def random_raja(grid, p):
    return random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)
def space_filling_sam(grid,p):
    valid = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == p:
                for y in range(max(0,i-1),min(64,i+2)):
                    for x in range(max(0,j-1),min(64,j+2)):
                        if grid[y][x] == 0:
                            valid.append((y, x))
    if len(valid) == 0:
        [(y,x) for y in range(len(grid)) for x in range(len(grid)) if grid[y][x] == 0]
    if len(valid) == 0:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == p:
                    for y in range(max(0,i-1),min(64,i+2)):
                        for x in range(max(0,j-1),min(64,j+2)):
                            if grid[y][x] != p:
                                valid.append((y, x))
    if len(valid) == 0:
        valid = [(y,x) for y in range(len(grid)) for x in range(len(grid)) if grid[y][x] == 0]
    if len(valid) == 0:
        return random_raja(grid,p)
    return random.choice(valid)

def neighbors(grid,color,s):
    total = 0
    for change in [(dy,dx) for dy in range(-1,2) for dx in range(-1,2) if (dy,dx) != (0,0)]:
        if 0 <= s[0]+change[0] < 64 and 0 <= s[1]+change[1] < 64:
            if grid[s[0]+change[0]][s[1]+change[1]] == color:
                total += 1
    return total
def max_neighbors(grid,p,s):
    neighbors = {}
    for change in [(dy,dx) for dy in range(-1,2) for dx in range(-1,2) if (dy,dx) != (0,0)]:
        if 0 <= s[0]+change[0] < 64 and 0 <= s[1]+change[1] < 64:
            n = grid[s[0]+change[0]][s[1]+change[1]]
            if n in neighbors.keys():
                neighbors[n] += 1
            else:
                neighbors[n] = 1
    maxn = 0
    for n in neighbors.keys():
        if neighbors[n] >= maxn and n not in (0,p):
            maxn = neighbors[n]
    return maxn

# actual charles
def cracked_charles(grid,p):
    if random.randint(1,20) == 1:
        return space_filling_sam(grid,p)
    changes = [(dy,dx) for dy in range(-1,2) for dx in range(-1,2) if (dy,dx) != (0,0)]
    best = 0
    bestSpots = []
    mySpots = []
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[y][x] == p:
                mySpots.append((y,x))
                for dy,dx in changes:
                    if 0 <= y+dy < 64 and 0 <= x+dx < 64:
                        if grid[y+dy][x+dx] != p:
                            ns = neighbors(grid,p,(y+dy,x+dx))
                            if grid[y+dy][x+dx] == 0 and max_neighbors(grid,p,(y+dy,x+dx)) == 0:
                                ns += 3
                            nns = [(y+dy+ddy,x+dx+ddx) for ddy,ddx in changes if 0 <= y+dy+ddy < 64 and 0 <= x+dx+ddx < 64 if grid[y+dy+ddy][x+dx+ddx] != p and max_neighbors(grid,p,(y+dy+ddy,x+dx+ddx)) < 7]
                            if len(nns) > 0:
                                if ns > best:
                                    bestSpots = nns
                                    best = ns
                                elif ns == best:
                                    bestSpots += nns
    if len(bestSpots) == 0:
        return random_raja(grid,p)
    return random.choice(bestSpots)

def adjacent_spots(s):
    return [(a,b) for a in range(max(0,s[0]-1),min(64,s[0]+2)) for b in range(max(0,s[1]-1),min(64,s[1]+2)) if (a,b) != s]
def amongus_andy(grid,p):
    amongus_spots = [(5, 20), (5, 21), (5, 22), (5, 23), (5, 24), (5, 25), (5, 26), (5, 27), (5, 28), (5, 29), (5, 30), (5, 31), (5, 32), (5, 33), (5, 34), (5, 35), (5, 36), (5, 37), (5, 38), (5, 39), (5, 40), (5, 41), (5, 42), (5, 43), (6, 20), (6, 21), (6, 22), (6, 23), (6, 24), (6, 25), (6, 26), (6, 27), (6, 28), (6, 29), (6, 30), (6, 31), (6, 32), (6, 33), (6, 34), (6, 35), (6, 36), (6, 37), (6, 38), (6, 39), (6, 40), (6, 41), (6, 42), (6, 43), (7, 20), (7, 21), (7, 22), (7, 23), (7, 24), (7, 25), (7, 26), (7, 27), (7, 28), (7, 29), (7, 30), (7, 31), (7, 32), (7, 33), (7, 34), (7, 35), (7, 36), (7, 37), (7, 38), (7, 39), (7, 40), (7, 41), (7, 42), (7, 43), (8, 20), (8, 21), (8, 22), (8, 41), (8, 42), (8, 43), (9, 20), (9, 21), (9, 22), (9, 41), (9, 42), (9, 43), (10, 20), (10, 21), (10, 22), (10, 41), (10, 42), (10, 43), (11, 20), (11, 21), (11, 22), (11, 41), (11, 42), (11, 43), (12, 20), (12, 21), (12, 22), (12, 41), (12, 42), (12, 43), (13, 20), (13, 21), (13, 22), (13, 41), (13, 42), (13, 43), (14, 11), (14, 12), (14, 13), (14, 14), (14, 15), (14, 16), (14, 17), (14, 18), (14, 19), (14, 20), (14, 21), (14, 22), (14, 22), (14, 23), (14, 24), (14, 25), (14, 26), (14, 27), (14, 28), (14, 29), (14, 30), (14, 31), (14, 32), (14, 33), (14, 34), (14, 35), (14, 36), (14, 37), (14, 38), (14, 39), (14, 40), (14, 41), (14, 41), (14, 42), (14, 43), (14, 44), (14, 45), (14, 46), (14, 47), (14, 48), (14, 49), (14, 50), (14, 51), (14, 52), (15, 11), (15, 12), (15, 13), (15, 14), (15, 15), (15, 16), (15, 17), (15, 18), (15, 19), (15, 20), (15, 21), (15, 22), (15, 23), (15, 24), (15, 25), (15, 26), (15, 27), (15, 28), (15, 29), (15, 30), (15, 31), (15, 32), (15, 33), (15, 34), (15, 35), (15, 36), (15, 37), (15, 38), (15, 39), (15, 40), (15, 41), (15, 42), (15, 43), (15, 44), (15, 45), (15, 46), (15, 47), (15, 48), (15, 49), (15, 50), (15, 51), (15, 52), (16, 10), (16, 11), (16, 12), (16, 13), (16, 14), (16, 15), (16, 16), (16, 17), (16, 18), (16, 19), (16, 20), (16, 21), (16, 22), (16, 23), (16, 24), (16, 25), (16, 26), (16, 27), (16, 28), (16, 29), (16, 30), (16, 31), (16, 32), (16, 33), (16, 34), (16, 35), (16, 36), (16, 37), (16, 38), (16, 39), (16, 40), (16, 41), (16, 42), (16, 43), (16, 44), (16, 45), (16, 46), (16, 47), (16, 48), (16, 49), (16, 50), (16, 51), (16, 52), (16, 53), (17, 8), (17, 9), (17, 10), (17, 11), (17, 52), (17, 53), (17, 54), (17, 55), (18, 8), (18, 9), (18, 10), (18, 53), (18, 54), (18, 55), (19, 8), (19, 9), (19, 10), (19, 53), (19, 54), (19, 54), (19, 55), (20, 8), (20, 9), (20, 10), (20, 53), (20, 54), (20, 54), (20, 55), (21, 8), (21, 9), (21, 10), (21, 53), (21, 54), (21, 55), (22, 8), (22, 9), (22, 10), (22, 52), (22, 53), (22, 54), (22, 55), (23, 8), (23, 9), (23, 10), (23, 44), (23, 45), (23, 46), (23, 47), (23, 48), (23, 49), (23, 50), (23, 51), (23, 52), (23, 53), (24, 8), (24, 9), (24, 10), (24, 44), (24, 45), (24, 46), (24, 47), (24, 48), (24, 49), (24, 50), (24, 51), (24, 52), (25, 8), (25, 9), (25, 10), (25, 44), (25, 45), (25, 46), (25, 47), (25, 48), (25, 49), (25, 50), (25, 51), (25, 52), (26, 8), (26, 9), (26, 10), (26, 44), (26, 45), (26, 46), (27, 8), (27, 9), (27, 10), (27, 44), (27, 45), (27, 46), (28, 8), (28, 9), (28, 10), (28, 44), (28, 45), (28, 46), (29, 8), (29, 9), (29, 10), (29, 44), (29, 45), (29, 46), (30, 8), (30, 9), (30, 10), (30, 44), (30, 45), (30, 46), (31, 8), (31, 9), (31, 10), (31, 44), (31, 45), (31, 46), (32, 8), (32, 9), (32, 10), (32, 20), (32, 21), (32, 22), (32, 23), (32, 24), (32, 25), (32, 44), (32, 45), (32, 46), (32, 47), (32, 48), (32, 49), (32, 50), (32, 51), (32, 52), (33, 8), (33, 9), (33, 10), (33, 20), (33, 21), (33, 22), (33, 22), (33, 23), (33, 23), (33, 24), (33, 25), (33, 44), (33, 45), (33, 46), (33, 47), (33, 48), (33, 49), (33, 50), (33, 51), (33, 52), (34, 8), (34, 9), (34, 10), (34, 19), (34, 20), (34, 21), (34, 22), (34, 23), (34, 24), (34, 25), (34, 26), (34, 44), (34, 45), (34, 46), (34, 47), (34, 48), (34, 49), (34, 50), (34, 51), (34, 52), (34, 53), (35, 8), (35, 9), (35, 10), (35, 17), (35, 18), (35, 19), (35, 20), (35, 25), (35, 26), (35, 27), (35, 28), (35, 52), (35, 53), (35, 54), (35, 55), (36, 8), (36, 9), (36, 10), (36, 17), (36, 18), (36, 19), (36, 26), (36, 27), (36, 28), (36, 53), (36, 54), (36, 55), (37, 8), (37, 9), (37, 10), (37, 17), (37, 18), (37, 19), (37, 26), (37, 27), (37, 28), (37, 53), (37, 54), (37, 54), (37, 55), (38, 8), (38, 9), (38, 10), (38, 17), (38, 18), (38, 19), (38, 26), (38, 27), (38, 28), (38, 53), (38, 54), (38, 54), (38, 55), (39, 8), (39, 9), (39, 10), (39, 17), (39, 18), (39, 19), (39, 26), (39, 27), (39, 28), (39, 53), (39, 54), (39, 55), (40, 8), (40, 9), (40, 10), (40, 11), (40, 17), (40, 18), (40, 19), (40, 26), (40, 27), (40, 28), (40, 52), (40, 53), (40, 54), (40, 55), (41, 10), (41, 11), (41, 12), (41, 13), (41, 14), (41, 15), (41, 16), (41, 17), (41, 18), (41, 19), (41, 26), (41, 27), (41, 28), (41, 29), (41, 30), (41, 31), (41, 32), (41, 33), (41, 34), (41, 35), (41, 36), (41, 37), (41, 38), (41, 39), (41, 40), (41, 41), (41, 42), (41, 43), (41, 44), (41, 45), (41, 46), (41, 47), (41, 48), (41, 49), (41, 50), (41, 51), (41, 52), (41, 53), (42, 11), (42, 12), (42, 13), (42, 14), (42, 15), (42, 16), (42, 17), (42, 18), (42, 19), (42, 26), (42, 27), (42, 28), (42, 29), (42, 30), (42, 31), (42, 32), (42, 33), (42, 34), (42, 35), (42, 36), (42, 37), (42, 38), (42, 39), (42, 40), (42, 41), (42, 42), (42, 43), (42, 44), (42, 45), (42, 46), (42, 47), (42, 48), (42, 49), (42, 50), (42, 51), (42, 52), (43, 11), (43, 12), (43, 13), (43, 14), (43, 15), (43, 16), (43, 17), (43, 18), (43, 19), (43, 26), (43, 27), (43, 28), (43, 29), (43, 30), (43, 31), (43, 32), (43, 33), (43, 34), (43, 35), (43, 36), (43, 37), (43, 38), (43, 39), (43, 40), (43, 41), (43, 42), (43, 43), (43, 44), (43, 45), (43, 46), (43, 47), (43, 48), (43, 49), (43, 50), (43, 51), (43, 52), (44, 17), (44, 18), (44, 19), (44, 26), (44, 27), (44, 28), (45, 17), (45, 18), (45, 19), (45, 26), (45, 27), (45, 28), (46, 17), (46, 18), (46, 19), (46, 20), (46, 25), (46, 26), (46, 27), (46, 28), (47, 19), (47, 20), (47, 21), (47, 22), (47, 23), (47, 24), (47, 25), (47, 26), (48, 20), (48, 21), (48, 22), (48, 22), (48, 23), (48, 23), (48, 24), (48, 25), (49, 20), (49, 21), (49, 22), (49, 23), (49, 24), (49, 25)]
    unfilledSpots = [(y,x) for y,x in amongus_spots if grid[y][x] != p if max_neighbors(grid,p,(y,x)) < 7 if neighbors(grid,p,(y,x)) < 5]
    if random.randint(1,int(1+100*len(unfilledSpots)/len(amongus_spots))) == 0:
        return random.choice(unfilledSpots)
    best = 0
    bestSpots = []
    for i in range(min(1+int(20*(1-len(unfilledSpots)/len(amongus_spots))),2*len(unfilledSpots))):
        y,x = random.choice(unfilledSpots)
        score = 0
        for i,j in adjacent_spots((y,x)):
            if binary_search(amongus_spots,(i,j)):
                myNeighbors = neighbors(grid,p,(i,j))
                if grid[i][j] == p:
                    score += 9-myNeighbors
                else:
                    score += myNeighbors
            if not binary_search(amongus_spots,(i,j)) and grid[i][j] not in (0,p):
                score += 5
        if neighbors(grid,p,(y,x)) == 3 and max_neighbors(grid,p,(y,x)) == 5:
            score += 10
        if max_neighbors(grid,p,(y,x)) == 6:
            score -= 1
        score += 2*neighbors(grid,0,(y,x))
        if score > best:
            best = score
            bestSpots = [(y,x)]
        elif score == best:
            bestSpots.append((y,x))
    if len(bestSpots) > 0:
        return random.choice(bestSpots)
    else:
        farthestDist = 0
        farthestDistCells = []
        for y in range(len(grid)):
            for x in range(len(grid)):
                if grid[y][x] != p:
                    dist = max(abs(x-32),abs(y-32))
                    if dist > farthestDist:
                        farthestDist = dist
                        farthestDistCells = [(y,x)]
                    elif dist == farthestDist:
                        farthestDistCells.append((y,x))
        if len(farthestDistCells) > 0:
            return random.choice(farthestDistCells)
        else:
            farthestDist = 0
            farthestDistCells = []
            for y in range(len(grid)):
                for x in range(len(grid)):
                    if grid[y][x] != p:
                        dist = max(abs(x-32),abs(y-32))
                        if dist > farthestDist:
                            farthestDist = dist
                            farthestDistCells = [(y,x)]
                        elif dist == farthestDist:
                            farthestDistCells.append((y,x))

def op_oliver(grid,p):
    valid = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == p:
                for y,x in [(i-2,j),(i-2,j-1),(i-2,j-2),(i-1,j-2),(i,j-2),(i+1,j-2),(i+2,j-2),(i+2,j-1),(i+2,j),(i+2,j+1),(i+2,j+2),(i+1,j+2),(i,j+2),(i-1,j+2),(i-2,j+2),(i-2,j+1)]:
                    if 0 <= y < 64 and 0 <= x < 64:
                        if grid[y][x] != p and max_neighbors(grid,p,(y,x)) < 7:
                            works = True
                            for a,b in adjacent_spots((y,x)):
                                if grid[a][b] == p:
                                    works = False
                            if works or random.randint(1,3) == 1:
                                valid.append((y,x))
    if len(valid) == 0:
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == p:
                    valid += [(a,b) for a,b in adjacent_spots((i,j)) if grid[a][b] != p]
    if len(valid) == 0:
        return (random.randint(0,63),random.randint(0,63))
    return random.choice(valid)


class IanAis:
    Charles = name("Cracked Charles", (200,250,250))(cracked_charles)
    Andy = name("Among Us Andy", (197, 17, 17))(amongus_andy)
    Oliver = name("OP Oliver", (97, 17, 78))(op_oliver)