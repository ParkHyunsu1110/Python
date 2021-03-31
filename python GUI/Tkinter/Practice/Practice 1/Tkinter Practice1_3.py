##Tkinter 실습 (1-3)
from tkinter import *
import tkinter.messagebox
mainFrame = Tk()

mainFrame.geometry("200x200")

showLabel = Label(mainFrame, text="정보 보여주기", font="serif 20")
showLabel.pack()

def showMyinfo():
    tkinter.messagebox.showinfo("정보 확인하기","이름: 박현수, 나이 22세")
showButton = Button(mainFrame, text="정보 확인하기", command = showMyinfo)
showButton.pack()

mainFrame.mainloop()
