

class Dog:  # 类名首字母要大写，驼峰体

    d_type = "京巴"  # 公共属性，又称类变量

    def __init__(self,name,age,master): # 初始化函数，只要一实例化，就会自动执行
        print('初始化这个实例....',name)
        self.name = name  # self.name 就是实例自己的变量
        self.age = age
        self.master = master

    def say_hi(self):  # 类的方法，必须带一个self参数，代表实例本身，具体先不解释
        print("hello , I am a dog,my type is ",self.d_type,self.name) # 想调用类里的属性，都要加上self., 原因先不表


# d = Dog("毛毛",2,"Alex")  # 生成一个狗的实例
d2 = Dog("二蛋",3,"Jack")  # 生成一个狗的实例



d2.say_hi() # 调用狗这个类的方法
print(d2.name, d2.age, d2.master) # 调用实例的变量

print(d2.d_type) # 注意通过实例也可以调用类的公共属性
# print(d.d_type)  # 调用Dog类的公共属性

print(Dog.d_type) # 查看Dog的d_type属性
print(Dog.say_hi)  # 引用Dog的say_hi方法，注意只是引用，不是调用


