'''
特殊方法名称
    基本定制
        __new__: 静态方法，调用以用于创建一个类的新实例
        __init__: 在__new__返回实例后调用该方法
        __del__: 在实例被销毁时调用
        __repr__: 返回一个正式的字符串表示，面对程序员，repr()调用
        __str__: 返回一个非正式的字符串表示，面对用户，str()调用
        __bytes__: 实现之后调用bytes()会返回实例的字节串表示
        __format__: 格式化字符串字面值, 使用format()内置函数或str.format()时,如果未定义该方法，则返回__str__结果
        __hash__: hash()函数调用，应该返回一个完全标识该对象的整数值
        __bool__: bool()函数调用, 如不定义该方法， bool()的时候会去调用__len__
        富比较方法：
            __lt__: <
            __le__: <=
            __eq__: ==
            __ne__: !=
            __gt__: >
            __ge__: >=


'''


def test_base():
    class TestNew:
        def __new__(cls, *arg):
            print('__new__:', cls)
            print('__new__:', arg)
            return super().__new__(cls)
        def __init__(self, *arg):
            print('__init__:', self)
            print('__init__:', arg)
            self.test = 'TEST'

        def __del__(self):
            print('__del__: 实例即将被销毁')
        
        def __str__(self):
            print('__str__: 非正式字符串表示')
            return '__str__TestNew 实例'
        
        def __repr__(self):
            print('__repr__: 正式的字符串表示')
            return '<正式表示:{}>'.format(self)
        
        def __bytes__(self):
            print('__bytes__: 返回字节串表示')
            return bytes('TestNew', 'utf-8')
        
        def __format__(self, spec):
            return '__format__结果'
        
        def __hash__(self):
            return hash(self.test)
        
    test = TestNew('name', 'dodo')
    print(test)
    print(repr(test))
    print(bytes(test))
    print('开始：{}'.format(test))
    test2 = TestNew('perry')
    print(hash(test), hash(test2))
    del test
    from datetime import datetime



test_base()

def test_rich_comparison():
    '''
    测试‘富比较’方法
    '''
    class Compare:
        def __init__(self, value=0):
            self.value = value

        def __lt__(self, other):
            return self.value < other.value
        
        def __le__(self, other):
            return self.value <= other.value
        
        def __eq__(self, other):
            return self.value == other.value

        def __ne__(self, other):
            return self.value != other.value

        def __gt__(self, other):
            return self.value > other.value

        def __ge__(self, other):
            return self.value >= other.value
    
    c1 = Compare(1)
    c2 = Compare(2)
    print(c1 < c2)
    print(c1 <= c2)
    print(c1 == c2)
    print(c1 != c2)
    print(c1 > c2)
    print(c1 >= c2)


# test_rich_comparison()


