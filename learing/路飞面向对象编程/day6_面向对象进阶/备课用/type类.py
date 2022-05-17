

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

p = Person("Alex",22)


def __init__(self,name,age):
    self.name = name
    self.age = age
    print("init. ", name,age)

Person2 = type("Person2",(object,),{"__init__":__init__})
# Person2 第一参数是类名
# (object,) 是这个类要继承的类
# {"__init__":__init__}是这个类的方法


p = Person2("Alex",22)
print(type(Person2))







