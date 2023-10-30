# class Base:
#     def func1(self):
#         print('func1')

# class Sub(Base):
#     def func2(self):
#         print('func2')

# obj = Sub()
# obj.func1()
# obj.func2()




# class User:
#     def __init__(self, name="", age=0):
#         self.name = name
#         self.age = age
    
#     def sey_name(self):
#         print("私の名前は" + self.name + "です。")


# class Employee(User):
#     def __init__(self, name, age, department):
#         super().__init__(name, age)
#         self.department = department

#     def say_department(self):
#         print("私の部署は" + self.department + "です。")

# e = Employee("Suzuki", 45, "営業部")
# e.sey_name()
# e.say_department()



# class Base1:
#     def func1(self):
#         print('func1')

# class Base2:
#     def func2(self):
#         print('func2')

# class Sub(Base1, Base2):
#     def func(self):
#         super().func1()
#         super().func2()

# obj = Sub()
# obj.func()



# class User:

#     def __init__(self, name="", age=0):
#         self.name = name 
#         self._age = age  
 
 
# user = User("Yamada", 45)
# user.name = "Yoshida"
# user._age = 39
# print(user.name,user._age)



# class Sample:
#     def __init__(self):
#         self.__text = "sample"

#     @property
#     def text(self):
#         return "{{0}}".format(self.__text)
    
#     @text.setter
#     def text(self, text):
#         if text is None:
#             self.__text = "None"
#         else:
#             self.__text = text

#     @text.deleter
#     def text(self):
#         pass

# obj = Sample()
# print(obj.text)

# obj.text = None
# print(obj.text)

# del obj.text
# print(obj.text)



# def add_member(cls):
#     cls.x = 'sample'
#     return cls

# class Sample:
#     pass

# NewSampleCls = add_member(Sample)
# obj = NewSampleCls()
# print(obj.x)



# class Coordinate:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __bool__(self):
#         if self.x or self.y:
#             return True
#         else:
#             return False
        
# p0 = Coordinate(0,0)
# p1 = Coordinate(100,200)
# p2 = Coordinate(0, 200)

# if p0:
#     print("点p0は真と評価されました")

# if p1:
#     print("点p1は真と評価されました")    

# if p2:
#     print("点p2は真と評価されました")



# class MyClass:
#     def __new__(cls):
#         print('__new__')
#         print(cls)

#     def __init__(self):
#         print('__init__')

#     def __str__(self):
#         return 'test'
    
# obj = MyClass()
# print(obj)


# class Sample:
#     def __init__(self, val, text):
#         self.val = val
#         self.text = text

#     def __lt__(self, other):
#         return self.val < other.val
    
#     def __le__(self, other):
#         return self.val <= other.val
 
 
#     def __eq__(self, other):
#         return self.val == other.val
 
 
#     def __ne__(self, other):
#         return self.val != other.val
 
 
#     def __gt__(self, other):
#         return self.val > other.val
 
 
#     def __ge__(self, other):
#         return self.val >= other.val
    
# obj1 = Sample(100, 'aaa')
# obj2 = Sample(200, 'aaa')

# print(obj1 < obj2)



class Sample1():
    pass

class Sample2(Sample1):
    pass

obj1 = Sample1()
obj2 = Sample2()

print(type(obj1) == Sample1)
print(type(obj1) == Sample2)
print(type(obj2) == Sample1)
print(type(obj2) == Sample1)
