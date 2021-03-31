##타임어택 끝말잇기 만들기
import time
#30초 세기, 임의로 10초 설정
startTime = time.time()
endTime = startTime + 30.0

wordList=[]
matchingGame=[]
j=0
count = 0
print('첫번째 단어는 "강아지"입니다.') 
wordList.append("강아지")
while time.time() < endTime:
    word = input("단어 >> ")
    wordList.append(word)
    lastword = list(wordList[-2])
    if lastword[-1] == word[0]:
        matchingGame.append(word)
        j += 1
        count += 1
        
    else:
        print("올바르게 단어를 입력하세요")
        del wordList[j+1]
        continue
    
print( "30초 경과" )
print("성공한 단어의 갯수 : ", count)
print("성공한 끝말잇기: ", matchingGame)
