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
