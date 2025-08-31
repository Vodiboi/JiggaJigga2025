"""
Play a single game with selected bots
"""
from helpers import *
from all_bots import *
import pygame

if __name__ == "__main__":
    # the below line is the only one that needs to be changed by you
    bots = [IanAis.Charles, OtherBots.FastChainReaction, SampleAis.Gukesh, Golf.olli]
    
    # this makes for good gameplay
    rounds = 2001

    # the timeout is 0.05 seconds for a bot move, otherwise the game would take too long
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

    disp.stall()