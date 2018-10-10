# Python中对异常的处理


# 1、抛出异常
def test_1():
    '测试抛出异常'
    # raise Exception #抛出的异常没有指出什么错误
    # raise Exception('hyperdrive overload')  # 抛出的异常指出什么错误
    raise ValueError


# test_1()


# 2、自定义异常类
class SomeCustomException(Exception): pass


# 3、捕获异常
def test_3():
    try:
        x = int(input('Enter the first number:'))
        y = int(input('Enter the last number:'))
        print(x / y)
    except ZeroDivisionError:
        print('The second number can\'n be zero')
    except ValueError:
        print('That is not a number,was it?')


# test_3()

# 一箭双雕，一个except处理多个错误
def test_4():
    try:
        x = int(input('Enter the first number:'))
        y = int(input('Enter the second number:'))
        print(x / y)
    # except (ZeroDivisionError, ValueError, TypeError):
    # 或者提供打印信息
    except (ZeroDivisionError, ValueError) as e:
        print('your number were bogus...', e)


# test_4()


# 捕获所有异常，只用except，但这很危险，这将连用户Ctrl+C退出意图也捕获
def test_5():
    try:
        x = int(input('something:'))
        y = int(input('something:'))
        print(x / y)
    # except:
    #     print('something wrong was happened')
    # 更好的方法是像下面这样，只会捕获exception和exception派生而来的错误
    # 像ctrl+c和systemExit退出的错误是从Exception的超类BaseException继承而来
    except Exception as  e:
        print('something wrong has happened', e)
    else:
        print('当没有异常时执行这一句')


# test_5()
def practice():
    while True:
        try:
            x = int(input('Enter a number:'))
            y = int(input('Enter a number:'))
            print(x / y)
        except Exception as  e:
            print('something has happened:', e)
        else:
            break
        finally:
            print('无论如何我都会执行')


# practice()


# 4、异常和函数
# 函数内的异常会逐级向上传播，直到处理，但一直没有处理就会传播到主程序，
# 如果主程序也没有处理错误，程序将停止并显示栈跟踪信息
def faulty():
    raise Exception('我抛出的异常将会向上传播')


def ignore_exception():
    faulty()


def handle_exception():
    try:
        ignore_exception()
    except Exception as  e:
        print('处理异常', e)


# handle_exception()


# 5、运用 if条件判断和try except对比

def app(user):
    print('Name:', user['name'])
    print('Age:', user['age'])
    if 'gender' in user:
        print(user['gender'])


def application(user):
    print('Name:', user['name'])
    print('Age:', user['age'])
    try:
        print(user['gender'])
    except:
        pass


user = {'name': 'perry', 'age': 22}
# app(user)
# application(user)
# 效果一致，但if判断显得效率不高，对gender会读取两遍，
# 虽然try方法对效率的提高微乎其微，但其简洁易读


# 6、发出警告
# 对于一些情况，我们并不想抛出错误，但要提示用户，可以使用warnings模块中的warn
from warnings import warn, filterwarnings


def test_6():
    warn('I\'ve got a bad feeling about this')
    # 使用filterwarnings来抑制发出的警告
    # filterwarnings('ignore')  # ignore表示忽略错误，还有error表示warn升级为错误
    warn('这条警告不会显示')
    # filterwarnings('error')
    # warn('发生错误，结束程序')
    # print('不会执行')
    # filterwarnings指定只忽略指定的警告
    filterwarnings('ignore', category=DeprecationWarning)
    warn('raise SomeCustomException', DeprecationWarning)
    warn('其它警告照常显示')
    print('end')


test_6()
