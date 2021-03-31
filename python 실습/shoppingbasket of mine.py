import sys
basket = []
while 1:
    print("=" * 30)
    print("코디의 장바구니입니다.")
    print("==============================")
    print("1. 담겨있는 물건 확인하기")
    print("\n 2. 물건 추가하기")
    print("\n 3. 물건 삭제하기")
    print("\n 0. 프로그램 종료")
    print("==============================")
    menu = int(input("무엇을 하실 건가요? (숫자 입력) : "))

    if(menu == 1):
        if(basket == []): #basket is Nome (기존 코드)
            print("\n아무것도 없습니다.")
        else:
            print(basket) 
    elif(menu == 2):
        while 1:
            object = input("추가 할 항목을 입력해 주세요. 더 이상 추가할 항목이 없으면 '그만'을 입력해 주세요")
            if(object=="그만"):
                print("\n장바구니 담기를 종료합니다.")
                break
            basket.append(object)

    elif(menu == 3):
        while 1:
            if(basket == []):   ##장바구니 상태 확인 후 비어있을때 종료되도록.  
                print("\n장바구니가 비었습니다. 추가해 주세요.")
                break
            print(basket)
            print("\n\n현재 담겨있는 장바구니 목록입니다. 삭제하실 항목을 입력해 주세요.")
            print("\n삭제 메뉴를 종료하시려면 그만을 입력해 주세요.\n")
            del_menu = input()
            if(del_menu in basket):     #del_menu is basket
                basket.remove(del_menu)
                print("\n삭제가 완료되었습니다.")
            elif(del_menu == "그만"):
                break
            else:
                print("\n잘못된 값을 입력하셨습니다. 다시 입력해 주세요.")
    elif(menu == 0):
        print("\n프로그램을 종료합니다.")
        sys.exit()
    else:
        print("\n잘못 입력했습니다. 다시 입력해 주세요.")
