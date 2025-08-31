from helpers import *
from scipy.signal import convolve2d as c
# def o(g,p):
#     """Concise variable names for code-golfing"""
#     # variables used repeatedly given concise names
#     g=np.array(g)
#     n=g!=p
#     k=np.ones((3,3))
#     k[1,1]=0
    
#     pn = c(1-n,k,m:='same') * n * (1-(g!=0)*.9) # player_neighbors
#     v = 5 ** pn # values
#     s = c(v,k,m) * n * (c(n*(g>0), k, m) < 7) # scores
#     return divmod(np.argmax(s),64)
def o(g,p):g=np.array(g);n=g!=p;k=np.ones((3,3));k[1,1]=0;return divmod(np.argmax(c(5**(c(1-n,k,m:='same')*n*(1-(g!=0)*.9)),k,m)*n*(c(n*(g>0),k,m)<7)),64)

class Golf:
    olli = name("Ollie", (50, 168, 90))(o)