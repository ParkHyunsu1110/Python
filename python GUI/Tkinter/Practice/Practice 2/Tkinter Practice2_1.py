##Tkinter 실습 (2-1)
from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
mainFrame = Tk()
mainFrame.geometry("200x200")
mainLabel = Label(mainFrame, text="로그인 프로그램", font="serif 15")
mainLabel.pack()
def login():
    id_Result = tkinter.simpledialog.askstring("로그인 프로그램","ID : ")
    pw_Result = tkinter.simpledialog.askstring("로그인 프로그램","PW : ")
    if id_Result == "1" and pw_Result == "a" :
        tkinter.messagebox.showinfo("로그인 결과...", "환영합니다!")
    else:
        tkinter.messagebox.showinfo("로그인 결과...", "정보가 옳지 않습니다.")
mainButton = Button(mainFrame, text="로그인", command=login)
mainButton.pack()
mainFrame.mainloop()
