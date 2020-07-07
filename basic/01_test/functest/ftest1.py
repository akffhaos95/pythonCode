class Test():
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
        print("make")
    
    def test(self):
        print(self._a+self._b+self._c)

if __name__=="__main__":
    claTest = Test(1,2,3)
    