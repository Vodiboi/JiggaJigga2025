# from helpers import *

# def lionel0down(grid, p):
#     ln = len(grid) - 1
#     for j in range(ln, -1, -1):
#         for i in range(ln + 1):
#             square = grid[i][j]
#             if j == ln or j == 0:
#                 if square != p:
#                     neighbors = 0
#                     for neighbor in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
#                         try:
#                             neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
#                         except:
#                             pass
#                     if (neighbors < 7 and square != 0) or neighbors < 5 or j == 0:
#                         return i, j
#             else:
#                 if i % 4 == 0 or i == ln:
#                     if square != p:
#                         neighbors = 0
#                         for neighbor in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
#                             try:
#                                 neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
#                             except:
#                                 pass
#                         if (neighbors < 7 and square != 0) or i == 0 or neighbors < 5:
#                             return i, j
#                 if square not in [0, p]:
#                     neighbors = 0
#                     for neighbor in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
#                         try:
#                             neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
#                         except:
#                             pass
#                     if neighbors < 7:
#                         if i % 2 == 0:
#                             return i, j
#                         elif i % 2 == 1:
#                             for neighbor in [[-1, -1], [-1, 0], [1, -1], [1, 0]]:
#                                 try:
#                                     if grid[i + neighbor[0]][j + neighbor[1]] != p and (i + neighbor[0]) % 4 == 2:
#                                         return i + neighbor[0], j + neighbor[1]
#                                 except:
#                                     pass
#     return random.randint(0, ln), random.randint(0, ln)

# def lionel1down(grid, p):
#     ln = len(grid) - 1
#     for j in range(ln, -1, -1):
#         for i in range(ln + 1):
#             square = grid[i][j]
#             if square != p:
#                 if j == ln:
#                     return i, j
#                 elif i % 2 == 0:
#                     return i, j
#                 elif square != 0:
#                     return i, j
#     return random.randint(0, ln), random.randint(0, ln)

# def lionel1up(grid, p):
#     ln = len(grid) - 1
#     for j in range(ln + 1):
#         for i in range(ln + 1):
#             square = grid[i][j]
#             if square != p:
#                 if j == 0:
#                     return i, j
#                 elif i % 2 == 0:
#                     return i, j
#                 elif square != 0:
#                     return i, j
#     return random.randint(0, ln), random.randint(0, ln)

# # def lionel2(grid, p):
# #     ln = len(grid) - 1
# #     fill_moves = []
# #     adjacent_moves = []
# #     any_moves = []
# #     for j in range(ln + 1):
# #         for i in range(ln + 1):
# #             square = grid[i][j]
# #             if square ==
# #             is_neighbor = False
# #             for neighbor in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
# #                 try:
# #                     if grid[i + neighbor[0]][j + neighbor[1]] == p:


# def lionel2(grid, p):
#     ln = len(grid) - 1
#     fill_moves = []
#     clear_moves = []
#     any_moves = []
#     for j in range(ln + 1):
#         for i in range(ln + 1):
#             square = grid[i][j]
#             if square != p:
#                 is_neighbor = False
#                 for neighbor in [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]:
#                     try:
#                         if grid[i + neighbor[0]][j + neighbor[1]] == p:
#                             is_neighbor = True
#                             any_moves.append((i, j))
#                             break
#                     except:
#                         pass
#                 if is_neighbor and square == 0:
#                     clear_moves.append((i, j))
#     if fill_moves != []:
#         return random.choice(fill_moves)
#     elif clear_moves != []:
#         return random.choice(clear_moves)
#     elif any_moves != []:
#         return random.choice(any_moves)
#     else:
#         return random.randint(0, ln), random.randint(0, ln)

# class LionelAis:
#     Lionel0down = name("Lionel0Down", (255, 255, 0))(lionel0down)
#     Lionel1down = name("Lionel1Down", (255, 255, 0))(lionel1down)
#     Lionel1up = name("Lionel1Up", (255, 255, 0))(lionel1up)
#     Lionel2 = name("Lionel2", (255, 255, 0))(lionel2)
#     # add your bot here using the format: MyBot = name("My Bot", (bot color rgb))(my_bot_function)
#     # then, you can use SampleAis.MyBot in main.py 


# # from helpers import *
# # from statistics import mode
# # from time import time

# # surrounders = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

