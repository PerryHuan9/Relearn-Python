import math

# 内置函数
# python提供了很多内置函数

# pow求幂 abs取绝对值 round将浮点数转化为最接近的整数（四舍五入）

a = abs(-10)  # 10
b = pow(2, 2)  # 4
b1 = pow(2, 2, 5)  # 4返回2的二次方对5进行取余的结果  结果为4
c = round(1.5)  # 2
c1 = round(3 / 2)  # 2

d = round(3.5)  # 4
e = round(3.6)  # 4
f = round(-3.5)  # -4
g = round(-3.6)  # -4

print(a, b, c, c1)
print(d, e, f, g)

# 向下取整可用floor
h = math.floor(1.8)
i = int(1.9)  # 1
print(h, i)  # 1

# ceil与floor相反，向上取整
j = math.ceil(1.1)  # 2
k = math.ceil(1.9)  # 2
print(j, k)

from math import sqrt  # 导入math模块中的sqrt函数

# sqrt函数的作用是求平法根
a1 = sqrt(9)  # 3.0
print('9的平方根为：', a1)
# b1 = sqrt(-1) 报错，有些平台计算的值为nan,意为not a number
