from scipy import signal as sgnl
from helpers import *
import pygame

# # def fast_filling_phil(grid, p):
# #     # Convert grid to numpy array if it's not already
# #     grid_arr = np.array(grid)
# #     grid_size = len(grid_arr)
    
# #     # Create binary masks
# #     opponent_mask = ((grid_arr != p) & (grid_arr != 0)).astype(float)
# #     player_mask = (grid_arr == p).astype(float)
# #     empty_mask = (grid_arr == 0).astype(float)
# #     non_player_mask = (grid_arr != p).astype(float)
    
# #     # If no opponents and no player pieces, return random position
# #     if not np.any(opponent_mask) and not np.any(player_mask):
# #         return random.randint(0, grid_size-1), random.randint(0, grid_size-1)

# #     # Kernel to count neighbors
# #     neighbor_kernel = np.ones((3, 3))
# #     neighbor_kernel[1, 1] = 0  # Don't count the cell itself
# #     # Count player neighbors for each cell
# #     player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
# #     squares_that_fill = (player_neighbors == 5) * empty_mask # set score to 0 on squares that will already fill
# #     ignore = sgnl.convolve2d(squares_that_fill, neighbor_kernel,mode='same')
# #     player_neighbors *= (player_neighbors < 5).astype(float)
# #     bonus = 3 ** player_neighbors
# #     scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * non_player_mask * (ignore == 0)
# #     # print(scores)
# #     # print(f'played at {np.unravel_index(np.argmax(scores), scores.shape)}')
# #     return np.unravel_index(np.argmax(scores), scores.shape)


# def fast_filling_phil(grid, p):
#     # Convert grid to numpy array if it's not already
#     grid_arr = np.array(grid)
#     grid_size = len(grid_arr)
    
#     # Create binary masks
#     opponent_mask = ((grid_arr != p) & (grid_arr != 0)).astype(float)
#     player_mask = (grid_arr == p).astype(float)
#     empty_mask = (grid_arr == 0).astype(float)
#     non_player_mask = (grid_arr != p).astype(float)
    
#     # If no opponents and no player pieces, return random position
#     if not np.any(opponent_mask) and not np.any(player_mask):
#         return random.randint(0, grid_size-1), random.randint(0, grid_size-1)

#     # Kernel to count neighbors
#     neighbor_kernel = np.ones((3, 3))
#     neighbor_kernel[1, 1] = 0  # Don't count the cell itself
#     # Count player neighbors for each cell
#     player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
#     squares_that_fill = (player_neighbors == 5) * empty_mask # set score to 0 on squares that will already fill
#     ignore = sgnl.convolve2d(squares_that_fill, neighbor_kernel,mode='same')
#     player_neighbors *= (player_neighbors < 5).astype(float)
#     bonus = 3 ** player_neighbors
#     scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * non_player_mask * (ignore == 0)

#     opponent_kernel = np.array([
#         [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
#         [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
#         [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
#         [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
#         [0   ,-50 ,-50 ,-50 ,100 ,-50 ,-50 ,-50 ,0   ],
#         [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
#         [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
#         [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
#         [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
#     ], dtype=float)

#     scores += sgnl.convolve2d(opponent_mask, opponent_kernel, mode='same')

#     return np.unravel_index(np.argmax(scores), scores.shape)

# class Phil:
#     def __str__(self):
#         return "Fast Filling Phil"
#     def _color4game(self):
#         # bad function name so not to be accidentally mess with an exisiting variable/function
#         return (13, 89, 116)
#     def __call__(self,grid, p):
#         # Convert grid to numpy array if it's not already
#         grid_arr = np.array(grid)
#         grid_size = len(grid_arr)
    
#         # Create binary masks
#         opponent_mask = ((grid_arr != p) & (grid_arr != 0)).astype(float)
#         player_mask = (grid_arr == p).astype(float)
#         empty_mask = (grid_arr == 0).astype(float)
#         non_player_mask = (grid_arr != p).astype(float)

#         # If no opponents and no player pieces, return random position
#         if not np.any(opponent_mask) and not np.any(player_mask):
#             return random.randint(0, grid_size-1), random.randint(0, grid_size-1)
#         if np.sum(empty_mask) > 10:
#             # Kernel to count neighbors
#             neighbor_kernel = np.ones((3, 3))
#             neighbor_kernel[1, 1] = 0  # Don't count the cell itself
#             # Count player neighbors for each cell
#             player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
#             squares_that_fill = (player_neighbors == 5) * empty_mask # set score to 0 on squares that will already fill
#             ignore = sgnl.convolve2d(squares_that_fill, neighbor_kernel,mode='same')
#             player_neighbors *= (player_neighbors < 5).astype(float)
#             bonus = 3 ** player_neighbors
#             scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * non_player_mask * (ignore == 0)
#             # print(scores)
#             opponent_kernel = np.array([
#                 [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
#                 [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
#                 [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
#                 [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
#                 [0   ,-50 ,-50 ,-50 ,100 ,-50 ,-50 ,-50 ,0   ],
#                 [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
#                 [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
#                 [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
#                 [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
#             ], dtype=float)
#             opp_avoidance = sgnl.convolve2d(opponent_mask, opponent_kernel,mode='same')
#             scores += opp_avoidance
#             if np.max(scores) < 0:
#                 scores -= opp_avoidance

