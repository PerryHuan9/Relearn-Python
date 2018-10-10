def test_1():
    '''
   1、导入模块
   上面先通过sys模快将要导入的包的路径加入sys.path包列表中，但这并不是一种好的处理的方法，
   正确的做法之一是将module放在site-packages目录下，这样所有的程序都能导入它
   另一种做法是告诉解释器到哪里找包，修改sys.path就是这种做法，
   但常见的是将模块所在的目录包含在PYTHONPATH中
   '''
    import sys, pprint, mymodule
    sys.path.append('F:/PythonProject/Relearn-Python/src/module')
    # mymodule是在site-packages下的，故对任何程序可见
    mymodule.print_poem()
    # 在主程序中__name__的值为__main__，在模块中为模块名
    print(__name__)
    # 对于一行容纳不下的内容可以使用pprint打印
    pprint.pprint(sys.path)


# test_1()


def test_2():
    '''
     2、模块只会导入一次,如果一定要重新加载模块，
     可以使用importlib模块中的reload方法进行重新加载
    '''
    import module, importlib
    importlib.reload(module)
    module.print_hello()


# test_2()
def test_3():
    '''
    3、导入包
     包是另一种模块，包是一个目录可以包含多个模块，并且必须存在一个__init__.py文件,
     该文件存储着包代码，包建立好后可以像下面一样导入
    '''
    # 导入包，即导入package目录下的__init__.py文件,

    import package
    print(package.PI)

    # 导入包内的模块
    import package.rectangle
    package.rectangle.print_rectangle()
    from package import triangle
    triangle.print_triangle()




test_3()