# # extra_surrounders = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1], [2, 0], [-2, 0], [0, 2], [0, -2], [2, 1], [-2, -1], [-2, 1], [2, -1], [1, 2], [-1, -2], [1, -2], [-1, 2], [2, 2], [-2, -2], [2, -2], [-2, 2]]

# # def simulate(grid, ln0, ln1):
# #     new_grid = grid + []
# #     for i in range(ln0):
# #         for j in range(ln1):
# #             neighbors = {}
# #             for neighbor in surrounders:
# #                 i0 = i + neighbor[0]
# #                 j0 = j + neighbor[1]
# #                 if -1 < i0 < ln0 and -1 < j0 < ln1:
# #                     square = grid[i0][j0]
# #                     if square in neighbors:
# #                         neighbors[square] += 1
# #                     else:
# #                         neighbors[square] = 1
# #             max_value = max(neighbors.values())
# #             if grid[i][j] == 0:
# #                 if max_value > 4:
# #                     for item in neighbors:
# #                         if neighbors[item] == max_value:
# #                             new_grid[i][j] = item
# #                             break
# #             else:
# #                 if max_value > 6:
# #                     for item in neighbors:
# #                         if neighbors[item] == max_value:
# #                             new_grid[i][j] = item
# #                             break
# #     return new_grid


# # class lionel0:
# #     def __init__(self):
# #         self.round = 0
# #         self.bad = []
# #         self.prev = None
# #     def __call__(self, grid, p):
# #         ln = len(grid) - 1
# #         for j in range(ln + 1):
# #             for i in range(ln + 1):
# #                 square = grid[i][j]
# #                 if j == ln or j == 0:
# #                     if square != p:
# #                         neighbors = 0
# #                         for neighbor in surrounders:
# #                             try:
# #                                 neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
# #                             except:
# #                                 pass
# #                         if (neighbors < 7 and square != 0) or neighbors < 5 or j == 0:
# #                             choice = (i, j)
# #                             if choice not in self.bad:
# #                                 if choice == self.prev:
# #                                     self.bad.append(choice)
# #                                 else:
# #                                     return choice
# #                 else:
# #                     if i % 4 == 0 or i == ln:
# #                         if square != p:
# #                             neighbors = 0
# #                             for neighbor in surrounders:
# #                                 try:
# #                                     neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
# #                                 except:
# #                                     pass
# #                             if (neighbors < 7 and square != 0) or i == 0 or neighbors < 5:
# #                                 choice = (i, j)
# #                             if choice not in self.bad:
# #                                 if choice == self.prev:
# #                                     self.bad.append(choice)
# #                                 else:
# #                                     return choice
# #                     if square not in [0, p]:
# #                         neighbors = 0
# #                         for neighbor in surrounders:
# #                             try:
# #                                 neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
# #                             except:
# #                                 pass
# #                         if neighbors < 7:
# #                             if i % 2 == 0:
# #                                 choice = (i, j)
# #                                 if choice not in self.bad:
# #                                     if choice == self.prev:
# #                                         self.bad.append(choice)
# #                                 else:
# #                                     return choice
# #                             elif i % 2 == 1:
# #                                 for neighbor in [[-1, -1], [-1, 0], [1, -1], [1, 0]]:
# #                                     try:
# #                                         if grid[i + neighbor[0]][j + neighbor[1]] != p and (i + neighbor[0]) % 4 == 2:
# #                                             choice = (i + neighbor[0], j + neighbor[1])
# #                                             if choice not in self.bad:
# #                                                 if choice == self.prev:
# #                                                     self.bad.append(choice)
# #                                                 else:
# #                                                     return choice
# #                                     except:
# #                                         pass
# #         return random.randint(0, ln), random.randint(0, ln)

