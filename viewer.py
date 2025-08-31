"""
Displays the game scoreboard within a terminal window
"""
from tournament_stages import *
import time
while True:
    disp_scoreboard_s1("", *get_scores_s1())
    # refresh the scoreboard at 2 Hz
    time.sleep(0.5)
