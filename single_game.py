"""
run a single tournament game without display
"""
from all_bots import *
import sys

ids = [int(i) for i in sys.argv[1:5]]
bots = [ALL_BOTS[x] for x in ids]

rounds = 2001

g = VotingGame(GameConstants.GRID_SIZE, bots, 6)

for rnd in range(rounds):
    g.run_round()
# save game results in outputs.txt
with open("outputs.txt", "a") as f:
    for x in range(4):
        print(ids[x], g.score[x+1], file=f)