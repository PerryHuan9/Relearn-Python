# python 的迭代器协议


def test_1():
    '''
    在Python中规定，凡是实现了__iter__(self)方法的对象都是可迭代的，可以被for in迭代，
    另外，__iter__方法应该返回一个实现了__next__(self)方法的迭代器对象

    '''

    class Fibs:
        def __init__(self):
            self.a = 0
            self.b = 1

        def __iter__(self):
            return self

        def __next__(self):
            self.a, self.b = self.b, self.a + self.b
            return self.a

    f = Fibs()
    for n in f:
        print(n)
        if n > 1000:
            break


# test_1()


def test_2():
    '''
    从迭代器创建序列
    :return:
    '''

    class TestIterator:
        value = 0

        def __iter__(self):
            return self

        def __next__(self):
            self.value += 1
            if self.value > 10:
                raise StopIteration
            return self.value

    ti = TestIterator()
    lst = list(ti)
    print(lst)


# test_2()

def test_3():
    '''
    生成器函数，一种能返回迭代器的函数
    :return:
    '''
    nested = [[1, 2], 88, [3, 4], [5], '你好']

    def flatten(nested):
        for n in nested:
            if isinstance(n, list):
                for e in n:
                    yield e
            else:
                yield n

    lst = list(flatten(nested))
    print(lst)

    # 另一种生成生成器的方式，生成器推导，其类似列表推导
    g = ((i + 2) ** 2 for i in range(10) if i % 2 == 0)
    print(list(g))
    # print(next(g))
    # 其有一个好处,但用做函数参数时，不需要再写一个括号
    print(sum((i + 2) ** 2 for i in range(10) if i % 2 == 0))


# test_3()


def test_4():
    '''
    递归生成器函数
    '''

    def generator(nested):
        try:
            try:
                nested + ''
                yield nested
            except TypeError:
                for n in nested:
                    for e in generator(n):
                        yield e
        except TypeError:
            yield nested

    nested = [('foo', 'bar'), 'hello', ['人生观', ['价值观']], '世界观']
    print(list(generator(nested)))

    def repeater(v):
        while True:
            new = yield v
            if new:
                v += new

    r = repeater(1)
    print(next(r))
    r.send(23)
    print(next(r))
    # r.throw(Exception)
    r.close()
    # print(next(r))


test_4()
