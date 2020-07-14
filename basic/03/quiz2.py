def insertData():
    student = {}
    while True:
        id = input("학번(8자리) : ")
        if len(id) != 8:
            print("학번은 8자리 입니다.")
        else:
            dupli = 0
            for i in stdlist:
                if i["id"] == id:
                    dupli = 1
                    print("학번이 중복됩니다")
            if dupli == 0:
                student["id"] = id
                break
    student["name"] = input("이름 : ")
    student["major"] = input("전공 : ")
    student["number"] = input("전화번호 : ")
    student["address"] = input("주소 : ")
    stdlist.append(student)
def showData():
    print(stdlist)
def deleteData():
    while True:
        std = input("삭제할 학생의 학번 입력 : ")
        delok = 0
        for i in range(len(stdlist)):
            if stdlist[i]["id"] == std:
                delok = 1
                del stdlist[i]
                print("***삭제 완료***")
                break
        if delok == 0:
            print("***해당하는 학번 없습니다***")
        else:
            break
def updateData():
    while True:
        std = input("수정 학생의 학번 입력 : ")
        idx = -1
        for i in range(len(stdlist)):
            if stdlist[i]["id"] == std:
                idx = 0
                print(stdlist[i])
                while True:
                    tmp = input(
                        "수정할 항목을 선택(1 : 이름, 2 : 학과, 3 : 전화번호, 4 : 주소, 5: 나가기) : ")
                    if tmp == "1":
                        stdlist[i]["name"] = input("이름을 입력")
                        print("***수정 완료***")
                    elif tmp == "2":
                        stdlist[i]["major"] = input("학과를 입력")
                        print("***수정 완료***")
                    elif tmp == "3":
                        stdlist[i]["number"] = input("전화번호를 입력")
                        print("***수정 완료***")
                    elif tmp == "4":
                        stdlist[i]["address"] = input("주소를 입력")
                        print("***수정 완료***")
                    elif tmp == "5":
                        break
                    else:
                        print("***1,2,3,4,5 중 하나를 선택해주세요***")
        if idx == -1:
            print("***해당하는 이메일이 없습니다***")
        else:
            break

stdlist = [{'id': '21432779', 'name': '김민석', 'major': '컴퓨터공학과', 'number': '1923', 'address' : '집'}]

while True:
    choice =input('''
    다음 중에서 하실 일을 골라주세요 :
    1 - 학생 정보 입력
    2 - 학생 리스트 조회
    3 - 학생 정보 삭제
    4 - 학생 정보 수정
    5 - 프로그램 종료
    ''')

    if choice =='1':
        insertData()
    elif choice =='2':
        showData()
    elif choice =='3':
        deleteData()
    elif choice =='4':
        updateData()
    elif choice =='5':
        quit()