#coding=utf-8

def calculate_fun(opr):
    def add(a, b):
        return a + b

    def sub(a, b):
         return a - b

    if opr == '+':
         return add
    else:
         return sub

f1 = calculate_fun('+')
f2 = calculate_fun('1')

print(type(f1))

print("10 + 5 = {0}".format(f1(10,5)))
print("10 - 5 = {0}".format(f2(10,5)))
