import random
import time

cnt = 0
input("게임 시작")
start = time.time()

for i in range(1, 4):
    c = random.choice(["+", "-", "//", "*"])
    if c is '*':
        a, b = random.randint(2,10), random.randint(2,10)
    else:
        a, b = random.randint(1,50), random.randint(1,50)
    print(a," ",c," ",b," =")
    num = int(input())
    ans = eval(str(a)+c+str(b))
    if num == ans:
        print("정답!")
        cnt += 1
    else:
        print("오답")
        print("정답은",ans)
end = time.time()
print(cnt, "개 맞음")
print("걸린 시간 : ",round(end-start, 2))
