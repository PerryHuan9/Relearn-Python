# Python中的魔术方法（特殊方法）、特性和迭代器


# 1、__init__构造函数
def test_1():
    # python的构造函数，在对象呗创建后自动被调用
    class FooBar:
        def __init__(self, value='默认值'):
            self.value = value

        def print_vlue(self):
            print(self.value)

    fb = FooBar('乘风破浪会有时，直挂云帆济沧海')
    fb.print_vlue()

    # 继承时重写了__init__方法，必须调用超类的，如果不调用将不会继承到超类的方法和属性
    class Foo(FooBar):
        def __init__(self, foo='foo'):
            self.foo = foo

        def print_foo(self):
            print(self.foo)

    f = Foo('会登凌绝顶，一览众山小')
    f.print_foo()

    # f.print_vlue() #报错，因为重写构造函数没有调用父类构造函数

    # 有两种方法可以解决上述问题:调用未关联的超类构造函数，以及使用super
    # ① 调用未关联（通过类名调用）的超类构造函数，
    # 这种方法只要是兼容Python2,因为Python2中不支持super
    class Bar(FooBar):
        def __init__(self, bar='bar'):
            FooBar.__init__(self, '我自横刀向天笑，去留肝胆两昆仑')
            self.bar = bar

        def print_bar(self):
            print(self.bar)

    b = Bar('倚天抽宝剑，跨海斩长鲸')
    b.print_bar()
    b.print_vlue()

    # ②使用super,这种方法和第一种方法是等价的，但其更方便，当多继承时，
    # 第一种方法需要调用多个超类的构造函数，super只需调用一次，
    # super只适合新式类，Python只有新式类

    class SuperBar(FooBar):
        def __init__(self, super_bar='super_bar'):
            super().__init__('我失骄杨君失柳，杨柳轻飏直上重霄九')
            self.super_bar = super_bar

        def print_super_bar(self):
            print(self.super_bar, self.value)

    sb = SuperBar('人生若只如初见，何事秋风悲画扇')
    sb.print_super_bar()
    sb.print_vlue()


# test_1()

def test_2():
    '''
        基本的序列和映射协议
        在Python中，多态仅基于对象的行为（而不需要继承某个基类或实现某个接口），
        只要求对象遵循特定的协议，因此要成为序列，只需遵循序列的协议即可
        序列的协议对不可变对象需要实现两个方法，可变对象需要实现四个方法
        __len__(self),__getitem__(self,key),__setitem__(self,key,value),__delitem__(self,key)

    '''

    class ArithmeticSequence:

        def __check_index(self, index):
            if not isinstance(index, int): raise TypeError
            if index < 0: raise IndexError

        def __init__(self, start=0, step=1):
            self.start = start
            self.step = step
            self.changed = {}

        def __getitem__(self, key):
            self.__check_index(key)
            try:
                return self.changed[key]
            except:
                return self.start + key * self.step

        def __setitem__(self, key, value):
            self.__check_index(key)
            self.changed[key] = value

    # 因为ArithmeticSequence类遵循了序列的协议
    a = ArithmeticSequence(1)
    print(a[4])
    a[5] = 888
    print(a[5])
    # del  a[6] 报错，因为并没有实现__del__方法
    # __len__方法也没有实现,因为其长度是无限的
    # a[-1]


# test_2()


def test_3():
    '''
    通常遵循一个协议必须要实现很多方法，还有许多普通方法，这样太麻烦了，幸好我们有更好的方法——继承
    像测试2那样，如果我们想创建一个类类表对象，可以继承list类，然后重写需要用到的方法，
    加入自己想要的功能

    '''

    class CounterList(list):
        def __init__(self, lst):
            super().__init__(lst)
            self.counter = 0

        def __getitem__(self, item):
            self.counter += 1
            return super().__getitem__(item)

    cl = CounterList([1, 2, 3, 4, 5, 6, 7])
    print(cl[1], cl[2], cl[5])
    print(cl.counter)


# test_3()
from math import sqrt


def test_4():
    '''
    poperty存取特性
    property是一个类，可传入四个方法，第一个获取方法，第二个为设置方法，
    第三个为删除方法，第四个为文档字符串
    可以使用装饰器方式替代函数设置方式
    '''

    class Rectangle:
        def __init__(self):
            self.width = 0
            self.height = 0

        @property
        def area(self):
            return self.width * self.height

        @area.setter
        def area(self, area):
            self.width = self.height = sqrt(area)

        @area.deleter
        def area(self):
            print('希望delete掉area')

        def set_size(self, size):
            self.width, self.height = size

        def get_size(self):
            print('get_size has called')
            return self.width, self.height

        size = property(get_size, set_size)

    # 在经上面设置后，我们可以像访问width和height一样访问size
    r = Rectangle()
    r.height = r.width = 100
    print(r.width, r.height, r.size, r.area)
    r.size = [666, 888]
    print(r.width, r.height, r.size, r.area)
    r.area = 888
    print(r.width, r.height, r.size, r.area)
    del r.area


# test_4()


def test_5():
    '''
    类方法和静态方法：对象和类都可以调用
    类方法会默认传入一个类似于self的参数cls，该参数关联类
    创建类方法和静态方法都有两种方式：装饰器方式，方法设置方式
    :return:
    '''

    class Class:
        # 类命名空间定义的变量，类和对象都可以访问
        abcd = 0
        print('你好', abcd)

        # 类命名空间定义的函数，只有类可以访问，对象无法访问
        def abc():
            print('花有重开日，人无再少年')

        def smeth():
            print('秦皇汉武，略输文采')

        smeth = staticmethod(smeth)

        @staticmethod
        def smethod():
            print('唐宗宋祖，稍逊风骚')

        def cmeth(cls):
            # cls.smeth()
            print('一代天骄，只识弯弓射大雕')

        cmeth = classmethod(cmeth)

        @classmethod
        def cmethod(cls):
            # cls.smethod()
            print('数风流人物，还看今朝')

        def call_all(self):
            self.smeth()
            self.smethod()
            self.cmeth()
            self.cmethod()

    Class.abcd = 888
    c = Class()
    c.call_all()
    print(Class.abcd)


# test_5()


def test_6():
    '''
    以下四个方法都是用于访问对象的属性：
    __getattr__(self,name)：在找不到对象的指定属性时调用
    __setattr__(self,name,value):设置对象的属性时候调用
    __delattr__(self,name):试图删除对象的属性时调用
    __getattribute__(self,name):在属性被访问时自动访问,返回值时又会访问属性，
    又会调用到它，所有为避免无限循环，最好不用重写它，使用父类的即可
    在可能的情况下应该使用property特性代替这种拦截属性访问的方式
    '''

    class Rectangle:
        def __init__(self):
            self.width = 0
            self.height = 0

        def __setattr__(self, key, value):
            print('对{}属性赋值:{}'.format(key, value))
            if key == 'size':
                self.width, self.height = value
            else:
                self.__dict__[key] = value

        def __getattr__(self, item):
            print('找不到属性：', item)
            if item == 'size':
                return self.width, self.height
            else:
                raise AttributeError

        def __delattr__(self, item):
            print('删除属性', item)

    r = Rectangle()
    r.height = 100
    r.width = 88
    print(r.size)
    r.size = 66, 88
    print(r.width, r.height, r.size)
    del r.size


test_6()
