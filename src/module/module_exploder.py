# 探索模块

def test_1():
    '''
    使用函数dir可以列出对象所有的方法属性，对于模块可以列出所有的函数、变量和类；
    根据约定，模块中那些以下划线开头的函数和变量是内部使用的，并非供外部使用；
    模块中的__all__变量是一个保存着所有对外名称的列表，这个变量旨在定义模块的公共接口，
    但使用from module import *将导入__all__变量保存的函数或变量

    '''
    import pprint, copy
    # dir将会把所有的函数变量打印出来，但其中的以下划线开头的函数变量仅供内部使用，
    # 我们可以使用列表推导过滤
    pprint.pprint(dir(copy))
    print([v for v in dir(copy) if not v.startswith('_')])
    # help方法查看copy模块中的copy函数的帮助信息
    help(copy.copy)
    # 文档信息保存在__doc__中
    print(range.__doc__)
    # 源代码的路径保存在__file__变量中
    print(copy.__file__)


test_1()
