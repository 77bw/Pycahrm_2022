
import sys


def s1():
    print('s1')


class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age

name = "test"



this_module = sys.modules[__name__] # __name__ 会动态的代表当前模块名

print(hasattr(this_module, 's1'))
print(hasattr(this_module, 'name'))
print(getattr(this_module, 'Person'))

p = getattr(this_module, 'Person')
p("Alex",22)


#
#
# class Person(object):
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def say_hi(self):
#         print("hi,guys , my name is " ,self.name)
#
# obj=Person('Alex',26)
#
# #检测是否含有某属性
# print(hasattr(obj,'name'))
# print(hasattr(obj,'say_hi'))
#
# #获取属性
# n=getattr(obj,'name')
# print(n)
# func=getattr(obj,'say_hi')
# func()
#
# print(getattr(obj,'aaaaaaaa','不存在啊')) #报错
#
# #设置属性
# setattr(obj,'hobbie',"girl")
# setattr(obj,'show_name',lambda self:self.name+'--%s' % self.age)
# print(obj.__dict__)
# print(obj.show_name(obj))
#
# #删除属性
# delattr(obj,'age')
# delattr(obj,'show_name')
# #delattr(obj,'show_name111') # 不存在,则报错
#
# print(obj.__dict__)
#
#
# class Person(object):
#     staticField = "Chinese"
#
#     def __init__(self):
#         self.name = 'alex'
#
#     def func(self):
#         return 'func'
#
#     @staticmethod
#     def bar():
#         return 'bar'
#
#
# print(getattr(Person, 'staticField'))
# print(getattr(Person, 'func'))
# print(getattr(Person, 'bar'))