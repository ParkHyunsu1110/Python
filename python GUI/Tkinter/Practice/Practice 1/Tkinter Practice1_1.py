from tkinter import *

mainFrame = Tk()
mainFrame.geometry("500x500")

practiceLabel = Label(mainFrame, text = "위치", font = "Serif 20")
practiceLabel.pack()

def changeLeft() :
    practiceLabel["text"] = "왼쪽"
leftButton = Button(mainFrame, text = "왼쪽", command = changeLeft)
leftButton.pack( side = "left")

def changeRight():
    practiceLabel["text"] = "오른쪽"

rightButton = Button(mainFrame, text = "오른쪽", command = changeRight)
rightButton.pack( side = "right")

mainFrame.mainloop()
