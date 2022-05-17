class Person:
    def __init__(self,name,age,sex):

        self.name = name
        self.age = age
        self.sex = sex
        self.partner = None # 另一半，是个对象

    def do_private_stuff(self):
        """和男/女盆友干点羞羞的事"""
        print("%s is doing %s in the 7th hotel." %(self.name,self.partner.name))


p1 = Person("武大郎",25,"男")
p2 = Person("黑姑娘",23,"女")

p1.partner = p2 # 两个对象要互相绑定彼此
p2.partner = p1

p1.do_private_stuff()
p2.do_private_stuff()

