import threading
import random
import json

#단어 사전
word = {1:"one", 2:"two", 3:"three", 4:"four", 5:"five"}
#타이머
def clock():
    print("time out")

def game():
    tic = 1
    point = 5
    input("엔터")
    threading.Timer(10, clock).start()
    while tic == 1 and point > 0:
        quiz = random.choice(word)
        print("문제 : ", quiz)
        ans = input()
        if quiz == ans:
            print("정답 point :", point)
            point += 1
        else:
            print("오답 point :", point)
            point -= 1
    print("게임 종료 point :", point)

jsonString = json.dumps(word)
while True:
    print("1.타자게임 | 2. 문제불러오기 | 3.문제저장하기 | 4.문제 등록 | 5.등수 | 6.종료하기")
    menu = input("선택 >> ")
    if menu == '1':
        game()
    elif menu == '2':
        with open('./basic/02_if_for/data.json', 'rt') as f:
            word = json.load(f)
            print(word)
    elif menu == '3':
        with open('./basic/02_if_for/data.json', 'wt') as f:
            json.dump(word, f, indent=4)

    elif menu == '4':
        pass
    elif menu == '5':
        pass
    elif menu == '6':
        print("종료")
        break
    else:
        print("올바른 번호가 아닙니다")