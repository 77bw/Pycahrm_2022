"""
类方法只能访问类变量，访问不了实例变量
why？
    因为self这个参数接受的不是实例本身，而是类本身

"""

#
# class Dog(object):
#
#     name = "stupid dog"
#
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def eat(self):
#         print("-->",self)
#         print("dog %s is eating..." % self.name)
#
#     @classmethod
#     def run(cls): # class
#         print(cls)


# d = Dog("Mjj")
# d.eat()
# print(Dog)
# d.run()

class Student(object):
    __stu_num = 0
    #name = 333
    def __init__(self,name):
        self.name = name
        #self.stu_num += 1 # 对实例进行赋值
        # Student.stu_num += 1 # 对类的变量进行赋值
        # print("生成了一个新学生,",name,self.stu_num)
        self.add_stu(self)

    @classmethod
    def add_stu(cls,obj): #obj stands for self instance
        if obj.name:
            cls.__stu_num += 1
            print("生成了一个新学生,",cls.__stu_num)


s1 = Student("Mjj")
s2 = Student("Jack")
s3 = Student("Alex")

Student.add_stu(Student)


# print(Student.stu_num)
# Student.stu_num += 1
# print(Student.stu_num)