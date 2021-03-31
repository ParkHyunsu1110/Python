##첫번째 문제
user_age = input("나이를 입력하세요. >>")
age = int( user_age )
if(age >= 20):
    print("성인")
    if(age % 2 == 0):
        print("나이가 짝수인 성인")
    else:
        print("나이가 홀수인 성인")
else :
    print("미성년자")
    if(age % 2 == 0):
        print("나이가 짝수인 미성년자")
    else:
        print("나이가 홀수인 미성년자")
##두번째 문제
        number = input("숫자를 입력하세요. >> ")
no = int(number)
for i in range(no+1):
    for j in range(i):
        print(i, end='')
