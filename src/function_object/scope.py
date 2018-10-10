# Python的作用域


# 1、作用域
x = 666
y = 777
z = 888


def test_1():
    '使用vars内置函数可以返回当前作用域对象，利用该对象可以访问到当前作用域的所有变量'
    x = 888
    scope = vars()
    print(scope['x'])  # 888
    # 使用global内置函数可以返回全局作用域对象
    this_global = globals()
    print(this_global['x'])  # 666


test_1()


# 2、修改全局变量的值
def test_2():
    # 在函数内赋值默认是建立一个局部变量，如要修改变量需要使用global声明
    global x  # 经过声明后，下面使用的x都将会是全局变量x
    print(x)
    x = 12345
    print(x)


# test_2()
# print('全局打印：',x)


def test_3():
    'python提供了一些有助于函数式编程的函数，map、filter和reduce'
    '事实上map和filter可以使用列表推导来代替'
    lst = list(map(str, range(1, 10)))
    print(lst)
    lst2 = [str(x) for x in range(1, 10)]
    print(lst2)

    def func(x):
        'isalnum()判断字符串是否只包含字母和数字'
        return x.isalnum()

    seq = ['foo', 'x41', '?!', "***"]
    fil = list(filter(func, seq))
    print(fil)
    fil2 = [x for x in seq if x.isalnum()]
    print(fil2)
    # 至于reduce方法就无法使用列表表达式表示，但可以使用lambda表达式
    # lambda即匿名函数，是函数简略写法
    print(list(filter(lambda x: x.isalnum(), seq)))  # 以lambda表达式代替上面传入的函数
    from functools import reduce
    total = reduce(lambda x, y: x + y, range(1, 9))
    print(total)
    print(sum(range(1, 9)))


test_3()
