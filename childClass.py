from Basics import OopsDemo
from Basics.OopsDemo import Abc


class ChildIpm(Abc):
    num1 = 20

    def __init__(self):
        Abc.__init__(self, 5, 4)

    def getdata(self):
        return self.num1 + self.num + self.firstNumber + self.secondNumber


obj2 = ChildIpm()
print(obj2.num1)
print(obj2.getdata())