# # def lionel0down(grid, p):
# #     ln = len(grid) - 1
# #     for j in range(ln, -1, -1):
# #         for i in range(ln + 1):
# #             square = grid[i][j]
# #             if j == ln or j == 0:
# #                 if square != p:
# #                     neighbors = 0
# #                     for neighbor in surrounders:
# #                         try:
# #                             neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
# #                         except:
# #                             pass
# #                     if (neighbors < 7 and square != 0) or neighbors < 5 or j == 0:
# #                         return i, j
# #             else:
# #                 if i % 4 == 0 or i == ln:
# #                     if square != p:
# #                         neighbors = 0
# #                         for neighbor in surrounders:
# #                             try:
# #                                 neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
# #                             except:
# #                                 pass
# #                         if (neighbors < 7 and square != 0) or i == 0 or neighbors < 5:
# #                             return i, j
# #                 if square not in [0, p]:
# #                     neighbors = 0
# #                     for neighbor in surrounders:
# #                         try:
# #                             neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
# #                         except:
# #                             pass
# #                     if neighbors < 7:
# #                         if i % 2 == 0:
# #                             return i, j
# #                         elif i % 2 == 1:
# #                             for neighbor in [[-1, -1], [-1, 0], [1, -1], [1, 0]]:
# #                                 try:
# #                                     if grid[i + neighbor[0]][j + neighbor[1]] != p and (i + neighbor[0]) % 4 == 2:
# #                                         return i + neighbor[0], j + neighbor[1]
# #                                 except:
# #                                     pass
# #     return random.randint(0, ln), random.randint(0, ln)

# # # def lionel1(grid, p):
# # #     ln = len(grid) - 1
# # #     for j in range(ln + 1):
# # #         for i in range(ln + 1):
# # #             square = grid[i][j]
# # #             if square != p:
# # #                 if j == 0:
# # #                     choice = (i, j)
# # #                     if choice not in self.bad:
# # #                         if choice == self.prev:
# # #                             self.bad.append(choice)
# # #                     else:
# # #                         return choice
# # #                 elif i % 2 == 0:
# # #                     if choice not in self.bad:
# # #                         if choice == self.prev:
# # #                             self.bad.append(choice)
# # #                     else:
# # #                         return choice
# # #                 elif square != 0:
# # #                     if choice not in self.bad:
# # #                         if choice == self.prev:
# # #                             self.bad.append(choice)
# # #                     else:
# # #                         return choice
# # #     return random.randint(0, ln), random.randint(0, ln)

# # def lionel1down(grid, p):
# #     ln = len(grid) - 1
# #     for j in range(ln, -1, -1):
# #         for i in range(ln + 1):
# #             square = grid[i][j]
# #             if square != p:
# #                 if j == ln:
# #                     return i, j
# #                 elif i % 2 == 0:
# #                     return i, j
# #                 elif square != 0:
# #                     return i, j
# #     return random.randint(0, ln), random.randint(0, ln)

# # def lionel2(grid, p):
# #     ln = len(grid) - 1
# #     fill_moves = []
# #     clear_moves = []
# #     any_moves = []
# #     for j in range(ln + 1):
# #         for i in range(ln + 1):
# #             square = grid[i][j]
# #             if square != p:
# #                 is_neighbor = False
# #                 for neighbor in surrounders:
# #                     try:
# #                         if grid[i + neighbor[0]][j + neighbor[1]] == p:
# #                             if -1 < i + neighbor[0] < ln + 1 and -1 < j + neighbor[1] < ln + 1:
# #                                 is_neighbor = True
# #                                 any_moves.append((i, j))
# #                                 break
# #                     except:
# #                         pass
# #                 if is_neighbor and square == 0:
# #                     clear_moves.append((i, j))
# #     if fill_moves != []:
# #         return random.choice(fill_moves)
# #     elif clear_moves != []:
# #         return random.choice(clear_moves)
# #     elif any_moves != []:
# #         return random.choice(any_moves)
# #     else:
# #         return random.randint(0, ln), random.randint(0, ln)