#         else:
#             neighbor_kernel = np.ones((3, 3))
#             neighbor_kernel[1, 1] = 0  # Don't count the cell itself
#             # Count player neighbors for each cell
#             player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
#             squares_that_fill = (player_neighbors >= 7) * empty_mask # set score to 0 on squares that will already fill
#             ignore = sgnl.convolve2d(squares_that_fill, neighbor_kernel,mode='same')
#             bonus = 3 ** player_neighbors
#             scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * (ignore == 0)
#         scores -= (10 ** 5) * player_mask # make sure to never play own spot
#         x, y = np.unravel_index(np.argmax(scores), scores.shape)
 
#         return np.unravel_index(np.argmax(scores), scores.shape)
    
# class EricAis:
#     Old_Phil = name("Old Phil", (13, 89, 16))(fast_filling_phil)
#     Phil = Phil()


from helpers import *
from matplotlib import pyplot as plt
import pickle


def random_raja(grid, p):
    """Picks a random cell"""
    return random.randint(0, len(grid)-1), random.randint(0, len(grid)-1)

def row_by_row_rishi(grid, p):
    """
    Goes row by row, tries to convince houses it is yet to convince
    """
    for y in range(len(grid)):
        for x in range(len(grid)):
            if grid[x][y] != p:
                # either empty or convinced to vote for another player
                return (x, y)
    # no free cells left, just pick a house randomly
    return random_raja(grid, p)

def row_by_row_rishi2(grid, p):
    """
    Goes row by row, tries to convince houses it is yet to convince
    """
    for y in reversed(range(len(grid))):
        for x in range(len(grid)):
            if grid[x][y] != p:
                # either empty or convinced to vote for another player
                return (x, y)
    # no free cells left, just pick a house randomly
    return random_raja(grid, p)

def row_by_row_rishi3(grid, p):
    """
    Goes row by row, tries to convince houses it is yet to convince
    """
    for y in range(len(grid)):
        for x in reversed(range(len(grid))):
            if grid[x][y] != p:
                # either empty or convinced to vote for another player
                return (x, y)
    # no free cells left, just pick a house randomly
    return random_raja(grid, p)

def row_by_row_rishi4(grid, p):
    """
    Goes row by row, tries to convince houses it is yet to convince
    """
    for y in reversed(range(len(grid))):
        for x in reversed(range(len(grid))):
            if grid[x][y] != p:
                # either empty or convinced to vote for another player
                return (x, y)
    # no free cells left, just pick a house randomly
    return random_raja(grid, p)

def growing_gukesh(grid, p):
    """
    Tries to convince a house next to a house it already convinced
    """
    valid = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == p:
                # try claiming adjacent to this guy
                for y, x in spots_adj((i, j), grid_size=len(grid)):
                    if grid[y][x] != p:
                        # make sure we aren't reclaiming our own land
                        valid.append((y, x))
    if len(valid) == 0:
        # we have not convinced anyone, so pick randomly
        return random_raja(grid, p)
    # randomly pick a valid cell
    a = random.choice(valid)
    return a


def perimeter_pranav(grid, p):
    '''
    always tries to play next to a house that is 
    convinced to vote for a different politician.
    If it can't do that, it resorts to random.
    '''
    possible_spots = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] not in [p, 0]:
                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    # using the wrp function, which prevents out of bounds
                    # use dy and dx to compute the new y and x coords
                    x2 = wrp((j+dx), len(grid))
                    y2 = wrp((i+dy), len(grid))
                    if grid[y2][x2] == 0:
                        possible_spots.append((y2, x2))
    if len(possible_spots) == 0:
        return (random.randint(0, len(grid)-1), random.randint(0, len(grid)-1))
    return random.choice(possible_spots)


import time

