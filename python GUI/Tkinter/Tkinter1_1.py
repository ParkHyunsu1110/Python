from tkinter import *

mainFrame = Tk()
mainFrame.geometry("400x200")

nameLabel = Label( mainFrame, text = "이름", font = "serif 20")
nameLabel.pack()

def changeHong():
    nameLabel["text"] = "홍길동"

hongButton = Button(mainFrame, text="홍길동으로 변경", command = changeHong )
hongButton.pack()

def changeSeong():
    nameLabel["text"] = "성춘향"

seongButton = Button(mainFrame, text = "성춘향으로 변경", command = changeSeong)
seongButton.pack()
	
# 글씨 변경
라벨이름["text"] = "원하는글씨"
 
# 글씨 색상 변경
라벨이름["foreground"] = "원하는색상"
 
# 라벨 배경 색상 변경
라벨이름["background"] = "원하는색상"
 
# 글씨체/글씨 크기 변경
라벨이름["font"] = "글씨체 글씨크기"

mainFrame.mainloop()
