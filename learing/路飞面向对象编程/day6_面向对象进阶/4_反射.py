"""
映射、反射、自省  说白了其操作就是绑定，绑定属性或者方法
可以通过字符串的形式来操作对象的属性

__name__  在当前模块主动执行的情况下(不是被导入执行)，等于__mian__
          在被其他模块导入执行的情况下，模块名
"""

class Person():
    def __init__(self ,name ,age):
        self.name = name
        self.age = age

    def walk(self):
        print("walking....")

    def getinfo(self):
        print(self.name,self.age)

def talk(self):
    print(self.name ,"is speaking.....")

p = Person("Alex" ,22)
if hasattr(p,"name"): # 映射
    print("l.......")

# if __name__ == '__main__':

# #反射、映射、自省
    # getattr() get 获取
    # a = getattr(p,"age")
    # print(a)

# hasattr() 判断
#     user_command = input(">>:").strip()
#     if hasattr(p,user_command):
#         func = getattr(p,user_command)   #可以判断p对象的属性跟方法，记住方法传的只是方法名
#         func()

# setattr()  赋值
#     ## static 属性
#     setattr(p,"sex","Female")
#     print(p.sex)

#     ## 方法
#    "spaek"为自定义名字，talk为要绑定到p实例对象上的方法
#     setattr(p,"speak",talk)
#     p.speak(p)  #调用这个的时候要传入参数实例本身

    #   ”speak2“为自定义方法的名字,将方法talk绑定到类Person上
#     setattr(Person,"speak2",talk)
#     p.speak2()  #这样子就可以直接绑定

# delattr()  删除

#delattr(p,"age")
# del p.age
# p.age

#getattr("4_反射.py","p")

# print(__name__) # __main__ 就代表模块本身， self.
#
# if __name__ == "__main__": #只会在被别的模块导入的时候发挥作用
#     print("hahahah")
#
# #print('hahaha')

#
import sys
# # for k,v in sys.modules.items():
# #     print(k,v)
#
#print(sys.modules["__main__"])
mod = sys.modules[__name__]
if hasattr(mod,"p"):
    o = getattr(mod,"p")
    print(o)
print(p)
#
# #import "os"

# class User:
#     def login(self):
#         print('欢迎来到登录页面')
#     def register(self):
#         print('欢迎来到注册页面')
#     def save(self):
#         print('欢迎来到存储页面')
#
# u = User()
# while True:
#     user_cmd = input(">>:").strip()
#     if hasattr(u,user_cmd):
#         func = getattr(u,user_cmd)
#         func()