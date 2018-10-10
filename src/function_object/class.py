# Python中的类

# 1、类中的方法的第一个参数总是对象
# 2、私有方法和属性以双下划线开头，外界无法访问，
# 实际上其是对类中的双下划线开头的方法的名称进行了转换，在其前面加上了下划线和类名，
# 无法禁止别人访问私有变量方法，但这个已经是一个强烈的信号
# 通常还有一种约定，约定私有方法和属性以单下划线开头，但这个只是约定，
# 不过导模块时 from module import * 会自动忽略以下划线开头的名称
# 3、在class语句中定义的代码都是在一个特殊的命名空间（类的命名空间）内执行的，
# 而类的所有成员都可以访问这个命名空间。类定义其实就是要执行的代码段


class Person:
    ' 类作用域的变量，所有的对象都可以访问，并且所有对象访问的都是同一个变量'
    # 类级变量，在class调用它时初始化，如果在创建对象之前没有访问过它，那么在第一个对象创建时访问它
    self_variate = '我是变量'
    # 下面语句在该类对象第一次被创建时执行，之后再创建对象不会执行，因为其已经存在
    print('类定义代码开始执行')
    # 私有属性以双下划线开头，外界无法访问
    __private_variate = '我是私有属性'

    def get_private_variate(self):
        self.__private_method()
        return self.__private_variate

    def __private_method(self):
        '私有方法以双下划线开头，外部无法访问'
        print('我是私有方法')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("Hello,word! I'm {}".format(self.name))

    def variate_introduce(self):
        print(self.self_variate)


foo = Person()
bar = Person()
foo.set_name('Perry Huang')
bar.set_name('黄益凛')
foo.greet()
bar.greet()
foo.name = 'Perry'
foo.greet()
print(foo.self_variate)  # 我是变量
print(Person.self_variate)  # 我是变量

# 方法有没有self并不取决与使用obj.method()调用，而是是否与关联
greet = foo.greet
greet()  # 这样也能拥有self

# 无法访问私有属性和方法
print(bar.get_private_variate())
# 事实上类只是将私有方法和属性对外换了一个名字，
# 像下面就可以访问到私有方法和属性，但我决不应该这样做
print(bar._Person__private_variate)

# 如果对类级变量赋值会怎样,只会在该对象上加入一个新的同名属性，该属性遮住了类级同名变量
bar.self_variate = '我将会成为对象的新属性'
print(bar.self_variate)  # '我将会成为对象的新属性'
print(foo.self_variate)  # 我是变量
# 要想修改类级变量只能通过类来修改
Person.self_variate = '直接通过类来修改'
print(foo.self_variate)
