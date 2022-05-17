
import abc
class Pay(object):

    @abc.abstractmethod
    def pay(self):
        """子类必须定义pay方法"""
        raise NotImplementedError

class AliPay(Pay):

    pass

a = AliPay()
a.pay()