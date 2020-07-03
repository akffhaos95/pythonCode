prompt = '''
-----------------------
    커피 자판기 메뉴    
-----------------------
1. 커피 메뉴 입력
2. 커피 메뉴 삭제
3. 커피 추출
4. 커피 메뉴 리스트
5. 종료
-----------------------
메뉴 선택 >>> '''
coffee = {'카누' : [1000, 10], '아메리카노' : [2000, 10] }
money = 10000
while True:
    print(prompt)
    menu = input()
    if menu=='1':
        name = input("커피 이름 : ")
        price = int(input("가격 : "))
        coffee[name] = [price, 10]
        print(coffee)
    elif menu=='2':
        name = input("삭제할 커피 : ")
        if name not in coffee:
            print("커피가 존재하지 않습니다")
        else:
            del(coffee[name])
        print(coffee)
    elif menu=='3':
        name = input("추출할 커피 이름 : ")
        if name not in coffee:
            print("커피가 존재하지 않습니다")
        else:
            if coffee[name][0] > money:
                print("잔액이 부족합니다.")
            else:
                if coffee[name][1]==0:
                    print("재고가 없습니다")
                else:
                    money -= coffee[name][0]
                    coffee[name][1] = coffee[name][1] -1
            print(coffee)
            print("잔액", money)
    elif menu=='4':
        for i in coffee.keys():
            print("메뉴 : ",i, end="    ")
        print("")
        for j in coffee.values():
            print("가격 : ",j[0], end="    ")
        print("")
        for j in coffee.values():
            print("재고 : ",j[1], end="      ")
        print("")
    elif menu=='5':
        print("종료")
        break
    else:
        print("존재하지 않는 메뉴")