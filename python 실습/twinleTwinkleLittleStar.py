##반짝반짝 작은별
##첫 번째 문제
height1 = int(input("줄 수를 입력해 주세요. : "))
for i in range (0, height1+1):
    print("*"*i)
##두 번째 문제
height2 = int(input("줄 수를 입력해 주세요. : "))
for j in range(0, height2+1):
    print(" "*(height2-j), end='')
    print("*"*j)
##세 번째 문제
height3 = int(input("줄 수를 입력해 주세요. : "))
for k in range(0, height3+1):
    print(" "*(height3-k), end='')
    print("*"*k, end='')
    print("*"*(k-1))
