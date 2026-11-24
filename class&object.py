# class Myclass:
#     x = 9
# p1 = Myclass()
# print(p1.x)
class Person:
    def __init__(self, name , age):
        self.name = name
        self.age = age
p1 = Person('Tim' , 90)
print(p1.name)
print(p1.age)
name = input("Enter your name : ")
age = input("Enter your age : ")
p2 = Person(name , age)
print(p2.name + " " + p2.age)