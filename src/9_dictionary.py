# Python中唯一的内置映射（mapping）类型


# 1、创建字典
# 可直接创建，或者使用dist函数从其他映射或键值对序列创建字典
def test_1():
    # 直接创建字典
    dictionary = {'name': 'perry', 'age': 22, 'gender': 'man'}
    print(dictionary)
    # 使用dist函数转化键值对序列,该序列必须为二维
    dic = dict([['name', '黄益凛'], ['age', 22]])
    print(dic)
    dic = dict([('name', '黄益威'), ('age', '24')])
    print(dic)
    # 使用关键字实参来调用dict函数
    dic = dict(key=888, value=999)
    print(dic)


test_1()


# 字典的基本操作和序列类似


# 2、将字符串格式用于字典
def test_2():
    name = 'perry'
    user = {'name': name, 'age': 22}
    info = "{name} is {age} old.".format_map(user)
    print(info)


test_2()

# 3、字典方法
# (1)clear 用于删除所有的字典项
# (2)copy 返回一个新字典，执行浅复制，
# 替换值时不会影响到原件，但修改值时会反映到原件，比如修改序列值时，所有的原副件都会被修改
# 可以进行深复制，使用deepcopy()内置函数
# (3)fromkeys,传入一个列表，列表的元素都作为字典的键，值都未None,还可指定默认值为第二参数,
# 只能用于创建字典,使用空字典调用它，事实上，字典的创建一般使用dict内置函数
# (4)
#
#
#
#
#
#
#
#
#
#
#
#
#


