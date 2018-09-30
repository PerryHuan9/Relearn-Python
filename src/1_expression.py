# 1、 / // % 三种运算
b = 10 / 3  # 3.3333333
c = 10 // 3  # 3
d = 10 % 3  # 1
e = 10 / -3  # -3.333333

f = 10 // -3  # -4 为向下取整故取小的数 -4小于-3
g = -10 // 3  # -4
h = 10 % -3  # -2
i = -10 % 3  # 2

print(b, c, d)
print(f, g, h, i)

# 2、** 幂运算 可使用pow函数代替 函数也是一个表达式
a1 = 2 ** 3  # 8
b1 = -3 ** 2  # -9
c1 = (-3) ** 2  # 9
d1 = pow(-3, 2)  # 9
print(a1, b1, c1, d1)

# 3、十六进制、八进制和二进制
a2 = 0x0f  # 15
b2 = 0o10  # 8
c2 = 0b11  # 3
print(a2, b2, c2)

# 4、 python支持单引号和双引号包裹字符串
print('你好啊!单引号')
print('你好啊！双引号')
print('"在单引号中使用双引号"')
print("'在双引号中使用单引号'")
# 或者对单引号或者双引号转义
print("\"双引号中使用双引号必须转义\"")
print('\'单引号中使用单引号也必须转义\'')

# 5、str能以合理的方式将值转换为用户能够看懂的字符
# repr通常会获得值的合法Python表达式
print(str('hello\nword'))  # 显示出来的结果会换行,特殊字符编码转换为相应的字符
print(repr('hello\nword'))  # 显示结果不会换行'hello\nword

# 6、长字符串使用''' ''''包裹，在里面的所有特殊字符都不会被转换，而且可自由换行
a3 = '''This is a very long string.It continus here.
And it's not over yet."Hello,world!"Still here.
'''
print(a3)

# 原始字符串 以r开头后面接引号，不会对反斜杠做处理
b3 = r"c:\nowhere"  # 结果为c:\nowhere
c3 = r'let\'s go'  # 结果为let\'s go
print(b3, c3)
d3 = r'This is illegal\\'  # This is illegal\\
print(d3)

# 如果想创建以反斜杆结尾的的子字符串，最好的方法是将反斜杠独立出来
print(r'c:\Program File\foo\bar''\\')
