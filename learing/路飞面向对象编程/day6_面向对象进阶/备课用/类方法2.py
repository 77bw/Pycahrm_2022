#
#
# class Dog(object):
#     name = "stupid dog"
#     def __init__(self,name):
#         self.name = name
#
#     @classmethod
#     def __eat(self,food):
#         print(self)
#         print("dog %s is eating  %s...." % (self.name,food) )
#
#     @classmethod
#     def run(cls):
#         print(cls.name,"running..")
#
# d = Dog("mjj")
# d.__eat("bones")
# d.run()



class Student(object):

    __stu_num = 0
    def __init__(self,name):
        self.name = name
        #Student.stu_num += 1
        self.add_stu(self)

    @classmethod
    def add_stu(cls,obj):
        if obj.name:
            cls.__stu_num += 1
            print("new student join in , we have %s now" % cls.__stu_num)

s = Student("Alex")
s2 = Student("Mjj")
s3 = Student("Egon")

Student.add_stu()
