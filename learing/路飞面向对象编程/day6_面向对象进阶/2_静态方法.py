"""
静态方法就相当于普通方法，没加self本身之前,访问不了实例变量跟类变量
举个例子：就像富家子弟被移除家庭，但是家里人过世，还是可以带着身份信息来瓜分财产。
也就相当于静态方法也可以加self来访问实例变量跟类变量
"""



class Student(object):
    role = "Stu"

    def __init__(self,name):
        self.name = name

    @staticmethod
    def fly(self):
        print(self.name,"is flying...")

    @staticmethod
    def walk(self):
        print("student walking...")

    @staticmethod
    def run():
        print("student is runing")


s = Student("Jack")
s.fly(s) # s.fly(s)
s.walk(s)
s.run()