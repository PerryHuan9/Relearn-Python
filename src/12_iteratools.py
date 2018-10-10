# 除了for in迭代之外，Python还提供了其它一些迭代工具


# 1、并行迭代，同时迭代两个序列
def test_1():
    names = ['anne', 'beth', 'georage', 'damoon']
    ages = [12, 23, 45, 56]
    for index in range(len(names)):
        print("{}'s age is {}.".format(names[index], ages[index]))
    # 还可以通过zip函数缝合两个序列后再迭代,当个缝合的两个序列长度不匹配时，取短的序列
    print(list(zip(names, ages)))  # [('anne', 12), ('beth', 23), ('georage', 45), ('damoon', 56)]
    for name, age in zip(names, ages):
        print(name, 'with age ', age)


# test_1()

# 2、迭代时获取索引
# 使用内置函数enumerate内置函数可将序列包装为字典
def test_2():
    num = [11, 22, 33, 44, 55]
    for index, value in enumerate(num):
        print(index, ':', value)

# test_2()


# 3、后向迭代和排序后迭代










