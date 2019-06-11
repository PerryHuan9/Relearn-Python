'''
装饰器: 装饰器是一个返回可调用对象的可调用对象
'''
from pprint import pprint
def test_func_decorator():
    def int_add(func):
        def wrapper(*arg):
            result = func(*arg)
            if isinstance(result, int):
                result += 1
            return result
        return wrapper

    @int_add
    def add(a, b):
        return a + b

    print(add(5, 6))
    print(add('abc', '123'))

    # 重载__call__实现， 这种方式对类方法的操作无效
    class IntAdd:
        def __init__(self, func):
            self.func = func
        
        def __call__(self, *arg):
            '''
            该方法在被装饰函数调用时调用
            '''
            result = self.func(*arg)
            if isinstance(result, int):
                result += 1
            return result

    @IntAdd
    def test_add(a, b):
        return a + b

    print(test_add(12, 16)) #29
    print(test_add('edf', '23')) #edf23

    class Test:
        @int_add
        def add(self, a, b):
            return a + b

    test = Test()
    print(test.add(12,34))
        

# 类装饰器
def test_class_decorator():

    def AddId(C):
        class Wrapper(C):
            current_id = 0
            def __init__(self, *arg):
                super().__init__(*arg)
                self.id = Wrapper.current_id
                Wrapper.current_id += 1

        return Wrapper

    @AddId
    class Class:
        def __init__(self, class_name, class_location):
            self.class_name = class_name
            self.class_location = class_location

        def show_info(self):
            pprint(self.__dict__)


    c = Class('15通卓', '东莞理工学院')
    c1 = Class('16通1', '东莞理工学院') 
    c2 = Class('16通1', '东莞理工学院') 
    c.show_info()
    c1.show_info()       
    c2.show_info()
    print(isinstance(c, Class)) #True


# 装饰器嵌套
def test_nest_decorator():
    def d1(fn):
        def wrapper(*arg):
            result = fn(*arg)
            return 'd1: {}'.format(result)
        return wrapper

    def d2(fn):
        def wrapper(*arg):
            result = fn(*arg)
            return 'd2: {}'.format(result)
        return wrapper

    def d3(fn):
        def wrapper(*arg):
            result = fn(*arg)
            return 'd3: {}'.format(result)
        return wrapper

    
    @d1
    @d2
    @d3
    def test(s):
        return 'test: {}'.format(s)
    

    print(test('你好'))


test_nest_decorator()



def test_decorator_arguement():
    '''
    测试装饰器参数
    '''
    def arg_decorator(a, b):
        def decorator(fn):
            def wrapper(*arg):
                result = fn(*arg)
                return '{}:{}:{}'.format(a, result, b)
            return wrapper
        return decorator
    
    @arg_decorator('begin', 'end')
    def test(arg):
        return arg
    
    print(test('我在中间'))

test_decorator_arguement()








    


