from tkinter import *
import tkinter.messagebox
import tkinter.simpledialog
 
mainFrame = Tk()
 
result1 = tkinter.simpledialog.askstring( "제목", "이름을 입력하세요.")
print( result1 )
result2 = tkinter.simpledialog.askinteger("제목", "나이를 입력하세요.")
print( result2 )
mainFrame.mainloop()
