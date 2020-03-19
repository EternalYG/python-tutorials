#coding=utf-8
rows = 0
columns = 0
with open('latex.log', 'r', encoding='utf-8') as f:
  for line in f:
    # 判断非空行
    if not len(line) == 1 and line[-1] == '\n':
      rows += 1
      # 去掉最后一个换行符'/n'
      columns += len(line) - 1
print(int(columns / rows + 0.5))
