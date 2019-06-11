'''
    python 的内置函数

'''
from functools import cmp_to_key
from pprint import pprint 

def dosort(a, b):
    if a > b:
        return -1
    if a < b:
        return 1;
    return 0

lst = [100, 88, 108, 56,99]
print(sorted(lst, key=cmp_to_key(dosort)))


class A:
    def __init__(self):
        self.a = 'A类'
    def print_a(self):
        print(self.a)


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.b = 'B类'
    def print_b(self):
        print(self.b)


# b = B()
# b.print_b()
# b.print_a()


def type_math():
    # abs 求绝对值, complex 创建复数，直接 a + bj 也可以创建
    print(abs(100), abs(-100))
    f = complex(-5, -5)
    print(f, abs(f))
    c = -5-4j;
    print(abs(c))
    # divmod(a, b) 返回一个包含商和余数的元组
    print(divmod(9, 2))
    # float 将一个字符串货数据转为浮点数，无参数则为0.0
    print(float(), float(8888))
    # int([x[, base]])
    print(int(8.888), int(15.555))
    print(int('14', 5))
    print(dir())
    print(dir([]))
    print('\r\n')
    a = 8
    s = 'abcdef'
    print(id(a), id(s))
    print(ascii('你好'))
    print(ord('凛'))
    print(b'1231231232312')
    print(bytearray('你好啊', 'utf-8'))
    def is_odd(n):
        return n%2 == 1;
    print(list(filter(is_odd, [1,2,3,4,5,6,7,8,9])))
    print(bytes([1,2,3,4,5]))
    print(bytes({1: 88, 2: 99, 3: 188}))
    print(bytes('abcdefgh', 'utf-8'), bytes('会登凌绝顶，一览众山小', 'utf-8'))


# type_math()


def test_format():
    print("1、{}".format('easy'))
    print("2、{1} {0}".format('index', 'according'))
    print("3、{name}: {url}".format(name="orca-lamb.xyz", url="129.204.15.100"))
    web = {'name': 'yilin.pro', 'url': '129.204.15.100'}
    print("4、{name}: {url}".format(**web))
    print("5、{0[name]}: {0[url]}".format(web))
    web2 = ['name', 'yilin.pro']
    print("6、{}: {}".format(*web2))
    print("7、{0[0]}: {0[1]}".format(web2))
    print('###############我是神奇的分割线&&&&&&&&&&&&&&&&&&&&')
    # 格式化
    print('{:.2f}'.format(10))
    print('{:+.2f}'.format(10)) # +10.00
    print('{:.0f}'.format(10.58)) # 11 
    print('{:0>5.2f}'.format(8)) #08.00
    print('{:x<6d}'.format(8)) # 8xxxxx
    print('{:,}'.format(8888888)) 
    print('{:.4%}'.format(8888888))
    print('{:.4e}'.format(8888888)) 
    print('{:<10}end'.format(88)) 
    print('{:<10}end'.format(99)) 
    print('{:>10}'.format(99)) 
    print('{:>10}'.format(99)) 
    print('begin{:^10}end'.format(99)) 
    print('begin{:^10}end'.format(99)) 



# test_format()


class Test:
    num = 1
    def __init__(self):
        self.__target = 'error'
        self._target = 'perry'
    
    @staticmethod
    def handle(things):
        print('It is handling {}. num: {}'.format(things, Test.num))
        Test.num += 1;
        print(Test().target)
    
    @classmethod
    def my_handle(cls):
        print(cls.num)
        print(cls().target)


    @property
    def target(self):
        return self.__target
        
    @target.setter
    def target(self, target):
        self.__target = target
    
    @target.deleter
    def target(self):
        print('正在删除target属性')
        del self.__target
    

def test_class():
    Test.handle('喂猫')
    test = Test()
    test.handle('dog')
    test.my_handle()
    print(test.target)
    test.target = 'info'
    print(test.target)
    del test.target
    print(test._target)

# test_class()


def do_test():
    s = frozenset([1,2,2,2,1,1,4,5,6,6])
    s2 = frozenset([1,2,2,2,1,1,4,5,6,6,23,34])
    print(s)
    print(list(s)+list(s2))
    print(vars(Test))
    print()
    print(dir(Test))
    print()
    print(vars(Test()))
    print()
    print(dir(Test()))



# do_test()

def test_compile():
    code = "for i in range(10): print(i)"
    c = compile(code, '', 'exec')
    exec(c)
    # 只有一些简单的表达式代码才能编译成eval
    a = 11
    b = 77
    code = "print(a+b)"
    d = compile(code, '', 'eval')
    eval(d)
    pprint(globals())
    print()
    l = str([1,2,3])
    d = str({'a': 1212})
    print(hash('aaa'), l, hash(l), d, hash(d))
    pprint(locals())
    print(list(map(lambda x: x**2, [1,2,3,4,5])))
    v = memoryview(bytearray('abcdef', 'utf-8'))
    print(v.tobytes())

# test_compile()


def test_common():
    a = [1,2,3,4,5]
    b = 'a', 'b', 'c', 'd'
    c = '@', '#', '$', '%'
    three = zip(a, b, c)
    print(list(three))
    two = zip(a, c)
    print(dict(two))
    print(pow(10, 2))
    print(pow(10, -2))
    print(str([1,2,3,4,'434', '213']))
    print(repr([1,2,3,4,'434', '213']))



test_common()

# __import__('1_expression')


print(list({1:2, 3:4}.keys()))










 


