# # class lionel3:
# #     def __init__(self):
# #         self.round = 0
# #         self.bad = []
# #         self.prev = None
# #     def __call__(self, grid, p):
# #         start = time()
# #         end = start + 0.045
# #         self.round += 1
# #         if self.round == 2:
# #             others = []
# #             for i in range(64):
# #                 for j in range(64):
# #                     if grid[i][j] != 0:
# #                         others.append((i, j))
# #             optimal = (0, 0)
# #             optimal_distance = 0
# #             for i in range(64):
# #                 for j in range(64):
# #                     distance = (min([i, j, 63 - i, 63 - j]) / 3) ** 2
# #                     for square in others:
# #                         distance = min(distance, ((i - square[0]) ** 2 + (j - square[1]) ** 2) ** .5)
# #                     if distance > optimal_distance:
# #                         optimal_distance = distance
# #                         optimal = (i, j)
# #             self.prev = optimal
# #             return optimal
# #         elif self.round != 1:
# #             most = 0
# #             best_moves = []
# #             availible = [[(i, j) for i in range(64)] for j in range(64)]
# #             for selection in extra_surrounders:
# #                 s0 = selection[0]
# #                 s1 = selection[1]
# #                 if time() > end:
# #                     for _ in range(5):
# #                         choice = random.choice(best_moves)
# #                         if choice not in self.bad:
# #                             if choice == self.prev:
# #                                 self.bad.append(choice)
# #                             else:
# #                                 return choice
# #                 for row in availible:
# #                     for square in row:
# #                         i = square[0]
# #                         j = square[1]
# #                         i0 = i + s0
# #                         j0 = j + s1
# #                         if -1 < i0 < 64 and -1 < j0 < 64:
# #                             if grid[i0][j0] == p:
# #                                 ilowbound, ihighbound, jlowbound, jhighbound = max(0, i - 4), min(63, i + 4) + 1, min(0, j - 4), max(63, j + 4) + 1
# #                                 sub_grid = [row[ilowbound: ihighbound] for row in grid[jlowbound: jhighbound]]
# #                                 prev = simulate(sub_grid, ihighbound - ilowbound - 1, jhighbound - jlowbound - 1)
# #                                 sub_grid[j - jlowbound][i - ilowbound] = p
# #                                 after = simulate(sub_grid, ihighbound - ilowbound - 1, jhighbound - jlowbound - 1)
# #                                 total = 0
# #                                 for cell in prev:
# #                                     total -= cell == p
# #                                 for cell in after:
# #                                     total += cell == p
# #                                 if total > most:
# #                                     most = total
# #                                     best_moves = [(i, j)]
# #                                 elif total == most:
# #                                     best_moves.append(i, j)
            

# # def lionel4(grid, p):
# #     for i in range(0, 63, 4):
# #         for j in range(63):
# #             if (i + j) % 2 == 0:
# #                 if grid[i][j] == 0:
# #                     return i, j
# #     for i in range(2, 65, 4):
# #         for j in range(63):
# #             if (i + j) % 2 == 0:
# #                 if grid[i][j] == 0:
# #                     return i, j
# #     for i in range(1, 64, 4):
# #         for j in range(63):
# #             if (i + j) % 2 == 0:
# #                 if grid[i][j] == 0:
# #                     return i, j
# #     for i in range(3, 66, 4):
# #         for j in range(63):
# #             if (i + j) % 2 == 0:
# #                 if grid[i][j] == 0:
# #                     return i, j
# #     while True:
# #         choice = (random.randint(0, 63), random.randint(0, 63))
# #         if grid[choice[0]][choice[1]] != p:
# #             return choice

# # class LionelAis:
# #     Lionel0 = name("Lionel0", (255, 255, 0))(lionel0())
# #     # Lionel0down = name("Lionel0Down", (255, 255, 0))(lionel0down)
# #     # Lionel1 = name("Lionel1", (255, 255, 100))(lionel1)
# #     # Lionel1down = name("Lionel1Down", (255, 255, 100))(lionel1down)
# #     Lionel2 = name("Lionel2", (255, 255, 200))(lionel2)
# #     # Lionel3 = name("Lionel3", (0, 255, 0))(lionel3())
# #     # Lionel4 = name("Lionel4", (255, 255, 255))(lionel4)
# #     # add your bot here using the format: MyBot = name("My Bot", (bot color rgb))(my_bot_function)
# #     # then, you can use SampleAis.MyBot in main.py 

# # # print(simulate([[0, 1, 1, 1, 3, 0], [0, 1, 3, 1, 1, 1], [1, 1, 0, 2, 2, 2], [1, 2, 1, 1, 0, 2], [1, 1, 1, 0, 2, 0], [3, 3, 3, 3, 1, 1]], 6))


from helpers import *
from statistics import mode
from time import time

surrounders = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

extra_surrounders = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1], [2, 0], [-2, 0], [0, 2], [0, -2], [2, 1], [-2, -1], [-2, 1], [2, -1], [1, 2], [-1, -2], [1, -2], [-1, 2], [2, 2], [-2, -2], [2, -2], [-2, 2]]

