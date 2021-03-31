##랜덤 당첨 번호 맞추기 게임 
import random

print("---------------------------------------")
print("-------------[LOTTO 6/25]--------------")
print("---------------------------------------")
print("----------------[조 건]----------------")
print("---------------------------------------")
print("1. 숫자의 범위는 1부터 25까지----------")
print("2. 범위 외의 숫자를 입력한 경우 재입력-")
print("3. 각기 다른 숫자를 입력---------------")

myLotto= []
while True:
    number = int(input(">>"))
    if 0< number and number < 26:
        myLotto.append(number)
        for i in range(len(myLotto)):
            if i != 0 and number == myLotto[i-1]:
                print("같은 숫자가 있습니다, 다시 입력해 주세요.")
                del myLotto[-1]
                continue
            else:
                continue
        if len(myLotto) == 6:
            break
        else:
            continue
    else:
        print("숫자를 다시 입력 하세요.")
        continue
    
comLotto = []
comLotto = random.sample(range(1,26),6)
print("---------------------------------------")
print("-------------[LOTTO 6/25]--------------")
print("---------------------------------------")
print("당첨 번호 : ", comLotto)
print("입력 번호 : ", myLotto)

count = 0

for i in range(len(myLotto)):
    for j in range(len(myLotto)):
        if myLotto[i] == comLotto[j]:
            count += 1
print("당신의 순위는...")
if count == 6: print("1등입니다.")
elif count == 5: print("2등입니다.")
elif count == 4: print("3등입니다.")
elif count == 3: print("4등입니다.")
elif count == 2: print("5등입니다.")
elif count == 1: print("6등입니다.")
elif count == 0: print("7등입니다.")

if 3 < count and count < 7:
    print("축하드립니다!!")
elif 0 <= count and count < 4:
    print("다시 도전해 봐요!")
