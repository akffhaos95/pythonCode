# **콘솔형 고객 정보 관리 시스템 구축**
import re

custlist=[{'name': 'asdf', 'gender': 'F', 'email': 'asdf123@naver.com', 'birthyear': '1923'}]
page=0
n = re.compile('[a-zA-Z]{3,}')
e = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')

def name():
    while True: #이름 입력
        name = input("이름을 입력하세요 : ")
        if n.match(name):
            return name
        else:
            print("***올바른 이름을 입력***")
def gender():
    while True: #성별 입력
        gender = input("성별을 입력하세요 : ").upper()
        if gender in ("M", "F"):
            return gender
        else:
            print("***올바른 성별을 입력(M/F)***")
def email():
    while True: #이메일 입력
        email = input("이메일을 입력하세요 : ")
        if e.match(email): #정규표현식
            ck = 0
            for i in custlist:
                if i["email"] == email:
                    print("***이메일이 중복됩니다***")
                    ck = 1
                    break
            if ck==0:
                return email
        else:
            print("***올바른 이메일을 입력***")
def birthyear():
    while True: #출생년도 입력
        birthyear = input("출생년도를 입력하세요 : ")
        if birthyear.isdecimal() and len(birthyear) == 4:
            return birthyear
        else:
            print("***올바른 출생년도를 입력(4자리 숫자)***")
def update(tmp, i):
    if tmp == "1": #이름 수정
        custlist[i]["name"] = name()
    elif tmp == "2": #성별 수정
        custlist[i]["gender"] = gender()
    elif tmp == "3": #출생년도 수정
        custlist[i]["birthyear"] = birthyear()
def show(customer):
    print("이름 : {}  성별 : {}".format(customer["name"], customer["gender"]))
    print("이메일 : {} ".format(customer["email"]))
    print("출생년도 : {} ".format(customer["birthyear"]))

while True:
    choice = input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
    
    if choice == "I":        
        print("고객 정보 입력")
        customer = {}
        customer["name"] = name()
        customer["gender"] = gender()
        customer["email"] = email()
        customer["birthyear"] = birthyear()
        custlist.append(customer)
        page += 1
    elif choice == "C":
        if page>=0 and len(custlist)>0:
            print("현재 고객 정보 조회 {}".format(page+1))
            show(custlist[page])
        else:
            print("***고객 정보가 없습니다***")
    elif choice == 'P':
        if page<=0:
            print("***첫번째 페이지 입니다***")
        else:
            print("이전 고객 정보 조회 {}".format(page+1))
            page -= 1
            show(custlist[page])
    elif choice == 'N':
        if len(custlist) <= page:
            print("다음 고객 정보 조회 {}".format(page+1))
            page += 1
            show(custlist[page])
        else:
            print("***마지막 페이지 입니다***")
    elif choice == 'D':
        print("고객 정보 삭제")
        while True: #이메일 입력
            del_mail = input("삭제할 고객의 이메일 입력 : ")
            delok = 0
            if e.match(del_mail): #정규표현식
                for i in range(len(custlist)):
                    if custlist[i]["email"] == del_mail:
                        delok = 1
                        show(custlist[i])
                        del custlist[i]
                        page -= 1
                        print("***삭제 완료***")
                        break
                if delok == 0:
                    print("***해당하는 이메일이 없습니다***")
                else:
                    break
            else:
                print("***올바른 이메일을 입력***")
    elif choice == "U": 
        print("고객 정보 수정")
        while True: #이메일 입력
            up_mail = input("삭제할 고객의 이메일 입력 : ")
            idx = -1
            if e.match(up_mail): #정규표현식
                for i in range(len(custlist)):
                    if custlist[i]["email"] == up_mail:
                        idx = 0
                        show(custlist[i])
                        while True:
                            tmp = input("수정할 항목을 선택(1 : 이름, 2 : 성별, 3 : 출생년도, 4 : 나가기) : ")
                            if tmp in ("1","2","3"):
                                update(tmp, i)
                                show(custlist[i])
                                print("***수정 완료***")
                            elif tmp == "4":
                                break
                            else:
                                print("***1,2,3,exit 중 하나를 선택해주세요***") 
                        break
                if idx == -1:
                    print("***해당하는 이메일이 없습니다***")
                else:
                    break
            else:
                print("***올바른 이메일을 입력***")
    elif choice == "Q":
        print("프로그램 종료")
        break