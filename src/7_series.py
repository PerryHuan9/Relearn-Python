# python支持一种数据结构的基本概念，名为容器。容器基本上就是可以包含其它对象的对象
# 主要有三种容器：序列（列表、元组和字符串）、映射（字典）和集合（set）
# 本篇主要介绍序列的操作

# python中重要的序列：列表、元组和字符串
a = [['黄益凛', 22], ['黄益威', 24], ['黄月娥', 27]]
print(a)


# 一、通用的序列操作包括索引、切片、相乘和成员资格检查
# 1、索引操作序列
def test_1():
    b = [12, 23, '你好', 'hello word', 3.14]
    print('list b is:', b)
    print('b[0]:', b[0])
    print('b[2]:', b[2])
    print('b[-1]:', b[-1])  # -1为倒数第一位
    fourth = input('Year:')[3]
    print('the fourth of Year is :', fourth)  # 将获得输入年份的第四位


# test_1()

# 对序列进行加操作会拼合两个序列，使用一个整数n乘序列则会复制该序列n次，返回一个加长的序列
def test_2():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    # 日后面的后缀，西方日历所带有的
    endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']
    year = input('Year:')
    month = int(input('Month(1-12):'))
    day = input('Day:(1-31):')
    number = day + endings[int(day) - 1]
    print(months[month - 1], number, year)


# test_2()

# 2、切片序列操作
# 对序列除了索引，还可以使用切片来访问特定范围的元素
# 其使用两个索引，并用冒号分隔,第一个索引是包含的第一个元素的编号，
# 第二个索引是切片后余下的第一个元素的编号
def test_3():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('numbers:', numbers)
    slicing_numbers = numbers[3:6]  # 4,5,6 numbers[3]包含 numbers[6]不包含
    print('切出的片：', slicing_numbers)
    print('切片后原来的序列：', numbers)  # 切片不会修改原来的序列
    # 第二索引对应元素的位置必须在比第一索引对应元素的位置之后，否则无法切片，返回空列表
    space = numbers[3:1]
    print('第二索引比第一索引小：', space)
    # 索引为负数,表示从后面开始切
    slicing = numbers[-3: -1]
    print('numbers[-3: -1]：', slicing)  # 7,8
    # 简写，省略第二索引则表示至序列末尾
    slicing1 = numbers[-3:]
    print('numbers[-3:]:', slicing1)
    # 省略第一索引，则表示切片始于序列开头
    slicing2 = numbers[:-1]
    print("numbers[:-1]:", slicing2)
    # 第一第二索引都省略则会复制整个序列
    numbers2 = numbers[:]
    print('numbers[:]:', numbers2)
    # 两个索引正负数结合的情况
    slicing3 = numbers[5:-1]
    slicing4 = numbers[-5:8]
    print('numbers[5:-1]:', slicing3)
    print('numbers[-5:8]: ', slicing4)
    print('+++++++++++++++可爱的分隔符++++++++++++++++++++++')
    # 在第二索引后面指定步长，步长为n表示在第一第二索引指定范围内每隔n-1个元素取一个元素
    print('numbers:', numbers)
    s1 = numbers[3:8:1]
    print("numbers[3:8:1]:", s1)
    s2 = numbers[3:8:2]
    print('numbers[3:8:2]:', s2)
    s3 = numbers[::3]
    print('numbers[::3]:', s3)
    # 步长不能为0，但可以为负数，表示从右向左提取元素
    s4 = numbers[::-3]
    print("numbers[::-3]:", s4)


# test_3()


# 3、序列相加，乘法
# 对两个序列进行相加，则会拼接这两个序列来创建一个新序列
# 使用一个整数n乘以一个序列，则会重复这个序列n次来创建一个新序列
def test_4():
    # 序列相加
    numbers = [1, 2, 3, 4, 5]
    string = ['上', '山', '打', '老', '虎']
    numbers_string = numbers + string
    print('numbers:', numbers)
    print('string:', string)
    print('numbers + string:', numbers_string)
    # 序列乘法
    strings = 'python' * 5
    print("'python' * 5:", strings)
    numbers2 = [8] * 10
    print('[8]*10:', numbers2)
    # 创建什么都没有的列表，可以使用None,None在Python中表示什么都没有
    # 使用None可以对列表的长度进行初始化
    sequence = [None] * 10
    print('[None]*10:', sequence)


# test_4()

def test_5():
    sentence = input('Sentence:')
    screen_width = 80
    text_width = len(sentence)
    box_width = text_width + 6
    left_width = (screen_width - box_width) // 2
    print()
    print(' ' * left_width + '+' + '-' * (box_width - 2) + '+')
    print(' ' * left_width + '|' + ' ' * (box_width - 2) + '|')
    print(' ' * left_width + '|  ' + sentence + '  |')
    print(' ' * left_width + '|' + ' ' * (box_width - 2) + '|')
    print(' ' * left_width + '+' + '-' * (box_width - 2) + '+')
    print()


# test_5()


# 4、序列成员资格验证
# 成员资格验证是通过in检验序列中是否存在该元素
def test_6():
    string = 'Are you ok ?'
    print('string:', string)
    s1 = 'r' in string
    print("'r' in string:", s1)
    s2 = 'you' in string
    print("'you' in string:", s2)
    numbers = [1, 2, 3, 4, 5, 6]
    print('numbers:', numbers)
    s3 = [1, 2, 3] in numbers
    # 只能检查元素是否在列表中，不能检查子列表是否在
    print('[1, 2, 3] in numbers:', s3)  # false
    users = ['perry', 'simon', 'hali']
    name = input('Name:')
    s3 = name in users
    if s3:
        print(name + ' is in the users list .')
    else:
        print(name + ' is not in the users list .')


# test_6()

def test_7():
    database = [
        ['perry', '1234'],
        ['黄益凛', '4567'],
        ['黄益威', '8888'],
    ]
    user_name = input('User Name:')
    pwd = input('Password:')
    if [user_name, pwd] in database:
        print('Access granted')


# test_7()


# 5、长度、最小值和最大值
# 序列的长度，最小值和最大值可以使用内置函数 len(),min()和max()来求
def test_8():
    numbers = [100, 23, 45, 56]
    numbers_len = len(numbers)
    numbers_max = max(numbers)
    numbers_min = min(numbers)
    print('len(numbers):', numbers_len)
    print('max(numbers):', numbers_max)
    print('min(numbers):', numbers_min)


# test_8()
