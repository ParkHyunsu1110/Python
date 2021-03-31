from tkinter import *
import tkinter.messagebox

mainFrame = Tk()

result = tkinter.messagebox.askyesno("정보 보여주기", "대화상자")
if result == True:
    print("예를 누르셨군요!")
elif result == False:
    print("아니오를 누르셨군요!")

mainFrame.mainloop()