def simulate(grid, ln0, ln1):
    new_grid = grid + []
    for i in range(ln0):
        for j in range(ln1):
            neighbors = {}
            for neighbor in surrounders:
                i0 = i + neighbor[0]
                j0 = j + neighbor[1]
                if -1 < i0 < ln0 and -1 < j0 < ln1:
                    square = grid[i0][j0]
                    if square in neighbors:
                        neighbors[square] += 1
                    else:
                        neighbors[square] = 1
            max_value = max(neighbors.values())
            if grid[i][j] == 0:
                if max_value > 4:
                    for item in neighbors:
                        if neighbors[item] == max_value:
                            new_grid[i][j] = item
                            break
            else:
                if max_value > 6:
                    for item in neighbors:
                        if neighbors[item] == max_value:
                            new_grid[i][j] = item
                            break
    return new_grid


class lionel0:
    def __init__(self):
        self.round = 0
        self.bad = []
        self.prev = []
        self.bot = 0
        self.badcount = 0
    def __call__(self, grid, p):
        if self.bot == 1:
            start = time()
            end = start + 0.04
            self.round += 1
            ln = 63
            clear_moves = []
            any_moves = []
            for j in range(ln + 1):
                for i in range(ln + 1):
                    square = grid[i][j]
                    if square != p:
                        is_neighbor = False
                        for neighbor in surrounders:
                            try:
                                if grid[i + neighbor[0]][j + neighbor[1]] == p:
                                    if -1 < i + neighbor[0] < ln + 1 and -1 < j + neighbor[1] < ln + 1:
                                        is_neighbor = True
                                        any_moves.append((i, j))
                                        break
                            except:
                                pass
                        if is_neighbor and square == 0:
                            clear_moves.append((i, j))
            if clear_moves != []:
                return random.choice(clear_moves)
            valid = []
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j] == p:
                        for y, x in spots_adj((i, j), grid_size=len(grid)):
                            if grid[y][x] != p:
                                valid.append((y, x))
            if len(valid) == 0:
                return random.randint(0, 63), random.randint(0, 63)
            a = random.choice(valid)
            return a
        ln = len(grid) - 1
        for j in range(ln + 1):
            for i in range(ln + 1):
                square = grid[i][j]
                if j == ln or j == 0:
                    if square != p:
                        neighbors = 0
                        for neighbor in surrounders:
                            try:
                                neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
                            except:
                                pass
                        if (neighbors < 7 and square != 0) or neighbors < 5 or j == 0:
                            choice = (i, j)
                            if choice not in self.bad:
                                if choice in self.prev:
                                    self.bad.append(choice)
                                else:
                                    self.prev.append(choice)
                                    if len(self.prev) > 10:
                                        self.prev = [self.prev[i] for i in range(10)]
                                    return choice
                            else:
                                self.badcount += 1
                                if self.badcount > -1:
                                    self.bot = 1
                else:
                    if i % 4 == 0 or i == ln:
                        if square != p:
                            neighbors = 0
                            for neighbor in surrounders:
                                try:
                                    neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
                                except:
                                    pass
                            if (neighbors < 7 and square != 0) or i == 0 or neighbors < 5:
                                choice = (i, j)
                                if choice not in self.bad:
                                    if choice in self.prev:
                                        self.bad.append(choice)
                                    else:
                                        self.prev.append(choice)
                                    if len(self.prev) > 10:
                                        self.prev = [self.prev[i] for i in range(10)]
                                        return choice
                                else:
                                    self.badcount += 1
                                    if self.badcount > -1:
                                        self.bot = 1
                    if square not in [0, p]:
                        neighbors = 0
                        for neighbor in surrounders:
                            try:
                                neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
                            except:
                                pass
                        if neighbors < 7:
                            if i % 2 == 0:
                                choice = (i, j)
                                if choice not in self.bad:
                                    if choice in self.prev:
                                        self.bad.append(choice)
                                    else:
                                        self.prev.append(choice)
                                        if len(self.prev) > 10:
                                            self.prev = [self.prev[i] for i in range(10)]
                                        return choice
                                else:
                                    self.badcount += 1
                                    if self.badcount > -1:
                                        self.bot = 1
                            elif i % 2 == 1:
                                for neighbor in [[-1, -1], [-1, 0], [1, -1], [1, 0]]:
                                    try:
                                        if grid[i + neighbor[0]][j + neighbor[1]] != p and (i + neighbor[0]) % 4 == 2:
                                            choice = (i + neighbor[0], j + neighbor[1])
                                            if choice not in self.bad:
                                                if choice in self.prev:
                                                    self.bad.append(choice)
                                                else:
                                                    self.prev.append(choice)
                                                    if len(self.prev) > 10:
                                                        self.prev = [self.prev[i] for i in range(10)]
                                                    return choice
                                            else:
                                                self.badcount += 1
                                                if self.badcount > -1:
                                                    self.bot = 1
                                    except:
                                        pass
        return random.randint(0, ln), random.randint(0, ln)

