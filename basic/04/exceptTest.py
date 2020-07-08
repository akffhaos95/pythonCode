try:
    f = open("test.txt", "r" )
except FileNotFoundError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
finally:
    print("finally")