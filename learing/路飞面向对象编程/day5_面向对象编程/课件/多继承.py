

class ShenXian:
    """神仙类"""
    def fly(self):
        print("神仙都会飞...")

class Monkey:
    def eat_peach(self):
        print("猴子都喜欢吃桃子...")


class MonkeyKing(ShenXian,Monkey):

    def play_goden_stick(self):
        print("孙悟空玩金箍棒...")


sxz = MonkeyKing()
sxz.eat_peach()
sxz.fly()
sxz.play_goden_stick()