class lionel0down:
    def __init__(self):
        self.round = 0
        self.bad = []
        self.prev = []
        self.bot = 0
        self.badcount = 0
    def __call__(self, grid, p):
        if self.bot == 1:
            start = time()
            end = start + 0.04
            self.round += 1
            ln = 63
            clear_moves = []
            any_moves = []
            for j in range(ln + 1):
                for i in range(ln + 1):
                    square = grid[i][j]
                    if square != p:
                        is_neighbor = False
                        for neighbor in surrounders:
                            try:
                                if grid[i + neighbor[0]][j + neighbor[1]] == p:
                                    if -1 < i + neighbor[0] < ln + 1 and -1 < j + neighbor[1] < ln + 1:
                                        is_neighbor = True
                                        any_moves.append((i, j))
                                        break
                            except:
                                pass
                        if is_neighbor and square == 0:
                            clear_moves.append((i, j))
            if clear_moves != []:
                return random.choice(clear_moves)
            valid = []
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j] == p:
                        for y, x in spots_adj((i, j), grid_size=len(grid)):
                            if grid[y][x] != p:
                                valid.append((y, x))
            if len(valid) == 0:
                return random.randint(0, 63), random.randint(0, 63)
            a = random.choice(valid)
            return a
        ln = len(grid) - 1
        for j in range(ln, -1, -1):
            for i in range(ln + 1):
                square = grid[i][j]
                if j == ln or j == 0:
                    if square != p:
                        neighbors = 0
                        for neighbor in surrounders:
                            try:
                                neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
                            except:
                                pass
                        if (neighbors < 7 and square != 0) or neighbors < 5 or j == 0:
                            choice = (i, j)
                            if choice not in self.bad:
                                if choice in self.prev:
                                    self.bad.append(choice)
                                else:
                                    self.prev.append(choice)
                                    if len(self.prev) > 10:
                                        self.prev = [self.prev[i] for i in range(10)]
                                    return choice
                            else:
                                self.badcount += 1
                                if self.badcount > -1:
                                    self.bot = 1
                else:
                    if i % 4 == 0 or i == ln:
                        if square != p:
                            neighbors = 0
                            for neighbor in surrounders:
                                try:
                                    neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
                                except:
                                    pass
                            if (neighbors < 7 and square != 0) or i == 0 or neighbors < 5:
                                choice = (i, j)
                                if choice not in self.bad:
                                    if choice in self.prev:
                                        self.bad.append(choice)
                                    else:
                                        self.prev.append(choice)
                                    if len(self.prev) > 10:
                                        self.prev = [self.prev[i] for i in range(10)]
                                        return choice
                                else:
                                    self.badcount += 1
                                    if self.badcount > -1:
                                        self.bot = 1
                    if square not in [0, p]:
                        neighbors = 0
                        for neighbor in surrounders:
                            try:
                                neighbors += grid[i + neighbor[0]][j + neighbor[1]] == p
                            except:
                                pass
                        if neighbors < 7:
                            if i % 2 == 0:
                                choice = (i, j)
                                if choice not in self.bad:
                                    if choice in self.prev:
                                        self.bad.append(choice)
                                    else:
                                        self.prev.append(choice)
                                        if len(self.prev) > 10:
                                            self.prev = [self.prev[i] for i in range(10)]
                                        return choice
                                else:
                                    self.badcount += 1
                                    if self.badcount > -1:
                                        self.bot = 1
                            elif i % 2 == 1:
                                for neighbor in [[-1, 1], [-1, 0], [1, 1], [1, 0]]:
                                    try:
                                        if grid[i + neighbor[0]][j + neighbor[1]] != p and (i + neighbor[0]) % 4 == 2:
                                            choice = (i + neighbor[0], j + neighbor[1])
                                            if choice not in self.bad:
                                                if choice in self.prev:
                                                    self.bad.append(choice)
                                                else:
                                                    self.prev.append(choice)
                                                    if len(self.prev) > 10:
                                                        self.prev = [self.prev[i] for i in range(10)]
                                                    return choice
                                            else:
                                                self.badcount += 1
                                                if self.badcount > -1:
                                                    self.bot = 1
                                    except:
                                        pass
        return random.randint(0, ln), random.randint(0, ln)

