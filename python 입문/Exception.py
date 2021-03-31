##첫번째 실습
direction = ["east","west","north","south"]
for i in range(0,5):
    try:
        print(direction[i])
    except IndexError:
        print("해당하는 인덱스가 없습니다.")

##두번째 실습
try:
    f = open("name.txt","r")
    
    print(f.read())
except FileNotFoundError:
    print("파일이 없습니다.")
