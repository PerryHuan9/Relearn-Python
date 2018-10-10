# 逻辑控制语句


def test_1():
    # 布尔值True和False是1和0的别名
    print(True == 1, False == 0)
    # 对于False、None、0、""、()、[]、{}这些都会被视为假
    # bool函数可以将其他值转为布尔值
    a = bool(" ")
    print(a)
    # num = input('number:')
    num = 0
    num = int(num)
    if num > 0:
        print(num, '>0')
    elif num < 0:
        print(num, '<0')
    else:
        print(num, '=0')

    a = ()
    if a:
        print('nihao')
    a = [1, 2]
    b = [23, 66, 88]
    # 相同类型才能比较
    if a < b:
        print(a, '>', b)


# test_1()


def test_2():
    'is相同运算符和==相等运算符的区别'
    # 相等运算符只要值相等，比两个序列具有相等的值，结果便为True
    # 而is相同运算符，两个变量必须指向相同的对象才会返回True
    x = y = [1, 2, 3]
    z = [1, 2, 3]
    print(x == y, x == z)  # True,True
    print(x is y, z is y)  # True,False
    a, b = 1, 1
    print(a is b)
    # 字符串之间的比较是根据字母排列顺序进行比较的,实际上是按unicode码点排列的
    print("abc" < 'acb')  # True
    # 字符串是根据顺序值进行排列的，要获取字符的顺序值可使用ord函数
    s = ord('好')
    print(s)
    # chr函数的作用域ord相反，即根据顺序值转为对应字符
    print(chr(12345))
    numer = int(input('number:'))
    if numer < 10 and numer > 0:
        print('Great')
    else:
        print('wrong')

    # 或者使用链式比较
    if 0 < numer < 10:
        print('great')
    else:
        print('wrong2')


# test_2()

def test_3():
    if "1" and [12]:
        print('and是逻辑与')
    if not ():
        print('not 是逻辑非')
    if () or [2]:
        print('or就是逻辑或')

    name = input('name:') or 'unknown'
    print(name)  # 'unknown'

    # 断言assert
    age = -1
    assert 0 < age < 100


# test_3()

import math


def test_4():
    lst = [1, 4, 6, 8, 0, 3, 5]
    for e in lst:
        print(e)
    # range函数
    lst = list(range(0, 8))
    print(lst)
    for n in range(1, 4):
        print(n)
    # 遍历字典,默认遍历键
    d = {'x': 666, 'y': 888}
    for k in d:
        print(k, ':', d[k])
    for key, value in d.items():
        print(key, "=", value)
    # 或者只遍历值
    for value in d.values():
        print(value)

    for n in range(99, 81, -1):
        root = math.sqrt(n)
        if root == int(root):
            print(n)
            break
    # 这句else语句尽在循环正常结束没有调用break才会执行
    else:
        print('Didn\'t find it')


# test_4()


# 4、简单推导
def test_5():
    '列表推导'
    a = [x * x for x in range(0, 10)]
    print(a)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    b = [x * x for x in range(10) if x % 3 == 0]
    print(b)  # [0, 9, 36, 81]
    c = [(x, y) for x in range(3) for y in range(2)]
    print(c)  # [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]
    d = [(x, y) for x in range(4) for y in range(4) if x == y]
    print(d)  # [(0, 0), (1, 1), (2, 2), (3, 3)]

    girls = ['alice', 'bernice', 'clarice']
    boys = ['chris', 'arnold', 'bob']
    letterGirls = {}
    for girl in girls:
        letterGirls.setdefault(girl[0], []).append(girl)
    print([b + '+' + g for b in boys for g in letterGirls[b[0]]])
    # 字典推导
    dic = {i: '{} squared is {}'.format(i, i ** 2) for i in range(5)}
    print(dic)


# test_5()


def test_6():
    '另外三条语句，pass、del和exec'
    # pass语句什么都不做
    name = 'Enid'
    if name == 'Ralph Auldus Melish':
        print('Welcome')
    elif name == 'Enid':
        # 什么都不做
        ""
        pass
    elif name == 'Bill Gates':
        print('Access Denied')
    # 上面的空代码块除了使用pass还可以直接用字符串，表示注释
    # 对于无用的名称可以使用del语句直接删除
    a = 1
    del a
    # print(a)将无法找到a
    # exec和eval函数用来动态地执行python代码字符串
    exec("print('exec函数执行代码',name)")
    eval("print('eval函数执行代码',name)")
    # 直接在当前命名空间执行语句，可能会污染当前命名空间的变量，所以应该传入第二参数充当命名空间
    from math import sqrt
    scope = {}
    exec("sqrt=88", scope)
    print(sqrt(4))
    print(scope['sqrt'])
    # eval函数执行一个表达式,eval也可提供命名空间
    print(eval("input('input something:')"))


test_6()
