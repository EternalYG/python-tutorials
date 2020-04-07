#coding=utf-8
#父类子类实例

class Animal(object):
    def __init__(self, age, sex=1, weight=0.0):
        self.age = age
        self.sex = sex
        self.weight = weight

    def eat(self):
        self.weight += 0.05
        print("动物吃...")

class Dog(Animal):
    def eat(self):
        self.weight += 0.1
        print('狗狗吃')
        print(self.weight)

a1 = Dog(2, 0, 10.0)
a1.eat()