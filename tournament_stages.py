"""
Helper file for tournament related code
"""
from helpers import *
from all_bots import *
def split_inds(n, times=1):
    ans = []
    for _ in range(4*times):
        l = list(range(n))
        random.shuffle(l)
        while len(ans) and len(set(ans[-2:] + l[:2])) != 4:
            random.shuffle(l)
        ans.extend(l)
    return [ans[4*j:4*(j+1)] for j in range(n*times)]
    
def all_ind_pairs(amt):
    return list(itertools.combinations(range(amt), 4))

def disp_scoreboard_s1(cnt, scores, games_played):
    scores_all = [(scores[i], games_played[i], BOT_NAMES[i]) for i in range(len(ALL_BOTS))]
    scores_all.sort(reverse=1)
    print("\x1bc", end="")
    print(f"{'Bot Name:':<40}", "|", f"{'Avg Score':<15}", "|", f"Games Played")
    for a, c, b in scores_all:
        print(f"{b:<40}", "|", f"{round(a, 5):<15}", "|", f"{c:<15}")
    print(cnt)

def get_scores_s1():
    with open("outputs.txt", "r") as f:
        d = f.read().split("\n")
    scores = [[] for _ in range(len(ALL_BOTS))]
    for x in d:
        if len(x.strip()) == 0:
            #empty line
            continue
        a, b = map(float, x.split())
        # print(a, b)
        scores[int(a)].append(b)
    # print(scores)
    games_played = [len(x) for x in scores]
    scores = [(0 if len(j) == 0 else np.mean(j)) for i, j in enumerate(scores)]
    return scores, games_played
    # scores.sort(reverse=1)

def create_games(file="1.sh", amt=2):
    inds = split_inds(len(ALL_BOTS), amt)
    with open(file, "w") as f:
        for nds in inds:
            print("python3.10 single_game.py", " ".join(map(str, nds)), "&", file=f)
    return 4*len(inds)
