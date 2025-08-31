"""
Add list of tournament games to tournament.sh files
"""
from tournament_stages import *
if __name__ == "__main__":
    print(create_games("tournament.sh", 2))