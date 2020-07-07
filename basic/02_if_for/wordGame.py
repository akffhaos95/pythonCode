import threading
import random
import json
import rank
import quiz

word = {}
#타이머
tic = 1
def clock():
    global tic
    tic = 0
    print("Time Out")

def game():
    global tic
    tic = 1
    point = 5
    input("Press Enter to start")
    t = threading.Timer(5, clock)
    t.start()
    while tic == 1 and point > 0:
        quizRan = random.choice(list(word.values()))
        print("문제 : ", quizRan)
        ans = input()
        if quizRan == ans:
            point += 1
            print("정답 point :", point)
        else:
            point -= 1
            print("오답 point :", point)
    print("게임 종료 point :", point)
    t.cancel()
    return point

jsonString = json.dumps(word)
while True:
    print("1.타자게임 | 2. 문제불러오기 | 3.문제저장하기 | 4.문제 등록 | 5.등수 | 6.종료하기")
    menu = input("선택 >> ")
    #타자 게임
    #1. 타이머 10초 시작, 포인트 5점으로 시작
    #2. 단어사전 랜덤으로 퀴즈 (맞추면 +1, 틀리면 -1)
    #3. 포인트 0점 or 시간 다 되면 종료
    #4. 포인트 0점으로 끝났을 시 이름 저장하지 않고 "Game Over"
    #5. 시간 종료시에 이름 저장후 JSON 랭킹에 저장
    if menu == '1':
        if not word:
            print("문제를 불러와주세요")
        else:
            point = game() #2    
            if point != 0:
                name = input("이름을 입력하세요 : ")
                rank.insertRank(name, point) #5
            else:
                print("Game Over")
    #문제 불러오기
    elif menu == '2':
        word = quiz.loadQuiz()
        print(word)
    #문제 저장하기
    elif menu == '3':
        quiz.saveQuiz()
    #문제 등록
    elif menu == '4':
        quizIns = input("문제로 낼 단어를 입력해주세요 : ")
        quiz.insertQuiz(quizIns)
    #등수
    elif menu == '5':
        #rank.json의 파일을 정렬하여 상위 3개만 출력
        rank.loadRank()
    #종료하기
    elif menu == '6':
        print("종료")
        break
    else:
        print("올바른 번호가 아닙니다")