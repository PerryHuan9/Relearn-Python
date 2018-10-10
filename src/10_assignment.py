# Python的赋值魔法


# 1、序列解包
def test_1():
    '序列解包，对所有的序列都适用，有一个前提，变量数和元素数必须一致'
    x, y, z = 1, 2, 3
    print(x, y, z)
    # 用于交换两个变量的值
    x, y = y, x
    print(x, y, z)
    (a, b, c) = [4, 5, 6]
    print(a, b, c)
    e, f, g = "你好啊"
    print(e, f, g)
    # 字典也可以进行序列解包
    mapping = {'name': 'perry', 'age': 22}
    key, value = mapping.popitem()
    print(key, value)
    # 对于序列元素大于解包变量的情况，可以使用*reset接收多余的变量
    a, b, *r = [1, 2, 3, 4, 5, 6]
    print(a, b, r)
    name = "Albus Percival Wulfric Brian Dumbledore"
    first, *middle, last = name.split()
    print(first, middle, last)


# test_1()


# 2、链式复制
def test_2():
    x = y = len
    # 上式与下面两个表达式等价
    y = len
    x = y
    # 但可能与下式不同
    x = len
    y = len


# test_2()


# 3、增强赋值
def test_3():
    '增强赋值适用于所有的标准运算符'
    x = 0
    x += 5
    x = x + 5


# test_3()
