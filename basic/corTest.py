def test1(i):
    print('start test1 coroutine')
    while True:
        print(i)
        yield i
        i += 1

def test2(i):
    print("start test2 coroutine")
    while True:
        value = yield i
        i += value
        print(i)

b = test2(5)
next(b)
b.send(3)
b.send(5)