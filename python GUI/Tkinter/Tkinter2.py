from tkinter import *
import tkinter.messagebox   ##메세지 박스
import tkinter.simpledialog ##대화 상자

mainFrame = Tk()

##messagebox

##show
tkinter.messagebox.showinfo("정보 보여주기", "showinfo 대화상자")          ##알림
tkinter.messagebox.showwarning("정보 경고하기", "showwarning 대화상자")    ##경고
tkinter.messagebox.showerror("에러 보여주기", "showerror 대화상자")        ##에러

##ask
tkinter.messagebox.askyesno("정보 보여주기", "askyesno 대화상자")                  ## 예, 아니오 버튼
tkinter.messagebox.askyesnocancel("정보 보여주기", "askyesnocancel 대화상자")      ## 예, 아니오, 취소 버튼                               	
tkinter.messagebox.askokcancel("정보 보여주기", "askokcancel 대화상자")            ## OK, 취소 버튼
tkinter.messagebox.askretrycancel("정보 보여주기", "askretrycancel 대화상자")      ## 다시 시도, 취소 버튼
tkinter.messagebox.askquestion("정보 보여주기", "askquestion 대화상자")            ## 예, 아니오 버튼

##simpledialog


##ask
tkinter.simpledialog.askinteger( "정보 입력하기", "askinteger 정수 입력하기" )   ## 정수를 입력 받음
tkinter.simpledialog.askstring( "정보 입력하기", "askstring 문자열 입력하기" )    ## 입력 받은 것을 문자열로 취급
mainFrame.mainloop()

##messagebox

## 알림창 (확인 버튼 1개)
showinfo( "제목"," 메세지", "옵션" )
## 경고창 (확인 버튼 1개)
showwarning( "제목", "메세지", "옵션" )
## 에러창 (확인 버튼 1개)
showerror( "제목", "메세지", "옵션" )
## 선택창 (예, 아니오 버튼)
askyesno( "제목", "메세지", "옵션" ) 
## 선택창 (예, 아니오, 취소 버튼)
askyesnocancel( "제목", "메세지", "옵션" )
## 선택창 (예, 취소 버튼)
askokcancel( "제목", "메세지", "옵션" )
## 경고창 (다시시도, 취소 버튼)
askretrycancel( "제목", "메세지", "옵션" )
## 선택창 (예, 아니오 버튼)
askquestion( "제목", "메세지", "옵션" )

##simpledialog

## 정수를 입력 받음
askinteger( "제목", "메세지" )
## 입력 받은 것을 문자열로 취급
askstring( "제목", "메세지" )    
