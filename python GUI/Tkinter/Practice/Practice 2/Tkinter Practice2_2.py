##Tkinter 실습 (2-2)
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

menubar = Menu(mainFrame)
mainFrame.config(menu = menubar)

figure_Item = Menu(menubar)
menubar.add_cascade(label = "도형", menu = figure_Item)
def circle() :
    print("원")
def rectangle() :
    print("사각형")
def line() :
    print("선")
figure_Item.add_command( label = "원", command = circle)
figure_Item.add_command( label = "사각형", command = rectangle)
figure_Item.add_command( label = "선", command = line)

help_Item = Menu(menubar)
menubar.add_cascade(label = "도움말", menu = help_Item)

def info() :
    print("정보")
def check() :
    print("확인")
help_Item.add_command( label = "정보", command = info)
help_Item.add_command( label = "확인", command = check)

mainFrame.mainloop()
