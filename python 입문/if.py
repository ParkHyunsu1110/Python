##첫번째 문제
user_input = input("나이를 입력하세요.")
age = int( user_input )
if (1 <= age <=7) : print("유아")
elif ( 8 <= age <= 13) : print("초등학생")
elif ( 14 <= age <= 16) : print("중학생")
elif ( 17 <= age <= 19) : print("고등학생")
else : print("성인")
##두번째 문제
user_name = input("이름을 입력하세요.")
if( user_name == "홍길동") : print("남자")
elif(user_name == "성춘향") : print("여자")
else : print("모르겠어요.")
