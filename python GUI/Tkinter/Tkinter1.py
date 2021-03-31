from tkinter import *

mainFrame = Tk()
##mainFrame.geometry("400x300")
##Button 예제
##appleButton = Button( mainFrame, text="사과", foreground = "Red")
##appleButton.pack()
##Label 예제
##fruitLable = Label(mainFrame, text="과일들", font="Serif 20")
##fruitLable.pack()

##pack() 사용 - side
mainFrame.geometry("500x500")

##b1 = Button(mainFrame, text = "1")
##b1.pack( side = "left")
##b2 = Button(mainFrame, text = "2")
##b2.pack( side = "right")
##b3 = Button(mainFrame, text = "3")
##b3.pack( side = "top")
##b4 = Button(mainFrame, text = "4")
##b4.pack( side = "bottom")
b1 = Button(mainFrame, text = "1")
b1.pack()
b2 = Button(mainFrame, text = "2")
b2.pack()
b3 = Button(mainFrame, text = "3")
b3.pack()
b4 = Button(mainFrame, text = "4")
b4.pack()

mainFrame.mainloop()
