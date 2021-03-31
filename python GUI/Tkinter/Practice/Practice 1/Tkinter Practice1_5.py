##Tkinter 실습 (1-5)
from tkinter import *
import tkinter.messagebox
mainFrame = Tk()
mainFrame.geometry("200x200")

yesLabel = Label(mainFrame, text="예", font="serif 20")
yesLabel.pack( side = "left")

noLabel = Label(mainFrame, text="아니오", font="serif 20")
noLabel.pack( side = "right")

def changeColor():
    result = tkinter.messagebox.askyesno("색상 변경","선택하십시오.")
    if result == True:
        yesLabel["background"] = "Blue"
    elif result == False:
        noLabel["background"] = "Red"
mainButton = Button(mainFrame, text="질문", command=changeColor)
mainButton.pack()

mainFrame.mainloop()
