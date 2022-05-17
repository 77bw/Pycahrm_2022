# -*- encoding:utf-8 -*-

class Base(object):
    def fight(self):
        print("..到了天地界限....")

class ShenXianBase(Base):
    pass
    # def fight(self):
    #     print("神仙祖宗在打架....")
    #

class MonkeyBase():

    def fight(self):
        print("猿猴在打架....")


class ShenXian(ShenXianBase):
    """神仙类"""
    def fly(self):
        print("神仙都会飞...")
    #
    # def fight(self):
    #     print("神仙在打架...")

class Monkey(MonkeyBase):
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")

    def fight(self):
        print("猴子在打架...")

class MonkeyKing(ShenXian,Monkey):

    def play_goden_stick(self):
        print("孙悟空玩金箍棒...")


sxz = MonkeyKing()
# sxz.eat_peach()
# sxz.fly()
# sxz.play_goden_stick()

sxz.fight()



class A: # 经典类
    pass

class B(object): # 新式类
    pass

print(MonkeyKing.__mro__)