def lonely_lance(grid, p):
    """
    Strategic placement that:
    1. Avoids opponent pieces (using a small repulsion kernel)
    2. Prefers positions near own pieces but with strategic gaps
    3. Never plays on already occupied cells
    4. Considers the 5/8 neighbor rule for automatic cell filling
    
    Args:
        grid: 2D grid where 0 is empty, p is player, other values are opponents
        p: player number
    
    Returns:
        (x, y) tuple of best move position
    """
    # Convert grid to numpy array if it's not already
    grid_arr = np.array(grid)
    grid_size = len(grid_arr)
    
    # Create binary masks
    opponent_mask = ((grid_arr != p) & (grid_arr != 0)).astype(float)
    player_mask = (grid_arr == p).astype(float)
    empty_mask = (grid_arr == 0).astype(float)
    
    # If no opponents and no player pieces, return random position
    if not np.any(opponent_mask) and not np.any(player_mask):
        return random.randint(0, grid_size-1), random.randint(0, grid_size-1)
    

    # --- STEP 1: Create repulsion field from opponents ---
    # Use a smaller kernel for opponent repulsion (only care about nearby opponents)
    opponent_kernel_size = min(11, grid_size)  # Smaller kernel
    y, x = np.ogrid[-opponent_kernel_size//2:opponent_kernel_size//2+1, 
                    -opponent_kernel_size//2:opponent_kernel_size//2+1]
    dist_squared = x**2 + y**2
    # Stronger localized repulsion
    opponent_kernel = 1 / (1e-5 + dist_squared)
    opponent_kernel[opponent_kernel_size//2 + 1, opponent_kernel_size//2 +1] = -1
    opponent_kernel = opponent_kernel / opponent_kernel.sum()
    
    # Convolve opponent mask with kernel to get "repulsion field"
    repulsion = sgnl.convolve2d(opponent_mask, opponent_kernel, mode='same')


    
    # --- STEP 2: Create attraction field for strategic positioning near own pieces ---
    # Create a "strategic positioning" kernel to encourage positions near player pieces
    # but with small gaps (to exploit the 5/8 rule)
    strategic_kernel_size = 5  # 5x5 kernel covers immediate neighbors plus one more cell
    strategic_kernel = np.zeros((strategic_kernel_size, strategic_kernel_size))
    
    # Fill in the strategic kernel:
    # - Zero at center (don't play on self)
    # - Positive values at a distance of exactly 2 cells (diagonal or orthogonal)
    # - Slightly negative values at immediate neighbors (keep some gaps)
    center = strategic_kernel_size // 2
    for i in range(strategic_kernel_size):
        for j in range(strategic_kernel_size):
            # Calculate Manhattan distance from center
            manhattan_dist = abs(i - center) + abs(j - center)
            # Calculate Chebyshev distance (maximum of x or y distance)
            chebyshev_dist = max(abs(i - center), abs(j - center))
            
            if manhattan_dist == 0:  # Center point
                strategic_kernel[i, j] = 0  # Never play on existing piece
            elif chebyshev_dist == 1:  # Immediate neighbors
                strategic_kernel[i, j] = -0.2  # Slightly discourage (to create gaps)
            elif chebyshev_dist == 2:  # Two cells away
                strategic_kernel[i, j] = 1.0  # Encourage these positions
            else:
                strategic_kernel[i, j] = 0.1  # Slight preference for other positions
    
    # Normalize the strategic kernel
    strategic_kernel = strategic_kernel / np.abs(strategic_kernel).sum()

    
    # Convolve player mask with strategic kernel
    strategy_field = sgnl.convolve2d(player_mask, strategic_kernel, mode='same')
    
    # --- STEP 3: Count neighbors for each empty cell ---
    # Kernel to count neighbors
    neighbor_kernel = np.ones((3, 3))
    neighbor_kernel[1, 1] = 0  # Don't count the cell itself
    
    # Count player neighbors for each cell
    player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
    
    # --- STEP 4: Combine all factors into a final score ---
    # 1. Avoid opponent pieces (minimize repulsion)
    # 2. Follow strategic positioning (maximize strategy_field)
    # 3. Favor positions that could trigger the 5/8 rule later
    
    count_size = 9
    count = np.ones((count_size,count_size))
    count[count_size//2 + 1, count_size//2 +1] = 0
    empties = sgnl.convolve2d(opponent_mask, count , mode='same')
    empties = (empties == 0)
    # Create a combined score (lower is better)
    combined_score = repulsion - strategy_field * 3 - empties * 100
    


    # # Adjust scores based on the 5/8 rule potential:
    # # For cells with 3-4 player neighbors, they're close to triggering the rule
    # rule_potential = np.zeros_like(combined_score)
    # # Boost cells that have 3-4 neighbors (on track to reach 5/8)
    # rule_potential[(player_neighbors >= 3) & (player_neighbors <= 4)] -= 0.5
    # combined_score += rule_potential
    
    # Only consider empty cells
    combined_score[empty_mask == 0] = np.inf
    
    # Find position with minimum combined score
    best_pos = np.unravel_index(np.argmin(combined_score), combined_score.shape)
    
    # If best_pos has a score of infinity, find any empty cell
    if combined_score[best_pos] == np.inf:
        empty_positions = np.argwhere(empty_mask == 1)
        if len(empty_positions) > 0:
            idx = random.randint(0, len(empty_positions) - 1)
            return tuple(empty_positions[idx])
        else:
            # No empty cells left
            return random.randint(0, grid_size-1), random.randint(0, grid_size-1)
    return best_pos

# from scipy import sgnl



def fast_filling_phil(grid, p):
    print(f'My number is {p}')
    # Convert grid to numpy array if it's not already
    grid_arr = np.array(grid)
    grid_size = len(grid_arr)
    
    # Create binary masks
    opponent_mask = ((grid_arr != p) & (grid_arr != 0)).astype(float)
    player_mask = (grid_arr == p).astype(float)
    empty_mask = (grid_arr == 0).astype(float)
    non_player_mask = (grid_arr != p).astype(float)
    
    # If no opponents and no player pieces, return random position
    if not np.any(opponent_mask) and not np.any(player_mask):
        return random.randint(0, grid_size-1), random.randint(0, grid_size-1)

    # Kernel to count neighbors
    neighbor_kernel = np.ones((3, 3))
    neighbor_kernel[1, 1] = 0  # Don't count the cell itself
    # Count player neighbors for each cell
    player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
    squares_that_fill = (player_neighbors == 5) * empty_mask # set score to 0 on squares that will already fill
    ignore = sgnl.convolve2d(squares_that_fill, neighbor_kernel,mode='same')
    player_neighbors *= (player_neighbors < 5).astype(float)
    bonus = 3 ** player_neighbors
    scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * non_player_mask * (ignore == 0)
    # print(scores)
    opponent_kernel = np.array([
        [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
        [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
        [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
        [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
        [0   ,-50 ,-50 ,-50 ,100 ,-50 ,-50 ,-50 ,0   ],
        [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
        [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
        [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
        [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
    ], dtype=float)
    np.set_printoptions(threshold=10**5)
    # empty_space = sgnl.convolve2d(opponent_mask, opponent_kernel, mode='same') == 0
    # if empty_space.any():
    #     scores *= empty_space
    scores += sgnl.convolve2d(opponent_mask, opponent_kernel, mode='same')
    # print('after opp mask')
    # print(scores)
    # print(f'played at {np.unravel_index(np.argmax(scores), scores.shape)}')
    return np.unravel_index(np.argmax(scores), scores.shape)

class Phil:
    def __str__(self):
        return "Fast Filling Phil"
    def _color4game(self):
        # bad function name so not to be accidentally mess with an exisiting variable/function
        return (0, 100, 0)
    def __call__(self,grid, p):
        # Convert grid to numpy array if it's not already
        grid_arr = np.array(grid)
        grid_size = len(grid_arr)
    
        # Create binary masks
        opponent_mask = ((grid_arr != p) & (grid_arr != 0)).astype(float)
        player_mask = (grid_arr == p).astype(float)
        empty_mask = (grid_arr == 0).astype(float)
        non_player_mask = (grid_arr != p).astype(float)

        # If no opponents and no player pieces, return random position
        if not np.any(opponent_mask) and not np.any(player_mask):
            return random.randint(0, grid_size-1), random.randint(0, grid_size-1)
        if np.sum(empty_mask) > 10:
            # Kernel to count neighbors
            neighbor_kernel = np.ones((3, 3))
            neighbor_kernel[1, 1] = 0  # Don't count the cell itself
            # Count player neighbors for each cell
            player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
            squares_that_fill = (player_neighbors == 5) * empty_mask # set score to 0 on squares that will already fill
            ignore = sgnl.convolve2d(squares_that_fill, neighbor_kernel,mode='same')
            player_neighbors *= (player_neighbors < 5).astype(float)
            bonus = 3 ** player_neighbors
            scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * non_player_mask * (ignore == 0)
            # print(scores)
            opponent_kernel = np.array([
                [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
                [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
                [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
                [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
                [0   ,-50 ,-50 ,-50 ,100 ,-50 ,-50 ,-50 ,0   ],
                [0   ,0   ,-50 ,-50 ,-50 ,-50 ,-50 ,0   ,0   ],
                [0   ,0   ,0   ,-50 ,-50 ,-50 ,0   ,0   ,0   ],
                [0   ,0   ,0   ,0   ,-50 ,0   ,0   ,0   ,0   ],
                [0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
            ], dtype=float)
            opp_avoidance = sgnl.convolve2d(opponent_mask, opponent_kernel,mode='same')
            scores += opp_avoidance
            if np.max(scores) < 0:
                scores -= opp_avoidance
            # opp_kernel_size = 9
            # opponent_kernel = np.ones((opp_kernel_size, opp_kernel_size))
            # opponent_kernel[opp_kernel_size // 2, opp_kernel_size // 2] = 0
            # empty_space = sgnl.convolve2d(opponent_mask, np.ones((9,9)), mode='same') == 0
            # if empty_space.any():
            #     scores *= empty_space
        else:
            neighbor_kernel = np.ones((3, 3))
            neighbor_kernel[1, 1] = 0  # Don't count the cell itself
            # Count player neighbors for each cell
            player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
            squares_that_fill = (player_neighbors >= 7) * empty_mask # set score to 0 on squares that will already fill
            ignore = sgnl.convolve2d(squares_that_fill, neighbor_kernel,mode='same')
            bonus = 3 ** player_neighbors
            scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * (ignore == 0)
        scores -= (10 ** 5) * player_mask # make sure to never play own spot
        x, y = np.unravel_index(np.argmax(scores), scores.shape)
        # print(f'Playing at {x,y}, currently has {grid[x][y]} with score {scores[x,y]}')

        
        return np.unravel_index(np.argmax(scores), scores.shape)


class Component:
    """A class to store a connected component of squares"""
    def __init__(self, grid_size = 64):
        self.grid_size = grid_size
        self.squares = set()
        self.xmin = grid_size
        self.xmax = 0
        self.ymin = grid_size
        self.ymax = 0
        self.mean = np.zeros(2)

    def add(self, i, j):
        self.mean = self.mean * len(self.squares) + np.array([i,j])
        self.squares.add((i,j))
        self.mean /= len(self.squares)
        self.xmin = min(i, self.xmin)
        self.xmax = max(i, self.xmax)
        self.ymin = min(j, self.ymin)
        self.ymax = max(j, self.ymax)
        assert np.sum((self.mean - np.mean(np.array(list(self.squares)), axis=0)) ** 2) < 0.1

    def remove(self, i, j):
        self.mean = self.mean * len(self.squares) - np.array([i,j])
        self.squares.remove((i,j))
        if len(self.squares) == 0:
            return
        self.mean /= len(self.squares)
        if i == self.xmin:
            self.xmin = min(x for (x,y) in self.squares)
        if i == self.xmax:
            self.xmax = max(x for (x,y) in self.squares)
        if j == self.ymin:
            self.ymin = min(y for (x,y) in self.squares)
        if j == self.ymax:
            self.ymax = max(y for (x,y) in self.squares)

    def __repr__(self):
        return str(len(self.squares)) + str(self.mean) + str(self.squares)

class Cluster:
    """A class to store groups clusters, which will track squares of a player"""

    def __init__(self):
        self.components = []
        self.total = 0
        self.component_map = {} #dict mapping squares to components

    def add(self, i, j):
        self.total += 1
        neighboring_components = []
        for a in [-1, 0, 1]:
            for b in [-1, 0, 1]:
                for component in self.components:
                    if (i + a, j + b) in component.squares and component not in neighboring_components:
                        neighboring_components.append(component)
        
        if len(neighboring_components) == 1:
            neighboring_components[0].add(i,j)
            self.component_map[(i,j)] = neighboring_components[0]
        else:
            new_component = Component()
            if len(neighboring_components) > 1:
                # merge components - any future merging logic goes here as component grows more complex
                new_component.squares = set.union(*[c.squares for c in neighboring_components])
                new_component.xmin = min(c.xmin for c in neighboring_components)
                new_component.ymin = min(c.ymin for c in neighboring_components)
                new_component.xmax = max(c.xmax for c in neighboring_components)
                new_component.ymax = max(c.ymax for c in neighboring_components)
                for c in neighboring_components:
                    self.components.remove(c)
                new_component.mean = np.sum([c.mean * len(c.squares) for c in  neighboring_components], axis=0) / len(new_component.squares)
            new_component.add(i,j)
            self.components.append(new_component)
            self.component_map[(i,j)] = new_component
        ## keep components sorted with largest first
        self.components.sort(key = lambda x: len(x.squares), reverse = True)

    def remove(self,i,j):
        self.total -= 1
        for c in self.components:
            if (i,j) in c.squares:
                c.remove(i, j)
                if len(c.squares) == 0:
                    self.components.remove(c)
        self.components.sort(key = lambda x: len(x.squares), reverse = True)

    def __repr__(self):
        s = f"{self.total} squares in {len(self.components)} components:\n"
        s += " ".join(str(c) for c in self.components) + "\n"
        return s

class Manny:

    def __init__(self, grid_size = 64):
        self.pause_next = False  # Flag to control debug pause
        self.grid_size = grid_size
        ## empty_squares currently not of type Cluster
        self.empty_squares = set((i,j) for i in range(grid_size) for j in range(grid_size))
        self.opponent_squares = {} # dict mapping opponent ID to a Cluster
        self.own_squares = Cluster()
        self.own_square_mask = np.zeros((grid_size, grid_size))
        self.last_grid = np.zeros((grid_size, grid_size))
        ## create numpy array counting how many empty neighboring cells there are
        self.empty_neighbors = 8* np.ones((grid_size, grid_size))
        for side_index in [(0, slice(None)), (-1, slice(None)), (slice(None), 0), (slice(None),-1)]:
            self.empty_neighbors[side_index] = 5
        for corner_index in [(0,0),(-1,0),(0,-1),(-1,-1)]:
            self.empty_neighbors[corner_index] = 3
        
        ## create numpy array counting distance to walls or clusterss
        self.obstacle_distances = np.ones((grid_size, grid_size))
        for i in range(1, grid_size // 2 + 1):
            self.obstacle_distances[i:-i, i:-i] += 1
        self.obstacle_distances *= 1.2 ## constant for edge distances
        self.lost_squares = set() # indices of squares that have been recaptured
        ## build distance table, currently L2 distances
        self.distance_table = np.zeros((2 * grid_size - 1, 2* grid_size - 1))
        for i in range(2 * grid_size - 1):
            for j in range(2 * grid_size - 1):
                self.distance_table[i,j] = ((i - (grid_size - 1))**2 + (j - (grid_size - 1))**2)**0.5

        self.num_turns = 0
        self.replay = []

    def update(self):
        """check updates from last grid"""
        dif = np.where(self.grid != self.last_grid)
        if len(dif) == 0:
            return
        for (i, j) in zip(dif[0], dif[1]):
            ## remove info from cell that went away
            if self.last_grid[i,j] == 0:
                self.empty_squares.remove((i,j))
                self.empty_neighbors[max(i-1,0):i+2,max(j-1,0):j+2] -= 1
                self.empty_neighbors[i,j] += 1
            elif self.last_grid[i,j] == self.p:
                self.own_squares.remove(i,j)
                self.own_square_mask[i,j] = 0
                self.lost_squares.add((i,j))
            else:
                self.opponent_squares[self.last_grid[i,j]].remove(i,j)
            ## add info for cell that appeared
            if self.grid[i,j] == 0:
                print(f'ERROR: cell {i,j} became empty')
            if self.grid[i,j] == self.p:
                self.own_squares.add(i,j)
                self.own_square_mask[i,j] = 1
                self.obstacle_distances[i,j] = 0 # never play on own
            else:
                if self.grid[i,j] not in self.opponent_squares:
                    self.opponent_squares[self.grid[i,j]] = Cluster()
                cluster = self.opponent_squares[self.grid[i,j]]
                cluster.add(i,j)
                comp_size = len(cluster.component_map[(i,j)].squares)
                if comp_size >= min(10, max(cluster.total / 2, 4)):
                    self.avoid_square(i, j)
        self.last_grid = self.grid
            
    def debug(self):
        print("⏸️ Debugging MannyBot.__call__()")
        import debugpy
        pygame.image.save(pygame.display.get_surface(), "debug_frame.png")
        # Save obstacle_distances
        plt.imshow(self.obstacle_distances.T, origin='upper', cmap='viridis')
        plt.colorbar(label='Distance')  # adds a legend for the color scale
        plt.title("Obstacle Distances")
        # Save to file
        plt.savefig("obstacle_distances.png", dpi=150)
        plt.close()

        # Save scores
        plt.imshow(self.scores.T, origin='upper', cmap='viridis',vmin=-2, vmax=np.max(self.scores))
                # --- Find max score locations ---
        max_val = np.max(self.scores)
        max_coords = np.argwhere(self.scores.T == max_val)

        # --- Plot red dots on those cells ---
        for (i, j) in max_coords:
            plt.plot(j, i, 'ro', markersize=2)  # note: (x, y) = (col, row)
        plt.colorbar(label='Score')  # adds a legend for the color scale
        plt.title("Scores")

        # Save to file
        plt.savefig("scores.png", dpi=150)
        plt.close()        
        debugpy.breakpoint()
        self.pause_next = False  # Reset

    def avoid_square(self, i, j):
        dists = self.distance_table[
            self.grid_size - 1 - i: 2*self.grid_size - 1 - i,
            self.grid_size - 1 - j: 2*self.grid_size - 1 - j
        ]
        self.obstacle_distances = np.minimum(self.obstacle_distances, dists)

    def __call__(self, grid, p):
        # start = time.time()
        # self.replay.append(np.array(grid))
        # if self.num_turns % 10 == 0:
        #     with open('data/manny_replay.pkl', "wb") as f:
        #         pickle.dump(self.replay, f)

        if getattr(self, "pause_next", False):
            self.debug()
        self.num_turns += 1
        self.p = p
        self.grid = np.array(grid)
        self.update()
        # print(self.opponent_squares)
        # print(self.own_squares)

        ### need to add logic to never recapture to avoid fights
        ## squash isolated enemies
        if self.num_turns < 15: # limit how long this goes on for
            for opp, cluster in self.opponent_squares.items():
                for c in cluster.components:
                    if len(c.squares) == 1:
                        i, j = next(iter(c.squares))
                        if self.empty_neighbors[i,j] >= 8 and (i,j) not in self.lost_squares:
                            print(f'Took {i,j} from {self.grid[i,j]}')
                            return i,j



        ### currently copying Phil Code
        # Convert grid to numpy array if it's not already
        grid_arr = np.array(grid)
        grid_size = len(grid_arr)
    
        # Create binary masks
        opponent_mask = ((grid_arr != p) & (grid_arr != 0)).astype(float)
        player_mask = (grid_arr == p).astype(float)
        empty_mask = (grid_arr == 0).astype(float)
        non_player_mask = (grid_arr != p).astype(float)


        # Kernel to count neighbors
        neighbor_kernel = np.ones((3, 3))
        neighbor_kernel[1, 1] = 0  # Don't count the cell itself
        # neighbor_kernel[1,1] = -0.1 # tried negative values but grew worse

        if np.sum(empty_mask) > 10:
            # Count player neighbors for each cell
            player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same') * empty_mask
            squares_that_fill = (player_neighbors >= 4) # set score to 0 on squares that will already fill or can fill from the side
            player_neighbors *= (player_neighbors < 5).astype(float)
            bonus = 5 ** player_neighbors # explore changing bonus
            scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same')
            scores *= (squares_that_fill == 0)
            scores += 0.3
            scores *= non_player_mask
            scores += 0.2
            scores = np.log2(scores)
            self.scores = scores.copy()

        ## np.power(0.2) -> made jump, grew at 2.8
        ## 0.2 -> jump, 2.76
        ## 0.05 -> no jump, 3.06 x2
        ## 0.05*3 -> still 3.06
        ## 0.05 *10 -> down to 2.93, jumped
        ## 0.05 * 5 -> at 3.11
        ## growth rate mostly at 3, able to hop around
        ## grows at 2.5 with pranav there
            scores += self.obstacle_distances * 5 * np.random.power(0.05)

        else:
        # Count player neighbors for each cell
            player_neighbors = sgnl.convolve2d(player_mask, neighbor_kernel, mode='same')
            bonus = 3 ** player_neighbors
            opp_neighbors = sgnl.convolve2d(opponent_mask, neighbor_kernel, mode='same')
            scores = sgnl.convolve2d(bonus, neighbor_kernel, mode='same') * (player_mask == 0) * (opp_neighbors < 7) * (player_neighbors < 7)
            self.scores = scores.copy()
        
        # scores -= 100 * player_mask # def never play on own square
        # for (i,j) in self.lost_squares:
        #     scores[i,j] -= 100
        print(f"have {self.own_squares.total} growing at {self.own_squares.total / self.num_turns} per turn")
        
        i,j = np.unravel_index(np.argmax(scores), scores.shape)

        ### early and midgame look great, next just need to get endgame working
        if self.grid[i,j] == p:
            print('oops played on own square')
        # print(f'Ran in {time.time() - start}')
        return i,j


    def __str__(self):
        return "Mindful Manny"

    def _color4game(self):
        # bad function name so not to be accidentally mess with an exisiting variable/function
        return (255, 36, 178)

# import old_brute_force

# class Barry:

#     def __init__(self, grid_size = 64):
#         self.pause_next = False  # Flag to control debug pause
#         self.grid_size = grid_size
#         ## empty_squares currently not of type Cluster
#         self.empty_squares = set((i,j) for i in range(grid_size) for j in range(grid_size))
#         self.opponent_squares = {} # dict mapping opponent ID to a Cluster
#         self.own_squares = Cluster()
#         self.own_square_mask = np.zeros((grid_size, grid_size))
#         self.last_grid = np.zeros((grid_size, grid_size))
#         ## create numpy array counting how many empty neighboring cells there are
#         self.empty_neighbors = 8* np.ones((grid_size, grid_size))
#         for side_index in [(0, slice(None)), (-1, slice(None)), (slice(None), 0), (slice(None),-1)]:
#             self.empty_neighbors[side_index] = 5
#         for corner_index in [(0,0),(-1,0),(0,-1),(-1,-1)]:
#             self.empty_neighbors[corner_index] = 3
        
#         ## create numpy array counting distance to walls or clusterss
#         self.obstacle_distances = np.ones((grid_size, grid_size))
#         for i in range(1, grid_size // 2 + 1):
#             self.obstacle_distances[i:-i, i:-i] += 1
#         self.obstacle_distances *= 1.2 ## constant for edge distances
#         self.lost_squares = set() # indices of squares that have been recaptured
#         ## build distance table, currently L2 distances
#         self.distance_table = np.zeros((2 * grid_size - 1, 2* grid_size - 1))
#         for i in range(2 * grid_size - 1):
#             for j in range(2 * grid_size - 1):
#                 self.distance_table[i,j] = ((i - (grid_size - 1))**2 + (j - (grid_size - 1))**2)**0.5

#         self.num_turns = 0

#     def update(self):
#         """check updates from last grid"""
#         dif = np.where(self.grid != self.last_grid)
#         if len(dif) == 0:
#             return
#         for (i, j) in zip(dif[0], dif[1]):
#             ## remove info from cell that went away
#             if self.last_grid[i,j] == 0:
#                 self.empty_squares.remove((i,j))
#                 self.empty_neighbors[max(i-1,0):i+2,max(j-1,0):j+2] -= 1
#                 self.empty_neighbors[i,j] += 1
#             elif self.last_grid[i,j] == self.p:
#                 self.own_squares.remove(i,j)
#                 self.own_square_mask[i,j] = 0
#                 self.lost_squares.add((i,j))
#             else:
#                 self.opponent_squares[self.last_grid[i,j]].remove(i,j)
#             ## add info for cell that appeared
#             if self.grid[i,j] == 0:
#                 print(f'ERROR: cell {i,j} became empty')
#             elif self.grid[i,j] == self.p:
#                 self.own_squares.add(i,j)
#                 self.own_square_mask[i,j] = 1
#                 self.obstacle_distances[i,j] = 0 # never play on own
#             else:
#                 if self.grid[i,j] not in self.opponent_squares:
#                     self.opponent_squares[self.grid[i,j]] = Cluster()
#                 cluster = self.opponent_squares[self.grid[i,j]]
#                 cluster.add(i,j)
#                 comp_size = len(cluster.component_map[(i,j)].squares)
#                 if comp_size >= min(10, max(cluster.total / 2, 4)):
#                     self.avoid_square(i, j)
#         self.last_grid = self.grid
            
#     def debug(self):
#         print("⏸️ Debugging MannyBot.__call__()")
#         import debugpy
#         pygame.image.save(pygame.display.get_surface(), "debug_frame.png")
#         # Save obstacle_distances
#         plt.imshow(self.obstacle_distances.T, origin='upper', cmap='viridis')
#         plt.colorbar(label='Distance')  # adds a legend for the color scale
#         plt.title("Obstacle Distances")
#         # Save to file
#         plt.savefig("obstacle_distances.png", dpi=150)
#         plt.close()

#         # Save scores
#         plt.imshow(self.scores.T, origin='upper', cmap='viridis',vmin=-2, vmax=np.max(self.scores))
#                 # --- Find max score locations ---
#         max_val = np.max(self.scores)
#         max_coords = np.argwhere(self.scores.T == max_val)

#         # --- Plot red dots on those cells ---
#         for (i, j) in max_coords:
#             plt.plot(j, i, 'ro', markersize=2)  # note: (x, y) = (col, row)
#         plt.colorbar(label='Score')  # adds a legend for the color scale
#         plt.title("Scores")

#         # Save to file
#         plt.savefig("scores.png", dpi=150)
#         plt.close()        
#         debugpy.breakpoint()
#         self.pause_next = False  # Reset

#     def avoid_square(self, i, j):
#         dists = self.distance_table[
#             self.grid_size - 1 - i: 2*self.grid_size - 1 - i,
#             self.grid_size - 1 - j: 2*self.grid_size - 1 - j
#         ]
#         self.obstacle_distances = np.minimum(self.obstacle_distances, dists)


#     def grid_around(self, i, j, g):
#         """
#         Return:
#         subgrid: a g x g sub-grid centered around (i, j) (clamped to edges)
#         top, left: the offsets in the global grid for subgrid[0,0].
#         """
#         half = g // 2
        
#         # First pass at top-left
#         top = i - half
#         left = j - half

#         # Clamp so top, left >= 0
#         top = max(top, 0)
#         left = max(left, 0)
#         # Also clamp so top+g <= self.n
#         top = min(top, self.grid_size - g)
#         left = min(left, self.grid_size - g)

#         subgrid = self.grid[top:top+g, left:left+g]
        
#         # Convert subgrid to {0,1,2} if needed...
#         converted = np.zeros((g, g), dtype=np.uint8)
#         converted[subgrid == self.p] = 1
#         converted[(subgrid != 0) & (subgrid != self.p)] = 2

#         return converted, top, left


#     def __call__(self, grid, p):
#         if getattr(self, "pause_next", False):
#             self.debug()
#         self.num_turns += 1
#         self.p = p
#         self.grid = np.array(grid)
#         self.update()


#         ### need to add logic to never recapture to avoid fights
#         ## squash isolated enemies
#         if self.num_turns < 15: # limit how long this goes on for
#             for opp, cluster in self.opponent_squares.items():
#                 for c in cluster.components:
#                     if len(c.squares) == 1:
#                         i, j = next(iter(c.squares))
#                         if self.empty_neighbors[i,j] >= 8 and (i,j) not in self.lost_squares:
#                             print(f'Took {i,j} from {self.grid[i,j]}')
#                             return i,j


#         i, j = np.unravel_index(np.argmax(self.obstacle_distances),
#                                 self.obstacle_distances.shape)
#         subgrid, top, left = self.grid_around(i, j, old_brute_force.subgrid_size)
#         best_moves = old_brute_force.score(subgrid)[1]  # local coords in subgrid
#         print(f'Have currently stored {len(old_brute_force.memo)} positions')

#         if not best_moves:
#             # Handle no-move case
#             return # or pick something random

#         # Let’s say we pick the first best move
#         li, lj = best_moves[0]

#         # Convert local subgrid coords (li, lj) → global coords (gi, gj)
#         gi = top + li
#         gj = left + lj

#         assert self.grid[i,j] != p
#         print(f"have {self.own_squares.total} growing at {self.own_squares.total / self.num_turns} per turn")
#         return gi, gj


#     def __str__(self):
#         return "Brute Force Barry"

#     def _color4game(self):
#         # bad function name so not to be accidentally mess with an exisiting variable/function
#         return (70, 100, 130)
class EricAis:

    Lance = name("Lonely Lance", (250, 100, 50))(lonely_lance)
    manny = name("Manny", (32, 41, 92))(Manny())
    phil = name("Fast Filling Phil", (35, 99, 35))(Phil())

    # Raja = name("Random Raja", (250, 100, 50))(random_raja)
    # Rishi = name("Row by Row Rishi", (100, 250, 50))(row_by_row_rishi)
    # Rishi2 = name("Row by Row Rishi2", (100, 200, 100))(row_by_row_rishi2)
    # Rishi3 = name("Row by Row Rishi3", (50, 250, 100))(row_by_row_rishi3)
    # Rishi4 = name("Row by Row Rishi4", (50, 150, 0))(row_by_row_rishi4)
    # Gukesh = name("Growing Gukesh", (100, 50, 250))(growing_gukesh)
    # Gukesh2 = name("Growing Gukesh2", (0, 50, 250))(growing_gukesh)
    # Gukesh3 = name("Growing Gukesh3", (100, 50, 0))(growing_gukesh)
    # Pranav = name("Perimeter Pranav", (10, 150, 250))(perimeter_pranav)