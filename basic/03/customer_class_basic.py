import re

class Customer():
    custlist=[{'name': '홍길동', 'gender': 'M', 'email': 'hong1@gmail.com', 'birthyear': 2000},
            {'name': '김길동', 'gender': 'M', 'email': 'kims1@gmail.com', 'birthyear': 2010},
            {'name': '박나리', 'gender': 'F', 'email': 'park1@gmail.com', 'birthyear': 1999},
            {'name': '김철수', 'gender': 'M', 'email': 'kim00@gmail.com', 'birthyear': 1988}]
    page=3
    def firstinput(self):
        choice=input('''
            다음 중에서 하실 일을 골라주세요 :
            I - 고객 정보 입력
            C - 현재 고객 정보 조회
            P - 이전 고객 정보 조회
            N - 다음 고객 정보 조회
            U - 고객 정보 수정
            D - 고객 정보 삭제
            Q - 프로그램 종료
            ''').upper()  
        return choice   
    def exe(self,choice):
        if choice=='I':
            self.insertData()    
        elif choice=='C':
            self.curSearch()
        elif choice=='P':
            self.preSearch()
        elif choice=='N':
            self.nextSearch()
        elif choice=='U':
            self.updateData()
        elif choice=='D':
            self.deleteData()    
        elif choice=='Q':
            quit()
    def name(self):
        while True: #이름 입력
            name = input("이름을 입력하세요 : ")
            n = re.compile('[a-zA-Z]{3,}')
            if n.match(name):
                return name
            else:
                print("***올바른 이름을 입력***")
    def gender(self):
        while True: #성별 입력
            gender = input("성별을 입력하세요 : ").upper()
            if gender in ("M", "F"):
                return gender
            else:
                print("***올바른 성별을 입력(M/F)***")
    def email(self):
        while True: #이메일 입력
            email = input("이메일을 입력하세요 : ")
            e = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
            if e.match(email): #정규표현식
                ck = 0
                for i in self.custlist:
                    if i["email"] == email:
                        print("***이메일이 중복됩니다***")
                        ck = 1
                        break
                if ck==0:
                    return email
            else:
                print("***올바른 이메일을 입력***")
    def birthyear(self):
        while True: #출생년도 입력
            birthyear = input("출생년도를 입력하세요 : ")
            if birthyear.isdecimal() and len(birthyear) == 4:
                return birthyear
            else:
                print("***올바른 출생년도를 입력(4자리 숫자)***")
    def update(self, tmp, i):
        if tmp == "1": #이름 수정
            self.custlist[i]["name"] = self.name()
        elif tmp == "2": #성별 수정
            self.custlist[i]["gender"] = self.gender()
        elif tmp == "3": #출생년도 수정
            self.custlist[i]["birthyear"] = self.birthyear()
    def show(self,customer):
        print("이름 : {}  성별 : {}".format(customer["name"], customer["gender"]))
        print("이메일 : {} ".format(customer["email"]))
        print("출생년도 : {} ".format(customer["birthyear"]))
    def insertData(self):    
        print("고객 정보 입력")
        customer = {}
        customer["name"] = self.name()
        customer["gender"] = self.gender()
        customer["email"] = self.email()
        customer["birthyear"] = self.birthyear()
        self.custlist.append(customer)
        self.page + 1  
    def curSearch(self):
        if self.page>=0 and len(self.custlist)>0:
            print("현재 고객 정보 조회 {}".format(self.page+1))
            self.show(self.custlist[self.page])
        else:
            print("***고객 정보가 없습니다***")
    def preSearch(self):
        if self.page<0:
            print("***첫번째 페이지 입니다***")
        else:
            print("이전 고객 정보 조회 {}".format(self.page+1))
            self.page -= 1
            self.show(self.custlist[self.page])
    def nextSearch(self):
        if len(self.custlist) <= self.page:
            print("다음 고객 정보 조회 {}".format(self.page+1))
            self.page += 1
            self.show(self.custlist[self.page])
        else:
            print("***마지막 페이지 입니다***")
    def deleteData(self):
        print("고객 정보 삭제")
        while True: #이메일 입력
            del_mail = input("삭제할 고객의 이메일 입력 : ")
            e = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
            delok = 0
            if e.match(del_mail): #정규표현식
                for i in range(len(self.custlist)):
                    if self.custlist[i]["email"] == del_mail:
                        delok = 1
                        self.show(self.custlist[i])
                        del self.custlist[i]
                        page -= 1
                        print("***삭제 완료***")
                        break
                if delok == 0:
                    print("***해당하는 이메일이 없습니다***")
                else:
                    break
            else:
                print("***올바른 이메일을 입력***")
    def updateData(self): 
        print("고객 정보 수정")
        while True: #이메일 입력
            up_mail = input("삭제할 고객의 이메일 입력 : ")
            e = re.compile('[a-z][a-z0-9]{4,}@[a-z]{2,}.[a-z]{2,5}')
            idx = -1
            if e.match(up_mail): #정규표현식
                for i in range(len(self.custlist)):
                    if self.custlist[i]["email"] == up_mail:
                        idx = 0
                        self.show(self.custlist[i])
                        while True:
                            tmp = input("수정할 항목을 선택(1 : 이름, 2 : 성별, 3 : 출생년도, 4 : 나가기) : ")
                            if tmp in ("1","2","3"):
                                self.update(tmp, i)
                                self.show(self.custlist[i])
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
    def __init__(self):
        while True:
            self.exe(self.firstinput())

Customer()
 