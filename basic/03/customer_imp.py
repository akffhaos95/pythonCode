import re
import cust
custlist=[{'name': 'asdf', 'gender': 'F', 'email': 'asdf123@naver.com', 'birthyear': '1923'}]
page=0

while True:
    choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''')
    exe(choice, page)