import math
class rectangle:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        res = self.x*self.x + self.y*self.y
        print(math.sqrt(res))


obj = rectangle(2,3)