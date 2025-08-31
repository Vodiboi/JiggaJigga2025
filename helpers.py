"""
Helper functions and libraries for working on your bot
"""
import numpy as np
import copy
import random
import signal
import functools
from contextlib import redirect_stdout
from collections import defaultdict, deque
from time import time_ns
import scipy
import itertools

def wrp(x, size):
    return np.maximum(np.minimum(x, size-1), 0)

def spots_adj(pt, grid_size):
    """
    Helper function that returns adjacent spots to a cell
    pt: the said cell
    grid_size: the grid size (i.e. len(grid)) 
    """
    y = wrp(np.array([-1, 0, 1]) + pt[0], grid_size)
    x = wrp(np.array([-1, 0, 1]) + pt[1], grid_size)
    xx, yy = np.meshgrid(x, y)
    return list(set(list(zip(yy.flatten()[np.arange(9)], xx.flatten()[np.arange(9)]))))

# timeout code for ensuring slow code does not slow down the game
# (partly courtesy of gpt)
class TimeoutException(Exception):
    pass

def timeout_handler(signum, frame):
    raise TimeoutException

def run_with_timeout(timeout, func, *args, **kwargs):
    # # Set the signal handler for SIGALRM
    signal.signal(signal.SIGALRM, timeout_handler)
    # Schedule the SIGALRM signal to be sent after `timeout` seconds
    signal.setitimer(signal.ITIMER_REAL, timeout)
    
    try:
        result = func(*args, **kwargs)
    except TimeoutException:
        return None
    except Exception as e:
        return ("Error Raised", e)
    finally:
        # Cancel the alarm
        signal.setitimer(signal.ITIMER_REAL, 0)
    # result = func(*args, **kwargs)
    return result


# courtesy of https://stackoverflow.com/questions/47452513/how-do-you-implement-str-for-a-function with some modfications
def name(nm, col):
    """
    function to give a name and color to each bot
    """
    def wrapper (f):
        class FuncType:
            def __call__ (self, *args, **kwargs):
                # call the original function
                return f(*args, **kwargs)
            def __str__ (self):
                # call the custom __str__ function
                if self.CLASSNAME is not None:
                    return self.CLASSNAME + " " + nm
                return nm
            def _color4game(self):
                # bad function name so not to be accidentally mess with an exisiting variable/function
                return col
        # decorate with functool.wraps to make the resulting function appear like f
        return functools.wraps(f)(FuncType())
    return wrapper
    
class PrintRedirectorStream:
    """
    a system to redirect bot print statements to the log file

    credit: Jasper Ng (from last year's Jigga Jigga)
    """

    def __init__(self, out):
        self.out = out
        self.current_plr = None
        self.has_written = False

    def set_cur_plr(self, plr):
        self.current_plr = plr
        self.has_written = False

    def write(self, val):
        if not self.has_written:
            self.out._log(f"{self.current_plr} has printed: ")
            self.has_written = True
        self.out._log(val)
