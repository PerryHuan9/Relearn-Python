# Python继承

class Filter:

    def init(self):
        self.blocked = []

    def filter(self, seq):
        return [e for e in seq if e not in self.blocked]


class SPAMFilter(Filter):
    def init(self):
        self.blocked = ['SPAM']


class APPFilter(SPAMFilter):
    def init(self):
        self.blocked.append('APP')


def test_1():
    seq = ['SPAM', 'SPAM', 'eggs', 'bacon', 'SPAM', 'other']
    filter = SPAMFilter()
    filter.init()
    lst = filter.filter(seq)
    print(lst)

    # 内置方法issubclass和类的特殊属性__base__指向其父类
    print(issubclass(SPAMFilter, Filter))  # True
    print(issubclass(Filter, SPAMFilter))  # False
    print(issubclass(APPFilter, Filter))  # True
    print(Filter.__bases__)  # (<class 'object'>,)
    print(SPAMFilter.__bases__)  # (<class '__main__.Filter'>,)
    print(APPFilter.__bases__)  # (<class '__main__.SPAMFilter'>,)
    # 内置方法isinstance,判断对象是否是特定类的实例
    print(isinstance(filter, SPAMFilter))  # True
    print(isinstance(filter, Filter))  # True

    # 对象的__class__属性获知其属于哪个类
    print(filter.__class__)  # <class '__main__.SPAMFilter'>
    print(type(filter))  # <class '__main__.SPAMFilter'>
    print(type(' '))  # <class 'str'>


# test_1()

# Python多继承
# 必须明确，多继承是有顺序的，在类名后面的括号中，
# 对于继承的多个类中的同名方法，位于前面的类的同名方法覆盖后面的类的同名方法


class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)

    def talk(self):
        print('我是talk方法')


class Talker:
    def talk(self):
        print('Hi,my value is ', self.value)


# 上面 Calculator类也有talk，要想调用到Talker雷类的talk方法，
# 必须将Talker类放在前面,这叫方法解析顺序
class TalkingCalculator(Talker, Calculator):
    pass


def test_2():
    tc = TalkingCalculator()
    tc.calculate('1+2*88')
    tc.talk()
    # hasattr判断对象是否存在指定属性
    print(hasattr(tc, 'talk'))
    print('tc has b :', hasattr(tc, 'b'))
    # getattr直接获取对象的指定方法，callable判断对象指定方法是否可以调用
    # getattr的第三个参数表示在没有该属性的则返回的变量
    print('tc talk method can call?:', callable(getattr(tc, 'talk', None)))
    # setattr内置方法的功能和getattr相反，用于设置对象的属性
    setattr(tc, 'talk', lambda: print('我改变了这个方法属性'))
    tc.talk()
    # 获取方法属性并执行
    getattr(tc, 'talk', None)()


# test_2()



