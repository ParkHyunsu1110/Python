##Tkinter 실습 (1-2)
from tkinter import *

mainFrame = Tk()

mainFrame.geometry("200x200")

sizeLabel = Label(mainFrame, text="크기", font="serif 20")
sizeLabel.pack()

colorLabel = Label(mainFrame, text="색상", font="serif 20", foreground="Blue")
colorLabel.pack()

def changeSize():
    sizeLabel["font"] = "30"
sizeButton = Button(mainFrame, text="크기 변경", command = changeSize)
sizeButton.pack()
def changeColor():
    colorLabel["foreground"] = "Red"
colorButton = Button(mainFrame, text="크기 변경", command = changeColor)
colorButton.pack()

mainFrame.mainloop()
