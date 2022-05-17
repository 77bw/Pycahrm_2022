


# class Student(object):
#
#     def __init__(self,name):
#         self.name = name
#         print('init hhaha')
#
#     def __new__(cls, *args, **kwargs):
#         # 负责执行__init__, 进行一些实例初始化前的工作
#         print(cls,args,kwargs)
#
#         return object.__new__(cls)
#         return super().__new__(cls)
#
# p = Student("Alex")
# p.name

# 设计 模式 23 gof 单例


class Printer(object):
    tasks = []
    instance = None  # 存放第一个实例对象
    def __init__(self,name):
        self.name = name

    def add_task(self,job):
        self.tasks.append(job)
        print("[%s] 添加任务[%s]到打印机,总任务数[%s]" %(self.name,job,len(self.tasks)))

    def __new__(cls, *args, **kwargs):
        #只有第一次实例化的时候，正常进行， 后面每次实例化，并不真正创建一个新实例
        if cls.instance is None: #
            #进行正常的实例化， 并把实例化后的对象 存在cls.instance里
            obj = object.__new__(cls) # 实例化过程
            print("obj",obj)
            cls.instance = obj # 把实例化好的对象存下来
        return cls.instance #以后的每次实例化，直接返回第一次存的实例对象   object.__new__(cls).instance
                #在上一次实例对象的基础上，再执行__Init__


p1 = Printer("Word app")
p2 = Printer("pdf app")
p3 = Printer("excel app")

p1.add_task("word file")
p2.add_task("pdf file")
p3.add_task("excel file")

print(p1,p2,p3)
print(p1.name,p2.name)