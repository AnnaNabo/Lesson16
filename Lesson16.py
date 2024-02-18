#1
class Kassa(object):
    summVkasse = 0
    def __init__(self, summ):
        self.summVkasse = summ
        
    def top_up(self, X):
        self.summVkasse = self.summVkasse + X
    
    def count_1000(self):
        kt = self.summVkasse//1000
        return(kt)
    
    def take_away(self, X):
        if self.summVkasse < X:
            print("summa v kasse menshe zaproshennoy")
        else:
            (self.summVkasse)-=X
            
            
  
Kassa1 = Kassa(100)
Kassa1.top_up(1200)
print(Kassa1.summVkasse)
print(Kassa1.count_1000())
Kassa1.take_away(200)
print(Kassa1.summVkasse)

#2
class Cherepashka(object):
    x = 0
    y = 0
    s = 1
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s
        
    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s <= 0:
            print('s = 0')
            return
        self.s -= 1

    def count_moves(self, x2, y2):
        return abs(self.x -x2) + abs(self.y - y2)
 
cherep = Cherepashka(15,4,1)
cherep.go_up()
print(cherep.x,cherep.y)
print(cherep.count_moves(16,10))