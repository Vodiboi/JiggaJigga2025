"""
While the real tournament is running behind the scenes,
show footage of gameplay to enterain viewers
"""
from helpers import *
from game import *
from all_bots import ALL_BOTS
import pygame
def run_game(rounds=2000):
    bots = random.sample(ALL_BOTS, 4)
    game = VotingGame(GameConstants.GRID_SIZE, bots, 0.05)
    disp = StandardGameDisplay(
        pygame,
        game, 
        GameConstants.GRID_SIZE, 
        GameConstants.SIZE, 
        GameConstants.SCR_WIDTH, 
        GameConstants.SCR_HEIGHT, 
        GameConstants.BLOCK_SIZE, 
        GameConstants.FPS,
        rounds
    )

    for rnd in range(rounds):
        if not disp.run_round(rnd):
            break

if __name__ == "__main__":
    while True:
        run_game()
