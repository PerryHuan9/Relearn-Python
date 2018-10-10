def print_hello():
    print('Hello,word')


# 为了避免在外部程序导入这个包的时候执行测试代码。需要添加条件判断

if __name__ == '__main__':
    # 测试代码
    print_hello()
    print(__name__)
