

class Person(object):
    def __init__(self,name):
        self.name = name
        print("--init ....")

    def __new__(cls, *args, **kwargs):
        """
        cls  : 代表Person这个类本身
        :param args:
        :param kwargs:
        :return:
        """
        print("--in new: ",cls,*args,**kwargs)

        return object.__new__(cls)  # 调用父类的__new__方法，必须这么干 ，要不然__init__方法就不会执行了

    def __call__(self, *args, **kwargs):
        print("-->call",self,*args,**kwargs)


p = Person("Alex")

p()  # 此时会执行__call__



# class Printer(object):
#     __instance = None # 用来存唯一的一个实例
#     __tasks = []
#
#     def __init__(self,task):
#         self.__tasks.append(task)
#         print("added a new task in queue..",task)
#
#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None: # 代表之前还没被实例化过
#             obj = object.__new__(cls)
#             cls.__instance = obj  # 把第一次实例化的对象 存下来，以后每次实例化都用这个第一次的对象
#         return cls.__instance  # 下一次实例化时，就返回第一次实例化的对象
#
#     def jobs(self):
#         return self.__tasks
#
# job = Printer("job1 word")
# job2 = Printer("job2 png")
# job3 = Printer("job3 excel")
# print(id(job),id(job2),id(job3)) # 会发现这3个实例的内存id一样
# print(job3.jobs())