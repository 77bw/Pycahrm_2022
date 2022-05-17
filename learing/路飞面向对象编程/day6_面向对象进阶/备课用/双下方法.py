#
#
# class A:
#     def __len__(self):
#         print(666)
#         return 3
#
# a = A() # len 一个对象就会触发 __len__方法。
# print(len(a))
#
#
# class B:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def __len__(self):
#         return len(self.__dict__)
# b = B()
# print(len(b))


# hash
# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#     def __hash__(self):
#         print("hash method.")
#         return hash(str(self.a)+str(self.b))
# a = A()
# print(hash(a))

# class A:
#     def __init__(self):
#         self.a = 1
#         self.b = 2
#
#     def __eq__(self,obj):
#         print("call eq method.")
#         if  self.a == obj.a and self.b == obj.b:
#             return True
# a = A()
# b = A()
# print(a == b)



# class Brand:
#     def __init__(self,name):
#         self.name=name
#
#     def __getitem__(self, item):
#         print("获取KEY",item)
#         print(self.__dict__[item])
#
#     def __setitem__(self, key, value):
#         print("设置一个key...",key)
#         self.__dict__[key]=value
#
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
#
#     def __delattr__(self, item):
#         print('del obj.key时,我执行')
#         self.__dict__.pop(item)
#
#
# b=Brand('小猿圈')
# b["slogan"] = "自学编程谁不爱小猿圈"
# b["website"] = "apeland.cn"
#
# del b["website"]
#
# b['name']='小猿圈Apeland'
#
# b["name"]  # 获取KEY
# print(b.__dict__)


#
# class School:
#     def __init__(self,name,addr,type):
#         self.name = name
#         self.addr = addr
#         self.type = type
#
#     def __repr__(self):
#         return 'School(%s,%s)' %(self.name,self.addr)
#
#     def __str__(self):
#         return '(%s,%s)' %(self.name,self.addr)
#
#
#
# s1=School('小猿圈','北京','私立')
# print('from repr: ',repr(s1))
# print('from str: ',str(s1))
# print(s1)
#
# '''
# str函数或者print函数调用时--->obj.__str__()
# repr或者交互式解释器中调用时--->obj.__repr__()
# 如果__str__没有被定义,那么就会使用__repr__来代替输出
# 注意:这俩方法的返回值必须是字符串,否则抛出异常
# '''

class Foo:

    def __del__(self):
        print('执行我啦')

f1=Foo()
del f1
print('------->')