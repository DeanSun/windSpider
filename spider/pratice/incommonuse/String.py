# 1. 使用占位符 方式输出
# %s 表示字符串
# %d 表示整数
# %f 表示小数(默认保留小数后6位, %.2f 保留两位小数)
# 存在格式化标志时，需要使用 %% 表示一个百分号
name = "xiaoming"
age = 12
print("1. 使用占位符 方式输出")
print("My name is %s, My age is %d" % (name, age))

# 2. format格式化
print("2. format格式化")
print("My name is {}, My age is {}".format(name, age))
print("My name is {0}, My age is {1}".format(name, age))
print("My name is {name}, My age is {age}".format(name=name, age=age))

# 2.1 format 进阶
# 2.1.1 填充补齐
# *<20: 左对齐， 总共20个字符， 不够的用*号填充
print('{0:*<20}'.format('hello'))
# *>20: 右对齐， 总共20个字符， 不够的用*号填充
print('{0:*>20}'.format('python'))
# *^20: 居中显示， 总共20个字符， 不够的用*号填充
print('{0:*^21}'.format('what'))

# 2.1.2 位数与进制转换
# 保留2为有效数字
print('{:.2f}'.format(1.13444))
# 转成二进制
print('{0:b}'.format(16))
# 转成八进制
print('{0:o}'.format(10))
# 转成十六进制
print('{0:x}'.format(15))
# 既有填充对齐，又有位数保留
print('{0:*<6.2f}'.format(3.1415926))

# 3. f-string格式化
# {}中直接使用变量
print(f'My name is {name}, My age is {age}')
# {}中运行表达式
print(f'{1 + 2 + 3}')
# 调用python内置函数
print(f'{name.upper()}')
# 用lambda匿名函数：可以做复杂的数值计算
fun = lambda x: x + 1
print(f'{fun(age)}')
