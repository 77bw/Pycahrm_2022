class Dog:
    d_type = "京巴" # 属性，类属性，类变量， 公共属性
    sss = "sss" # 属性，类属性，类变量

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
Dog.say_hi(d)

d.say_hi() # 实例.方法
d2.say_hi() # d2.sayhi(d2)
print(d2)

d.sex = "母狗"
print(d.sex)



