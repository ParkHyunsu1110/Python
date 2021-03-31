##Tkinter 실습 (1-4)
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog

mainFrame = Tk()

mainFrame.geometry("300x300")

nameLabel = Label(mainFrame, text="이름", font="serif 20")
nameLabel.pack()

ageLabel = Label(mainFrame, text="나이", font="serif 20")
ageLabel.pack()

def changeLabels():
    nameLabel["text"] = tkinter.simpledialog.askstring("정보 입력","이름을 입력 해 주세요.")
    ageLabel["text"] = tkinter.simpledialog.askinteger("정보 입력","나이를 입력 해 주세요.")
    
changeButton = Button(mainFrame, text="정보 입력", command=changeLabels)
changeButton.pack()

mainFrame.mainloop()
