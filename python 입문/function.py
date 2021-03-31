##첫번째 문제
def test(a,b,c):
    return a*b*c
print(test(1,2,3))
##두번째 문제
def test():
    return "안녕"
print(test())
##세번째 문제
def test(a,b=3,c=4):
    return a+b+c
print("1번 정답: ",test(2))
print("2번 정답: ",test(1,2))
print("3번 정답: ",test(1,2,3))
