
class E:
    def tell(self):
        print("From E")

class G(E):
    def tell(self):
        print("From G")
class B:
    def tell(self):
        print("From B")

class F(G):
    def tell(self):
        print("From F")


class D:
    def tell(self):
        print("From D")

class C(B):
    def tell(self):
        print("C")


class A(C,D,F):
    pass

a = A()
a.tell()
print(A.__mro__)

