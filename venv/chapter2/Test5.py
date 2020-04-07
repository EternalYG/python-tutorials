#coding=utf-8
#多态与类型检查实例
class Figure:
    def draw(self):
        print('绘制Figure...')

class Ellipse(Figure):
    def draw(self):
        print('绘制Ellipse...')

class Triangle(Figure):
    def draw(self):
        print('绘制Triangle...')

f1 = Figure()
f1.draw()

f2 = Ellipse()
f2.draw()

f3 = Triangle()
f3.draw()

#类型检查
print(isinstance(f1, Triangle))
print(isinstance(f2, Triangle))
print(isinstance(f3, Triangle))
print(isinstance(f2, Figure))

