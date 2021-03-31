from tkinter import *
mainFrame = TK()

mainFrame.mainloop();
##빙고게임
lyrics = input("가사를 입력 해 주세요")
times = lyrics.split()
word= input("찾을 단어를 입력해 주세요.")
find = times.count(word)
n = int(input("예상 횟수를 입력해 주세요."))

if n > find :
    for  i in range(1,n):
        print(i,",", end='')
    print("중에 답이 있습니다.")
elif n < find:
    print("예상 숫자보다 큽니다.")
else:
    print("빙고")
