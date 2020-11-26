class Calculator:
    def __init__(self, number1=0, number2=0):
        self.number1 = number1
        self.number2 = number2
    def add(self):
        print(self.number1 + self.number2)
    def diffirence(self):
        print(self.number1 - self.number2)
    def multiply(self):
        print(self.number1 * self.number2)
    def divide(self):
        print(self.number1 / self.number2)

class ScienceCalculator(Calculator):
    def powerTo(self):
        print(self.number1 ** self.number2)
    def noModulo(self):
        print(self.number1 // self.number2)
    def modulo(self):
        print(self.number1 % self.number2)
    def isSame(self):
        print(self.number1 == self.number2)