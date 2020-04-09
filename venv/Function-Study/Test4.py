#coding=utf-8
from functools import reduce

number_list =range(1, 11)
number_filter = filter(lambda it : it % 2 == 0, number_list)
print(list(number_filter))

users = ['Tony', 'Tom', 'Ben', 'Alex']
users_map = map(lambda u:  u.lower(), users)
print(list(users_map))

a = (1, 2, 3, 4)
a_reduce = reduce(lambda acc, i: acc + i, a)
# a_reduce = reduce(lambda acc, i: acc + i, a, 2)
print(a_reduce)