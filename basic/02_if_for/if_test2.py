#숫자를 입력받아서 짝수인지 홀수인지 판별
while True:
    num = input()
    if not num.isdecimal():
        print("숫자를 입력")
    elif int(num)%2==0:
        print("짝수")
        break
    else:
        print("홀수")
        break