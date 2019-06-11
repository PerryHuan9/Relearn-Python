
class Student:
    class Descriptor:
        def __get__(self, instance, owner):
            print(self, instance, owner, sep='\n')
            return instance.name
        
        def __set__(*arg):
            '''构建只读属性，赋值时抛出错误'''
            raise AttributeError('can not set')
        
        def __delete__(self, instance):
            del instance.name
    
    class Group:
        def __init__(self, group):
            self.group = group
        def __get__(self, *arg):
            return self.group

        def __set__(self,instance,group):
            self.group = group
        
        def __delete__(self, instance):
            del self.group


    group = Group('码隆')
    id = Descriptor()

    def __init__(self):
        self.__name = 'perry'
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @name.deleter
    def name(self):
        del self.__name
    



s = Student()
print(s.name)
s.name = 'huangyilin'
print(s.name)
print(s.id)
# Student.id
# s.id = 'niaho'
# print(s.id)
# del s.id
# print(s.id)
print(Student.group)
print(s.group)



class Property:
    '''
        使用描述符实现property特性
    '''
    def __init__(self, fget=None, fset=None, fdel=None, fdoc=None):
        print('初始化' , fget)
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        self.fdoc = fdoc
    
    def __call__(self, *arg):
        print('__call__')
        return self
    
    def setter(self, fset):
        self.fset = fset
        return self
    
    def deleter(self, fdel):
        self.fdel = fdel
        return  self
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.fget is None:
            raise AttributeError('can not get attribuate')
        return self.fget(instance)


    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError('can not set attribuate')
        print('setter:', value)
        self.fset(instance, value)


    def __delete__(self, instance,):
        if self.fdel is None:
            raise AttributeError("can't del attribuate")
        self.fdel(instance)
    

class Persion:
    def __init__(self):
        self._name = None
        self._age = 0
    
    def getName(self):
        return self._name
    
    def setName(self, name):
        self._name = name
    
    def delName(self):
        del self._name
    
    name = Property(getName, setName, delName)

    @Property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        self._age = value
    
    @age.deleter
    def age(self):
        del self._age


p = Persion()
p.name = 'huangyilin'
print(p.name)
del p.name
print(p.age)
p.age = 88
print(p.age)



    

























