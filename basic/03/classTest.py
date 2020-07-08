import sys

class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        print(self.x + self.y)
    def min(self):
        print(self.x - self.y)
    def mul(self):
        print(self.x * self.y)
    def div(self):
        print(self.x / self.y)

class FourCalculator(Calculator):
    def pow(self):
        print(self.x ** self.y)
    def div(self):
        if self.y == 0:
            return 0
        else:
            print(self.x / self.y)

cal = FourCalculator(10, 0)
while True:
    choice = input("***: ")
    if choice == "add":
        cal.add()
    elif choice == "min":
        cal.min()
    elif choice == "mul":
        cal.mul()
    elif choice == "div":
        cal.div()
    elif choice == "pow":
        cal.pow()
    else:
        print("No")
