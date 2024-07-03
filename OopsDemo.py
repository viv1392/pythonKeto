class Abc:
    num = 120  # class variable or global variable;

    def __init__(self, u, v):
        self.firstNumber = u
        self.secondNumber = v
        print("it is in constructer")

    def xyz(self):
        print("I am inside the method")
        string = "hello vivek"  # instance or method variable
        print(string)

    def add(self, a, b, ):
        c = a+b
        print(c)

    def summation(self):
        return self.firstNumber + self.secondNumber + self.num


obj = Abc(30, 20)

obj.xyz()
obj.add(10,20)

obj1 = Abc(40, 50)
print(obj1.num)
obj1.xyz()
print(obj1.summation())



