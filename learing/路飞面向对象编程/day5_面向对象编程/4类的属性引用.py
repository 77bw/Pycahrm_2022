

class Dog:
    d_type = "京巴" # 属性，类属性，类变量， 公共属性

    def __init__(self,name,age,sex): # 初始化方法，构造方法，构造函数，实例化时会自动执行，进行一些初始化工作。
        print('hahhah',name,age)
        self.sex = sex # d.sex = sex
        # 要想把name, age这2个值 ，真正的存到实例里。那就要把2个值 跟实例绑定
        self.name2 = name # 绑定参数值 到实例 d2.name2 = name
        self.age2 = age

    def say_hi(self): # 方法 ，第一个参数，必须是self,  self 代表实例本身..
        print("hello ,i am a dog, my type is ",self.d_type, self.name2 )


d = Dog("mjj",3,"公狗") # 生成了一个实例
d2 = Dog("毛蛋",2,"母狗") # 生成了一个实例



class People:

    nationality = "TW" #重复的字段提出来

    def __init__(self,name,age,sex,nationality):
        self.name = name
        self.age = age
        self.sex = sex
        self.nationality=nationality



p = People("Mjj",22,"M")
# p2 = People("Alex",23,"M")
# p3 = People("Jack",25,"F")
print(p.nationality)   # 寻找属性会先在当前对象中寻找是否含有该属性，如果没有在到当前对象的类对象中去寻找，如果有则返回类对象的属性值，没有则报错

People.nationality = "CN"  #修改公共属性  如果这个属性（方法）是所有的实例共享的，则应该将其保存到类对象中

print(p.nationality)
#
# p.nationality = "JP"  # 相当于，给p实例创建了一个新实例属性，自己改了国籍，是否可以？
#
# print(p.nationality)
print(People.nationality)




# print(Dog.d_type)
#
#
# Dog.d_type = "金毛"
#
#
# print(d.d_type)
# print(d2.d_type)

# print(d.name2)
# d.name2 = "马JJ"
# print(d.name2)
# print(Dog.name2)  #错误，Dog类没有绑定name2属性，该属性实在对象上的


