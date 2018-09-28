# math模块中的函数无法处理复数，python提供了cmath模块处理复数
import cmath

a = cmath.sqrt(-1)  # 1j
print(a)


# __future__模块 保存着Python当前不支持，但未来可能成为标准组成部分的功能
