

class Student(object):

    stu_num = 0
    def __init__(self,name):
        self.name = name


    @staticmethod
    def fly():
        print("%s is flying..." )



s = Student("Mjj")
# s.fly(s)
s.fly()