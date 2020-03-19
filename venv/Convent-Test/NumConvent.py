#coding=utf-8
TempStr = input()
table = ''.maketrans("0123456789","零一二三四五六七八九")
print(TempStr.translate(table))
