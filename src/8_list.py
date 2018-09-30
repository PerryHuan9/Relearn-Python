# python序列之列表
# 列表在python中极其有用，是python的主力


# 1、list函数 reversed sorted
# 内置的list函数可以将序列转为列表
def test_1():
    l = list('你好abcld')
    print('liat(你好abcld):', l)
    # 字符串的join方法可将列表转为字符串
    s = ''.join(l)
    print("''.join(l):", s)
    s1 = '*'.join(l)
    print("'*'.join(l):", s1)
    lst = [12, 454, 2, 3434, 451, 1]
    a = reversed(lst)
    print(a)
    b = sorted(lst)
    print(b)


test_1()


# 2、基本的列表操作
# 列表是一种序列，所以自然能够进行索引、切片、相乘和拼接等操作
# 但列表的有趣之处在于它是可以修改的
def test_2():
    # 修改列表 通过索引给特定位置的元素赋值
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print('修改之前：', numbers)
    numbers[1] = 4
    print('修改之后：', numbers)
    # 删除元素 使用del 语句可删除列表中指定元素
    del numbers[0]
    print('删除后的列表：', numbers)
    # 给切片赋值，通过给切片赋值改变列表中指定范围的值,只能赋值给序列
    numbers[3:] = list('123')
    print('给切片赋值之后：', numbers)
    # 还可以在不替换原来元素的情况下插入新元素
    numbers[1:1] = '插入的元素'
    print(numbers)
    numbers[1:4] = []  # 相当与 delete numbers[1:6]
    print(numbers)
    # 步长不为1的切片赋值，使用步长时必须考虑范围、步长还有所赋值的长度相匹配
    numbers[1:6:2] = [1, 2, 88]
    print(numbers)


# test_2()


# 3、列表方法
# python为列表提供了很多方法，一些常用的方法包括
# append、clear、copy,extend、index、insert、pop、remove、reverse和sort
def text_3():
    # (1)append方法用于在列表的末尾追加一个元素
    lst = [1, 2, 3]
    print('append前：', lst)
    lst.append(888)
    print('append后：', lst)
    # (2)clear方法清空列表
    lst.clear()
    print(lst)
    lst = [1, 2, 3, 4]
    print('重建列表：', lst)
    # (3)copy方法复制一个新列表,类似于a[:]或list(a)
    lst2 = lst.copy()
    print('复制生成的新数组：', lst2)
    # (4)count方法计算指定元素在列表中出现的次数
    ls = ['to', 'be', 'or', 'not', 'to', 'be']
    print('新数组:', ls)
    to_count = ls.count('to')
    print('"to"出现的次数：', to_count)  # 2
    # count不会遍历列表中的列表元素存在的值
    x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
    print('x:', x)
    print('x中1的个数：', x.count(1))  # 2
    # (5)extend方法用于将一个列表附加到列表末尾,
    # 其效果与序列的相加相同，但序列的相加会创建一个新序列，所以效率比extend抵
    # 另外给切片赋值也可以实现相同的效果，但可读性不高
    ls.extend([66, 77, 88, 99])
    print(ls)
    ls[len(ls):] = [11, 22, 33]
    print(ls)
    # (6) index方法搜索列表中指定值第一次出现的索引,不存在时报异常
    be_index = ls.index('be')
    print('be第一次出现的index:', be_index)
    # (7)insert方法用于将一个对象插入列表,其也可以使用插片赋值实现
    ls.insert(1, '你好')
    print('在index为1的位置插入：', ls)
    ls[1:1] = ['切片赋值插入']
    print(ls)
    # (8)从列表的末尾删除并返回一个元素,
    f = ls.pop()
    print(ls, f)
    # (9)remove方法用于删除列表中指定值的第一个元素,删除不存在的元素报异常
    ls.remove('be')
    print(ls)
    # (10)reverse方法按相反的顺序排列列表中的元素
    ls.reverse()
    print(ls)
    # (11)sort方法用于对列表进行就地排序，即改变原列表
    ll = [99, 22, 88, 55, 66, 44, 11]
    print('sort前的列表：', ll)
    ll.sort()
    print('sort后的列表：', ll)
    ss = ['adsdfs', 'ab', 'acdssdf']
    ss.sort()
    print(ss)
    # (12)高级排序，sort方法还可以传入两个参数，key和reverse，
    # key设置排序的方式，即根据大小或长度排序,可传入一个方法，reverse设为true则与reverse方法一样
    ss.sort(key=len)  # 根据字符串的长度
    print(ss)
    ss.sort(reverse=True)
    print(ss)
    ss.sort(key=len, reverse=True)
    print(ss)
    print('adsasd', reversed([12, 34, 45]))


# text_3()


# 4、元组:不可修改的序列
# 元组支持序列的所有操作，但不包括更改序列值得操作
def text_4():
    # 创建元组有两种方式
    a = 1, 2, 3
    print(a)
    b = (1, 2, 3)
    print(b)
    c = ()
    print(c)
    # 只有一个元素的元组,左边必须加逗号
    d = 'abc',
    print(d)
    e = (88,)
    print(e)
    # tuple方法将一个列表转换为元组
    f = tuple([23, 44, 55])
    print(f)
    i = list(f)
    print(i)

# text_4()
