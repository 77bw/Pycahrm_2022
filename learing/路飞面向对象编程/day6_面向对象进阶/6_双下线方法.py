#
#
# class Person():
#     def __init__(self ,name ,age):
#         self.name = name
#         self.age = age
#
#     def __len__(self):
#         print("trigger....")
#         return 2
#
#     def __hash__(self):
#         print("hash....")
#         return 22222
#
#     def __eq__(self, other):
#         print(self.name,other.name)

# p = Person("alex",22)
# p2 = Person("jack",22)
# # len(p)

# print(p==p2)

# hash(p)
# print(hash(p))

class Brand:
    def __init__(self,name):
        self.name=name

    def __getitem__(self, item):
        print('---get item...',self.__dict__[item])

        #print(self.__dict__)

    def __setitem__(self, key, value):
        print("set item")
        self.__dict__[key] = value

    def __delitem__(self, key):
        print("__del...")

    def __delattr__(self, item):
        print('del obj.key时,我执行')
        self.__dict__.pop(item)



b = Brand("小猿圈")
b["name"]
#
# b["website"] = "www.apeland.cn"
# b["website"] = "https://www.apeland.cn"
# print(b.website)
#
# del b["name"]
#
# del b.name