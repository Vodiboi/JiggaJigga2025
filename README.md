# Jigga Jigga 2025

I ran my school's annual Jigga Jigga competition this spring. Jigga Jigga is an annual game competition at my school where students code bots to play a game competitively.

This year, the game was called "Politician Simulator", and the rules are given [here](https://docs.google.com/document/d/12al8sjD0eWckV0t4ydhDed-ewNURp6g2a1v54ZSj0Iw/edit?usp=sharing).

This year, I am going to be doing something unusual, in that I will be making everything (including bots that played in the tournament, and many of my own bots which were kept private before the tournament) public. I hope that this will help anyone who stumbles onto this game in finding good strategies.

I also want to give a special thanks to Eric Severson for his invaluable help on reviewing and playtesting the game, and also figuring out an optimization that made the game about 33% faster (if you're curious, speeding up updt_cells in [game.py](game.py) by using convolutions, which I hadn't thought to do). I would also like to thank Dr. V for giving me the opportunity to run Jigga Jigga this year. 


## To Run a Single Game with Selected Bots

In line 9 of [main.py](main.py), change the bots to be whichever bots you want. Then, run `python3 main.py` to watch a game with the selected bots.

## Run a Continuous Feed of Random Games

This is useful for entertaining people while the tournament is running in the background.

To do this, run `python3 random_games.py`

## Run a Tournament of Games

First, you are going to need to run `python3 tournament.py`. This will enter in a command to run many games in parallel in the background into [tournament.sh](tournament.sh). Then, run this file by typing `./tournament.sh` into the terminal. 

To see the results of the tournament live, open a new terminal window and run `python3 viewer.py`

