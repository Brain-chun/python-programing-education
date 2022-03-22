items = {"커피음료":7,"펜":3,"종이컵":2,"우유":1,"콜라":3,"책":5}

#메뉴별 항목을 반복하기위해 무한반복문을 만들고 특정상황시 반복문 종료
case = True

while case:
    menu = int(input("메뉴를 선택하시오 1) 재고조회 2) 입고 3) 출고 4) 종료 : "))
    
    if menu == 1:
        print("[재고조회] ",end="")
        key = input("물건의 이름을 입력하시오 : ").rstrip()
        print("재고 : ",items.get(key))
        
    elif menu == 2:
        key, x = input("[입고] 물건의 이름과 수량을 입력하시오 : ").split() 
        items[key] += int(x)
        print(key+"의 재고 : " + str(items[key]))
        
    elif menu == 3:
        key, x = input("[출고] 물건의 이름과 수량을 입력하시오 : ").split()        
        #재고가 음수 값으로 떨어지는 상황 방지
        if items[key] - int(x) < 0:
            print(str(items[key])+"개 이상 출고할 수 없습니다.")
        else:
            items[key] -= int(x)
        print(key+"의 재고 : " + str(items[key]))
        
    elif menu == 4:
        #프로그램 종료시 무한 while loop 탈출
        print("프로그램을 종료합니다.")
        case = False
    
    else:
        print("잘못된 입력입니다.")
