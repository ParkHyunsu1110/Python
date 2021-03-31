##file = open("file.txt","w")
##file.write("반갑습니다.\n안녕히계세요.")
##file.close()

	
# 파일 탐색기를 통해 C 드라이브 안에 'Folder'라는 폴더를 생성해주세요.
# 메모장에서 그림과 같이 작성하시고 information.txt 를 Folder라는 폴더 안에 저장해주세요.
# 줄을 기준으로 앞의 것이 아이디, 뒤의 것이 비밀번호 입니다.( ex) 아이디 : 1, 비밀번호 : a )
# 사용자에게 아이디와 비밀번호를 입력받고, 일치하면 "성공"  일치하지 않으면 "실패" 라고 출력해주세요.
##user_id = input("아이디 : ")
##user_pw = input("비밀번호 : ")
##info = user_id+" "+user_pw
##print(info)
##file = open("C:\Folder\information.txt","r")
##print(file.read(), end='')
##for i in range(0,4):
##    if(info == file.readlines()):
##        print("성공\n")
##        break
##    else:
##        print("실패\n")

file = open("C:\Folder\information.txt","r")
info = file.readlines()
user_id = input("ID : ")
user_pw = input("PW : ")

for i in range(len(info)):
    information = info[i].split()
    if information[0] == user_id and information[1] == user_pw:
        print("로그인 성공")
        break
    else:
        print("로그인 실패")
        break
    
    
