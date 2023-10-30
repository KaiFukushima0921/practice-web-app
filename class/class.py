import math

# class Coordinate:
#     def __init__(self):
#         self.x = 0
#         self.y = 0

#     def move(self,x,y):
#         self.x += x
#         self.y += y
    
#     def show_coordinate(self):
#         print(self.x, self.y)

#     def __str__(self):
#         return "({0},{1})".format(self.x, self.y)
    
# cood = Coordinate()
# cood.x = 100
# cood.y = 200
# cood.move(100,200)
# cood.show_coordinate()

# print(cood)




# class Sample:
#     def __init__(self):
#         self.x = 100

# obj = Sample()
# obj.y = 200
# print(obj.y)

# del obj.x
# print(obj.x)




# class Sample: pass

# obj = Sample()
# obj.x = 100
# obj.y = 200
# print(obj.x, obj.y)




# class Coordinate:
#     def __init__(self):
#         self.x = 0
#         self.y = 0

#     def show_coordinate(self):
#         print(self.x, self.y)
        
# cood = Coordinate()
# cood.x = 100
# cood.y = 200
# cood.show_coordinate()

# c = Coordinate
# cood2 = c()
# cood2.x = 300
# cood2.y = 600
# cood2.show_coordinate()



# class Coordinate:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def show_coordinate(self):
#         print(self.x, self.y)

#     @classmethod
#     def create_origin(cls):
#         origin = cls(0,0)
#         return origin
    
# cood = Coordinate.create_origin()
# print(cood.show_coordinate())

# cood2 = cood(10,20)
# cood3 = cood2.create_origin()
# print(cood3.show_coordinate)



class Coordinate:
    def __init__(self):
        self.x = 0
        self.y = 0

    def show_coordinate(self):
        print(self.x, self.y)

    @staticmethod
    def calc_dist(cood1, cood2):
        x = cood1.x - cood2.x
        y = cood1.y - cood2.y
        return math.sqrt((math.pow(x,2) + math.pow(y, 2)))

cood1 = Coordinate()
cood1.x, cood1.y = 100, 100

cood2 = Coordinate()
cood2.x, cood2.y = 200, 200

dist = Coordinate.calc_dist(cood1, cood2)
print(dist)