class Calculate:
    c = 8           # class variable
    d = 9           # class variable

    def __init__(self):
        self.e = self.c * self.d   # 8 * 9 = 72
        print(self.e)

    def sum(self, a, b):
        print(a + b)

    def multi(self):
        self.x = 4
        self.y = 5
        print(self.x * self.y)

    def sub(self, p, q):
        print(p - q)

obj = Calculate()         # prints 72 (from constructor)
obj.sum(10, 20)           # prints 30
obj.sub(50, 10)           # prints 40
obj.multi()               # prints 20

print(obj.c + obj.d)      # prints 17 (8 + 9)
#Above can also be written as
print(Calculate.c + Calculate.d)
