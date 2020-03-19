#coding=utf-8
#csv数据清洗
'''with open('data.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # 按行进行倒序排列
    lines.reverse()  # 原地转换
    # lines = lines[::-1]  # 利用切片进行倒序

    for line in lines:
        # 用分号(;)代替逗号(,)分割数据，无空格
        line = line.strip('\n')
        # line = line.replace('\n', '')
        line = line.replace(' ', '')
        # 每行数据倒序排列
        t = line.split(',')
        t.reverse()  # 原地倒序
        # t = t[::-1]  # 切片倒序
        # 输出转换后的数据
        print(';'.join(t))'''

#系统信息输出
'''import sys
print("RECLIMIT:{}, EXEPATH:{}, UNICODE:{}".format(sys.getrecursionlimit(), sys.executable, sys.maxunicode))'''

#文本关键行计算
'''with open('latex.log', 'r', encoding='utf-8') as f:
    rows_set = set(f.readlines())
    print('共{}关键行'.format(len(rows_set)))'''


#二维数组输出
from tabulate import tabulate
data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
print(tabulate(data, tablefmt="grid"))


