#coding=utf-8
#鸭子类型实例，python语言不做类型检查，一方面可以充分发挥python动态语言的特点，
#另一方面也给软件设计者带来了困难，对程序员的要求非常高

class Animal(object):
    def run(self):
        print('动物跑...')

class Dog(Animal):
    def run(self):
        print('狗狗跑...')

class Car:
    def run(self):
        print('汽车跑...')

def go(animal):
    animal.run()

go(Animal())
go(Dog())
go(Car())
