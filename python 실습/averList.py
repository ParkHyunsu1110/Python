##리스트 평균 구하기
list1 = []
for i in input("숫자를 여러개 입력해 주세요. >> ").split():
    list1.append(int(i))
print(list1)
print("가장 큰 값 : ",max(list1))
list2.remove(max(list1))
print("가장 작은 값 : ",min(list1))
list2.remove(min(list1))
print(list1)
print("나머지 값의 평균 : ",sum(list1)/len(list1))
