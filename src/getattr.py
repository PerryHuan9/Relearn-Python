# -*— coding=utf-8 -*-
# 测试getattr,setattr,delattr和getattribute


class Attr:
    field = 888
    def __init__(self, value):
        self._test = value

    def __getattr__(self, name):
        '''
            该函数只有在对象访问属性触发AttribuateError时被调用，仅对对象属性生效，
            在类属性在被访问时即便触发AttribuateError也不会调用
        '''
        if name == 'test':
            print('__getattr__:', name)
            return self._test
        else:
            raise AttributeError('the `{}` field is Undefined.'.format(name))
    

    def __setattr__(self, name, value):
        if name == 'test':
            print('setattr:', name, value)
            name = '_test'
        self.__dict__[name] = value
    

    def __delattr__(self, name):
        if name == 'test':
            name = '_test'
            print('delattr:', name)
        del self.__dict__[name]
    

    def fit_dog(self):
        print("喂狗",)
        


attr = Attr('perry huang ')
print(attr.test)
attr.test = '黄益凛'
print(attr.test)
attr.perry = 'huang'
print(attr.perry)
del attr.perry
del attr.test


class Attr2:
    '''
    使用__getattribuate__替代__getattr__
    '''
    def __init__(self):
        self._name = 'perry'
    
    def __getattribute__(self, attr):
        print('__getattribuate__: 被调用')
        if attr == 'name':
            attr = '_name'
        return object.__getattribute__(self, attr)
    
    def __setattr__(self, attr, value):
        if attr == 'name':
            print('__setattr__:', attr)
            attr = '_name'
        object.__setattr__(self, attr, value)
    
    def __delattr__(self, attr):
        if attr == 'name':
            print('__delattr__:', attr)
            attr = '_name'
        del self.__dict__[attr]


a = Attr2()
print(a.name)
a.name = '你好，明天!'
print(a.name)

    

    










