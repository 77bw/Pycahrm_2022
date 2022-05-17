# class Dog(object):
#     name = "我是类变量"
#     def __init__(self, name):
#         self.name = name
#
#     @classmethod
#     def eat(self):
#         print("%s is eating" % self.name)
#
#
# d = Dog("Mjj")
# d.eat()












class Student(object):

    __stu_num = 0  # 学员计数需存在类变量里，不能存在每个实例里

    def __init__(self,name):
        self.name = name
        self.add_stu_num() # 相当于Student.add_stu_num() 初始化学员时调用

    @classmethod
    def add_stu_num(cls): # 注意这里调用时传进来的其实是类本身，不是实例本身，所以参数名一般改为cls
        cls.__stu_num += 1
        print("total student num:",cls.__stu_num)


s1 = Student("张1")
s2 = Student("张2")
s3 = Student("张3")
s4 = Student("张4")


Student.add_stu_num() # 也可以这样调

