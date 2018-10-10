# Python通过引入模块abc提供了抽象基类的支持
from abc import ABC, abstractmethod


class Talker(ABC):
    '抽象类无法实例化，只能通过继承使用'

    @abstractmethod
    def talk(self):
        pass


class Knigget(Talker):
    '如果继承抽象类的类没有实现抽象类的方法，那么它也是抽象类，无法被实例化'
    pass


class Person(Talker):
    def talk(self):
        print('A human talk.')


# t=Talker() #报错，无法被实例化
# k=Knigget() #报错，无法被实例化
p = Person()
p.talk()
print(isinstance(p, Person))  # True
print(isinstance(p, Talker))  # True


# 对于实现该接口但不是该子类的类，需要使用register
class Herring:
    def talk(self):
        print('Herring也实现Talker抽象类的接口，但没有继承Talker抽象类')


h = Herring()
print('注册前：', isinstance(h, Talker))  # False
Talker.register(Herring)
print('注册后：', isinstance(h, Talker))


# 但这样有一个缺点，抽象基类提供的保障没有了，
# 即不会检查注册的类是否实现了接口，只有到使用的时候才发现其可能不存在该方法
class Clam:
    pass


Talker.register(Clam)
c = Clam()
# c.talk()
