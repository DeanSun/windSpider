# 输出 9*9 乘法口诀表
for i in range(1, 10):
    str = ""
    for j in range(1, i + 1):
        str += "{a}*{b}={c} ".format(a=j, b=i, c=(i * j))
    print(str)

# 优化输出
for i in range(1, 10):
    str = ""
    for j in range(1, i + 1):
        str += f'{j}*{i}={j * i} '
    print(str)
