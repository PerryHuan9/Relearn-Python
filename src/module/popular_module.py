# 测试标准库中一些受欢迎的模块

def test_sys():
    '''
    1、模块sys用于访问于python解释器紧密相关的函数和变量
    argv变量保存着变量名
    :return:
    '''
    import sys
    print(sys.argv)
    args = sys.argv[1:]
    args.reverse()
    print(' '.join(args))


# test_sys()


def test_os():
    '''
    2、 os模块用于访问多个操作系统服务
    '''
    import os
    # 打开火狐浏览器
    os.system(r'D:\"Program Files (x86)"\"Mozilla Firefox"\firefox.exe')
    # window特有的函数,路径中包含空格也没有关系
    os.startfile(r'D:\Program Files (x86)\Mozilla Firefox\firefox.exe')


# test_os()

def test_fileinput():
    '''
    3、fileinput模块用于操作文本文件
    '''
    import fileinput
    for line in fileinput.input(inplace=True):
        line = line.rstrip()
        num = fileinput.lineno()
        print('{:<50}#{:2d}'.format(line, num))


# test_fileinput()


# Python time模块


def test_time():
    '''
    4、时间可以由包含九个元素的元组表示。
    这九个元素分别表示年、月、日、时、分、秒、星期、儒略日、夏令时

    '''
    import time
    # 将时间元组转为时间字符串，默认为当前时间
    time_str = time.asctime()
    print(time_str)
    # strptime讲一个字符串转化为时间元组，为asctime的逆操作
    time_tuple = time.strptime(time_str)
    print(time_tuple)
    # localtime将一个实数转为时间元组，默认为当前时间
    time_tuple = time.localtime(19999)
    print(time_tuple)
    # mktime根据时间元组转化为新纪元后的秒数，于localtime功能相反
    time_sec = time.mktime(time_tuple)
    print(time_sec)  # 19999.0
    # sleep让解释器等待指定的秒数
    time.sleep(5)
    print('Time out')


# test_time()


def test_random():
    '''
    5、random包含生成位随机数的函数，如要真正随机的数应使用os模块中的urandom，
    random模块中的SystenRandom类基于的功能和urandom类似

    '''
    import random, time
    start_date = time.mktime((2016, 1, 1, 0, 0, 0, -1, -1, -1))
    end_date = time.mktime((2017, 1, 1, 0, 0, 0, -1, -1, -1))
    # uniform从a-b随机去一个数
    random_time = random.uniform(start_date, end_date)
    print(time.asctime(time.localtime(random_time)))
    # random返回一个0-1的随机实数
    print(random.random())
    # getrandbits(n)以长整数的方式返回n个随机二进制位
    print(random.getrandbits(3))
    # randrange(start,stop,step)从range(start,end,step)中随机选取一个数
    print(random.randrange(4, 9, 2))
    # choice(seq)从序列seq中随机选取一个数
    print(random.choice([12, 34, 56, 67, 87]))
    # shuffle(seq) 就地打乱序列seq
    print(random.shuffle([12, 234, 34, 45, 56, 23]))
    # sample(seq,n)从序列seq中随机地选择n个值不同的元素
    print(random.sample([11, 11, 11, 1, 23, 54, 546, 23, 11, 23, 34, 456], 3))


# test_random()


def test_shelve_json():
    '''
    6、shelve模块用于储存数据，其关键函数是open和close，open方法接收一个文件名，
    返回一个一个非普通映射,对映射中的序列操作必须重新保存，否则序列并没有改变

    '''
    import shelve
    s = shelve.open('test.dat')
    s['name'] = 'perry'
    s['age'] = 22
    s['sex'] = 'man'
    s['hobby'] = ['ping-pong', 'swimming', 'study']
    s['hobby'].append('reading')  # 并没有保存进去
    print(s['hobby'])
    # 必须得重新保存
    lst = s['hobby']
    lst.append('reading')
    s['hobby'] = lst
    print(s['hobby'])


test_shelve_json()


def test_shelve():
    '''
    一个简单的使用shelve保存数据的实例
    '''
    import shelve
    class User:

        def __init__(self):
            self.__db = shelve.open('database.dat')

        def store_person(self):
            try:
                pid = input('Enter unique ID number:')
                person = {}
                person['name'] = input('Enter name:')
                person['age'] = int(input('enter age:'))
                person['phone'] = input('Enter phone number:')
                self.__db[pid] = person

            except Exception:
                pass

        def lookup_person(self):
            pid = input('Enter ID number:')
            field = input('What wonld you want to know?(name,age,phone)')
            field = field.strip().lower()
            print(field.capitalize() + ':' + self.__db[pid][field])

        def print_help(self):
            print('The available commands are: ')
            print('store:Stores information about a person')
            print('lookup:Looks up a person from ID number ')
            print('quit:Save changes and exit')
            print('?:Prints this message')

        def __enter_command(self):
            cmd = input('Enter command(? for help):')
            cmd = cmd.strip().lower()
            return cmd

        def run(self):
            try:
                while True:
                    cmd = self.__enter_command()
                    if cmd == 'store':
                        self.store_person()
                    elif cmd == 'lookup':
                        self.lookup_person()
                    elif cmd == '?':
                        self.print_help()
                    elif cmd == 'quit':
                        return
            finally:
                self.__db.close()

    user=User()
    user.run()


test_shelve()