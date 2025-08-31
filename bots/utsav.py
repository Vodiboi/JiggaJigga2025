from helpers import *

import time
import random


def fractal_franny(grid, p):

    t1 = time.time()

    posdict = {}
    k = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            posdict[(i,j)] = 0 if grid[i][j] != p else 1
            if posdict[(i,j)] == 1:
                k = True

    if not k:
        return (random.randrange(0, 65), random.randrange(0, 65))

    for m in range(0, 1):
        poslist = []
        minx = 64
        maxx = 0
        miny = 64
        maxy = 0
        for i in posdict:
            if posdict[i] == 1:
                minx = min(i[0], minx)
                miny = min(i[1], miny)
                maxx = max(i[0], maxx)
                maxy = max(i[1], maxy)
        ws = 5
        minx = max(0, minx-ws)
        miny = max(0, miny-ws)
        maxx = min(64, maxx+ws)
        maxy = min(64, maxy+ws)
        newposdict = {}
        for i in range(minx, maxx):
            for j in range(miny, maxy):
                if posdict[(i,j)] == 0:
                    poslist.append((i,j))
                newposdict[(i,j)]=True


        pos = random.choice(poslist)
        while True:
            if time.time()-t1 > 0.02:
                break
            x = pos[0]
            y = pos[1]
            if (x-1,y) in posdict and posdict[(x-1, y)] == 1:
                break
            if (x+1,y) in posdict and posdict[(x+1, y)] == 1:
                break
            if (x,y-1) in posdict and posdict[(x, y-1)] == 1:
                break
            if (x,y+1) in posdict and posdict[(x, y+1)] == 1:
                break
            newlist = []
            for i in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if i in newposdict:
                    newlist.append(i)
            pos = random.choice(newlist)
        return pos

class UtsavAis:
    fractal_franny = name("Fractal Franny", (255, 255, 255))(fractal_franny)