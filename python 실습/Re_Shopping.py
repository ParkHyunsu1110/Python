##나만의 장바구니
import sys
basket = []
while True:
    print("="*30)
    print("코디의 장바구니")
    print("="*30)
    print("1. 물건 확인")
    print("\n2. 물건 추가")
    print("\n3. 물건 삭제")
    print("\n0. 종료하기")
    print("="*30)
    menu = int(input("무엇을 할까요? (숫자 입력) : "))
    if menu == 1:
        if basket == []:
            print("\n아무것도 없습니다.")
        else:
            print(basket)
    elif menu == 2:
        while True:
            add_object = input("추가할 항목을 입력해 주세요. 더이상 추가할 항목이 없으면 '그만'을 입력해 주세요. \n")
            if add_object=="그만":
                print("\n장바구니 담기를 종료합니다.")
                break
            else:
                basket.append(add_object)
    elif menu == 3:
        while True:
            if basket == []:
                print("\n아무것도 없습니다.")
                break
            print(basket)
            print("\n\n현재 담겨있는 장바구니 목록입니다, 삭제하실 항목을 입력해 주세요.")
            print("삭제 메뉴를 종료하실려면 0을 입력해 주세요.\n")
            remove_object = input()
            if remove_object == "0":
                print("\n장바구니 삭제를 종료합니다.")
                break
            elif remove_object in basket:
                print("\n삭제가 완료되었습니다.")
                basket.remove(remove_object)
            else:
                print("\n잘못된 값을 입력하셨습니다. 다시 입력해 주세요.")
    elif menu == 0:
        print("\n프로그램을 종료합니다.")
        sys.exit()
    else:
        print("\n잘못 입력하셨습니다. 다시 입력하세요.")
        
