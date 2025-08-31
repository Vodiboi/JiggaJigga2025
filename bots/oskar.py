from bots.oskarbotscopy import oskarbot, oskarbot2, oskarbot3, Hugo, Andy
from helpers import *
class OskarAis:
    oskar1 = name("Oskar 1", (252, 186, 3))(oskarbot)
    oskar2 = name("Oskar 2", (47, 173, 159))(oskarbot2)
    oskar3 = name("Oskar 3", (128, 194, 130))(oskarbot3)

class OskarHack:
    # hugo = name("Huga", (50, 156, 78))(Hugo)
    hugo = Hugo
    andy = name("Andy", (50, 29, 71))(Andy)