def lionel1(grid, p):
    ln = len(grid) - 1
    for j in range(ln + 1):
        for i in range(ln + 1):
            square = grid[i][j]
            if square != p:
                if j == 0:
                    return i, j
                elif i % 2 == 0:
                    return i, j
                elif square != 0:
                    return i, j
    return random.randint(0, ln), random.randint(0, ln)

def lionel1down(grid, p):
    ln = len(grid) - 1
    for j in range(ln, -1, -1):
        for i in range(ln + 1):
            square = grid[i][j]
            if square != p:
                if j == ln:
                    return i, j
                elif i % 2 == 0:
                    return i, j
                elif square != 0:
                    return i, j
    return random.randint(0, ln), random.randint(0, ln)

def lionel2(grid, p):
    ln = len(grid) - 1
    fill_moves = []
    clear_moves = []
    any_moves = []
    for j in range(ln + 1):
        for i in range(ln + 1):
            square = grid[i][j]
            if square != p:
                is_neighbor = False
                for neighbor in surrounders:
                    try:
                        if grid[i + neighbor[0]][j + neighbor[1]] == p:
                            if -1 < i + neighbor[0] < ln + 1 and -1 < j + neighbor[1] < ln + 1:
                                is_neighbor = True
                                any_moves.append((i, j))
                                break
                    except:
                        pass
                if is_neighbor and square == 0:
                    clear_moves.append((i, j))
    if fill_moves != []:
        return random.choice(fill_moves)
    elif clear_moves != []:
        return random.choice(clear_moves)
    elif any_moves != []:
        return random.choice(any_moves)
    else:
        return random.randint(0, ln), random.randint(0, ln)

class lionel3:
    def __init__(self):
        self.round = 0
        self.bad = []
        self.prev = None
    def __call__(self, grid, p):
        start = time()
        end = start + 0.04
        self.round += 1
        if self.round == 2:
            others = []
            for i in range(64):
                for j in range(64):
                    if grid[i][j] != 0:
                        others.append((i, j))
            optimal = (0, 0)
            optimal_distance = 0
            for i in range(64):
                for j in range(64):
                    distance = (min([i, j, 63 - i, 63 - j]) / 3) ** 2
                    for square in others:
                        distance = min(distance, ((i - square[0]) ** 2 + (j - square[1]) ** 2) ** .5)
                    if distance > optimal_distance:
                        optimal_distance = distance
                        optimal = (i, j)
            self.prev = optimal
            return optimal
        elif self.round != 1:
            most = 0
            best_moves = []
            availible = [[(i, j) for i in range(64)] for j in range(64)]
            for selection in extra_surrounders:
                s0 = selection[0]
                s1 = selection[1]
                if time() > end:
                    open('log.txt', 'a').write(str(best_moves) + ' ')
                    for _ in range(5):
                        choice = random.choice(best_moves)
                        if choice not in self.bad:
                            if choice == self.prev:
                                self.bad.append(choice)
                            else:
                                return choice
                for row in availible:
                    for square in row:
                        i = square[0]
                        j = square[1]
                        i0 = i + s0
                        j0 = j + s1
                        if -1 < i0 < 64 and -1 < j0 < 64:
                            if grid[i0][j0] == p:
                                ilowbound, ihighbound, jlowbound, jhighbound = max(0, i - 4), min(63, i + 4) + 1, max(0, j - 4), min(63, j + 4) + 1
                                sub_grid = [row[ilowbound: ihighbound] for row in grid[jlowbound: jhighbound]]
                                # print(sub_grid, ilowbound, ihighbound, jlowbound, jhighbound)
                                prev = simulate(sub_grid, ihighbound - ilowbound - 1, jhighbound - jlowbound - 1)
                                sub_grid[j - jlowbound][i - ilowbound] = p
                                after = simulate(sub_grid, ihighbound - ilowbound - 1, jhighbound - jlowbound - 1)
                                total = 0
                                for cell in prev:
                                    total -= cell == p
                                for cell in after:
                                    total += cell == p
                                if total > most:
                                    most = total
                                    best_moves = [(i, j)]
                                elif total == most:
                                    best_moves.append((i, j))

