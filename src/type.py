'''
学习python的所有类型：
    1、None
    2、NotImplemented 方法未实现指定运算符的运算法则时返回此值
    3、Ellipsis 表示...
    4、Number 表示所有数字类型(int、float、complex、bool(布尔值也属于一种特殊的数字类型))
    5、序列 
        不可变序列： 元组(tuple)、字符串(str)、字节串（bytes）
        可变序列：列表(list)、字节数组（bytearray）
    6、集合  包括 集合（set）和 冻结集合（frozenset）
    7、映射 字典（dict）
    8、可调用类型
        用户自定义函数
        实例方法
        生成器函数
        协程函数
        异步生成器函数
        内置函数
        内置方法
        类
        类实例
    9、模块
    10、自定义类
    11、类实例
    12、I/O对象
    13、内部类型

'''


def learn_number_type():
    '''
    Number类型表示数字类型，包括整数，浮点数和虚数, 布尔值
    '''
    from numbers import Number
    print(isinstance(12, Number))
    print(isinstance(1.234, Number))
    print(isinstance(1+2j, Number))
    print(isinstance(True, Number))
    b = 1,
    print(b)


# learn_number_type()


global_field = 8888
def learn_fun_field():
    '''
    测试用户自定义函数的内置属性
    '''
    def test_fun_field(name, age=888, *arg, sex="man", **kargs):
        '''
        函数的doc
        '''
        global global_field
        global_field = 9999


    print(test_fun_field.__doc__)
    print(test_fun_field.__module__)
    print(test_fun_field.__code__)
    print(test_fun_field.__dict__)
    print(test_fun_field.__globals__)
    print(test_fun_field.__defaults__)
    print(test_fun_field.__kwdefaults__)


# learn_fun_field()


def learn_obj_method():
    '''
    测试实例方法的属性
    '''
    class Test:
        def test_method(self, name):
            '''
            实例方法
            '''
            myname = name
            print(myname)
        
    test = Test()
    print(test.test_method.__self__)
    print(test.test_method.__func__)
    print(test.test_method.__doc__)
    print(test.test_method.__name__)


learn_obj_method()
