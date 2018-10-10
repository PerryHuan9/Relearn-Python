# 本章学习Python的函数


# 1、可以使用functionName.__doc__访问到函数的注释
# 在交互式环境中可以使用help(function_name)获取有关函数的信息，这些信息包括文档字符串
def test_1():
    def say(name):
        '这是注释'
        print('Hello ! ' + name + ".")

    say('perry')
    print(say.__doc__)


# test_1()


# 2、修改函数的参数
def test_2():
    '实现一个通过名字、中间名和姓找到全名,使用面向结构编程'

    def init(data):
        data['first'] = {}
        data['middle'] = {}
        data['last'] = {}

    def lookup(data, label, name):
        labels = data.get(label)
        if labels:
            return labels.get(name)

    def store(data, full_name):
        names = full_name.split()
        if len(names) == 2: names.insert(1, "")
        labels = 'first', 'middle', 'last'
        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

    names = {}
    init(names)
    store(names, 'perry huang ')
    store(names, 'perry Yi huang')
    print(lookup(names, 'last', 'huang'))


# test_2()

# 关键字参数和默认值
def test_3():
    'Python中参数可使用关键字并带默认值'

    def hello(name, word):
        print('Hello,', name, '!', word)

    hello(name='perry', word='Are you ok ?')

    # 指定默认参数
    def hi(name='perry', word='Goodbye'):
        print('Hello,', name, '!', word)

    hi()

    # 位置参数和关键字参数结合使用
    def say(name, word='Goodbye'):
        print('Hello,', name, '!', word)

    say('黄益凛', word='I love you.')

    # 星号接收多余的参数,params将会是一个元组
    def print_param(title, *params):
        print(title)
        print(params)

    print_param('星号接收多余参数', 1, 2, 3, 4, 5)

    # 星号可以放中间位置，其后的参数必须使用关键字才能传递
    def print_param1(title, *params, last):
        print(title)
        print(params)
        print(last)

    print_param1('星号放中间', 12, 3, 4, 5, last='星号之后的元素必须使用关键字参数')

    def print_param2(**params):
        '*不会接收关键字参数，除非用**,这时params将会是字典，而不是元组'
        print(params)

    print_param2(last='finally', start='beginning')

    def print_params(x, y, z=3, *param, **params):
        print(x, y, z)
        print(param)
        print(params)

    print_params(1, 2, 11, 22, 33, d=88, a=34, b=55)


# test_3()

def test_4():
    '分配参数'

    def print_param(x, y, z, *all):
        print(x, y, z)
        print(all)

    param = [11, 22, 33, 44, 55, 66]
    # 给函数传入序列,相当于位置参数
    print_param(*param)
    # 给函数传入字典，则相当于关键字参数
    param = {'x': 111, 'y': 222, 'z': 333}
    print_param(**param)


test_4()


def practice():
    '对于传参的练习'

    def practice_1(**params):
        print('{name} is {thing} now.'.format_map(params))

    practice_1(**{'name': 'perry', 'thing': 'learning'})
    practice_1(name='黄益凛', thing='学习')

    def practice_2(one, two, *other):
        if other:
            print('other params is:', other)
        print(pow(one, two))

    practice_2(2, 3, 33, 44, 55)
    practice_2(*(4, 2, 66, 77, 88))
    practice_2(4, 3, 5, *[0, 11, 22])

    def interval(start, stop=None, step=1):
        if not stop:
            start, stop = 0, start
        i = start
        result = []
        while i < stop:
            result.append(i)
            i += step
        print(result)

    interval(4)
    interval(2, 8)
    interval(2, 8, 2)
    interval(8, step=3)


practice()