class lionel:
    def __init__(self):
        self.round = 0
        self.bad = []
        self.prev = None
    def __call__(self, grid, p):
        start = time()
        end = start + 0.04
        self.round += 1
        if self.round == 2:
            others = []
            for i in range(64):
                for j in range(64):
                    if grid[i][j] != 0:
                        others.append((i, j))
            optimal = (0, 0)
            optimal_distance = 0
            for i in range(64):
                for j in range(64):
                    distance = (min([i, j, 63 - i, 63 - j]) / 3) ** 2
                    for square in others:
                        distance = min(distance, ((i - square[0]) ** 2 + (j - square[1]) ** 2) ** .5)
                    if distance > optimal_distance:
                        optimal_distance = distance
                        optimal = (i, j)
            self.prev = optimal
            return optimal
        elif self.round != 1:
            ln = 63
            clear_moves = []
            any_moves = []
            for j in range(ln + 1):
                for i in range(ln + 1):
                    square = grid[i][j]
                    if square != p:
                        is_neighbor = False
                        for neighbor in surrounders:
                            try:
                                if grid[i + neighbor[0]][j + neighbor[1]] == p:
                                    if -1 < i + neighbor[0] < ln + 1 and -1 < j + neighbor[1] < ln + 1:
                                        is_neighbor = True
                                        any_moves.append((i, j))
                                        break
                            except:
                                pass
                        if is_neighbor and square == 0:
                            clear_moves.append((i, j))
            if clear_moves != []:
                return random.choice(clear_moves)
            valid = []
            for i in range(len(grid)):
                for j in range(len(grid)):
                    if grid[i][j] == p:
                        for y, x in spots_adj((i, j), grid_size=len(grid)):
                            if grid[y][x] != p:
                                valid.append((y, x))
            if len(valid) == 0:
                return random.randint(0, 63), random.randint(0, 63)
            a = random.choice(valid)
            return a

def lionel4(grid, p):
    for i in range(0, 63, 4):
        for j in range(63):
            if (i + j) % 2 == 0:
                if grid[i][j] == 0:
                    return i, j
    for i in range(2, 65, 4):
        for j in range(63):
            if (i + j) % 2 == 0:
                if grid[i][j] == 0:
                    return i, j
    for i in range(1, 64, 4):
        for j in range(63):
            if (i + j) % 2 == 0:
                if grid[i][j] == 0:
                    return i, j
    for i in range(3, 66, 4):
        for j in range(63):
            if (i + j) % 2 == 0:
                if grid[i][j] == 0:
                    return i, j
    while True:
        choice = (random.randint(0, 63), random.randint(0, 63))
        if grid[choice[0]][choice[1]] != p:
            return choice

def test(grid, p):
    # for i in range(10, 53):
    #     for j in range(10, 53):
    #         if grid[i][j] != p:
    #             return i, j
    return 0, 0
class LionelAis:
    GrassUp = name("GrassUp", (255, 235, 0))(lionel0())
    GrassDown = name("GrassDown", (235, 255, 0))(lionel0down())
    # Lionel1 = name("Lionel1", (255, 255, 100))(lionel1)
    # Lionel1down = name("Lionel1Down", (255, 255, 100))(lionel1down)
    # Lionel2 = name("Lionel2", (255, 255, 200))(lionel2)
    # Lionel3 = name("Lionel3", (0, 255, 0))(lionel3())
    Lionel5 = name("Lionel5", (255, 255, 0))(lionel())
    # Lionel4 = name("Lionel4", (255, 255, 255))(lionel4)
    # Test = name("Test", (255, 255, 255))(test)
    # add your bot here using the format: MyBot = name("My Bot", (bot color rgb))(my_bot_function)
    # then, you can use SampleAis.MyBot in main.py 

# print(simulate([[0, 1, 1, 1, 3, 0], [0, 1, 3, 1, 1, 1], [1, 1, 0, 2, 2, 2], [1, 2, 1, 1, 0, 2], [1, 1, 1, 0, 2, 0], [3, 3, 3, 3, 1, 1]], 6))