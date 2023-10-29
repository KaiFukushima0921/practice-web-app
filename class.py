class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self,x,y):
        self.x += x
        self.y += y
    
    def show_coordinate(self):
        print(self.x, self.y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)
    
cood = Coordinate()
cood.x = 100
cood.y = 200
cood.move(100,200)
cood.show_coordinate()


# print(cood)