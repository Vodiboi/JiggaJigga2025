from helpers import *

def test_bot(grid, p):
    return (32,32)

class Expanding_Enterprise:
    def __init__(self):
        self.squares = [[],[],[],[],[],[],[],[],[]]
        self.close = []
        self.count = 0
        
    def __call__(self, grid, p):
        self.squares = [[],[],[],[],[],[],[],[],[]]
        self.close = []
        self.count += 1
        print(self.count)
        if self.count > 20:
            print('break')
        for i in range(2, 62):
            for j in range(2, 62):
                sub_array = [row[j-2:j+3] for row in grid[i-2:i+3]]
                n = self.simulateputplay(sub_array, p)
                self.squares[n].append([i,j])
                    
        for i in range(1, 63):
            for j in range(1, 63):
                if(self.has_neighbors(grid, p, i, j)):
                    self.close.append([i,j])       
        
        
        
        for k in range(8, 0, -1):
            l = len(self.squares[k])
            if(l!=0):
                r = random.randint(0,l-1)
                return self.squares[k][r]
        if(len(self.close)!=0):
            r = random.randint(0, len(self.close)-1)
            return self.close[r]
        
        return [random.randint(0,63),random.randint(0,63)]
    
    def has_neighbors(self, grid, p, a, b):
        s = [row[b-1:b+2] for row in grid[a-1:a+2]]
        for i in range(0,3):
            for j in range(0,3):
                if((i!=1) or (j!=1)):
                    if(s[i][j] == p):
                        return True
        return False

    def simulatesinglesqaure(self, a3by3, p):         
        if(a3by3[1][1] == p):
            return False
        else:
            count = 0
            for i in range(0,3):
                for j in range(0,3):
                    if((i!=1) or (j!=1)):
                        if(a3by3[i][j] == p):
                            count +=1
            if((count>=5) and (a3by3[1][1]==0)):
                return True
            elif(count>=8):
                return True
            else:
                return False       

    def simulateputplay(self, a5by5, p):
        count = 0
        if(a5by5[2][2] == p):
            return 0
        a5by5[2][2] = p
        for i in range(1,4):
            for j in range(1,4):
                if((i!=2) or (j!=2)):
                    s = [[a5by5[i-1][j-1], a5by5[i-1][j], a5by5[i-1][j+1]], 
                        [a5by5[i][j-1], a5by5[i][j], a5by5[i][j+1]], 
                        [a5by5[i+1][j-1], a5by5[i+1][j], a5by5[i+1][j+1]]]
                    if (self.simulatesinglesqaure(s,p) == True):
                        count+=1        
        return count

e = Expanding_Enterprise()
class ElizabethAis:
    ee = name("Expanding_Enterprise", (180,180,200))(e)