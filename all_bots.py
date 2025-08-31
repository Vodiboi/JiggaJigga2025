"""
All bots for the tournament
"""
from helpers import *
from bots.aayan_bots import *
from game import *
from bots.sample_ais import *
from bots.spencer import SpencerAis
from bots.ian import IanAis
from bots.lionel import LionelAis
from bots.elizabeth import ElizabethAis
from bots.utsav import UtsavAis
from bots.eric import EricAis
from bots.oskar import OskarAis, OskarHack
from bots.golf import Golf

BOT_CLASSES = [AayanBots, OtherBots, SampleAis, SpencerAis, IanAis, LionelAis, ElizabethAis, UtsavAis, EricAis, OskarAis, OskarHack, Golf]

ALL_BOTS = []
for c in BOT_CLASSES:
    for (k, v) in vars(c).items():
        if not k.startswith("_"):
            v.CLASSNAME = c.__name__
    ALL_BOTS.extend([v for (k, v) in vars(c).items() if not k.startswith("_")])
BOT_NAMES = [str(i) for i in ALL_BOTS]



