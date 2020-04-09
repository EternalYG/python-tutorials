#coding=utf-8
#重写object类的__str__()方法与__eq__()方法实例

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        template = 'Person [name={0}, age={1}]'
        s = template.format(self.name, self.age)
        return s

    def __eq__(self, other):
        if self.name == other.name and self.age == other.age:
            return True
        else:
            return False

person = Person('Tony', 18)
print(person)

p1 = Person('Tom', 18)
p2 = Person('Tom', 20)

print(p1 == p2)
