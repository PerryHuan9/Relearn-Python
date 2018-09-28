# 用户输入语句


def test1():
    str = input('请输入一段信息：')
    print('你输入的信息为：', str)


# test1()

# 对输入的数字进行强制转化，转为整数或浮点数
def test2():
    int1 = input('请输入一个整数:')
    f1 = input('请输入一个浮点数:')
    c = int(int1) + float(f1)
    print(int1, '+', f1, '=', c)


test2()
