##★RSP
rsp_in = []
win = 0
for i in input("입력(각각의 사람이 무엇을 낼지)").split():
    rsp_in.append(int(i))
print(rsp_in)
for i in range(len(rsp_in)):
    for j in range(len(rsp_in)):
        if rsp_in[i] == 1 and rsp_in[j]==3:
            win += 1
        elif rsp_in[i] == 2 and rsp_in[j]==1:
            win += 1
        elif rsp_in[i] == 3 and rsp_in[j]==2:
            win += 1
        else:
            break
print("출력(이긴 사람의 수)")
print(win)

##★RSP-해답
a = input(">>")
player = a.split()

s = player.count('1')
r = player.count('2')
p = player.count('3')

if s == 0 and r != 0 and p != 0:
    print(p)
elif s != 0 and r == 0 and p != 0:
    print(s)
elif s != 0 and r != 0 and p == 0:
    print(r)
elif s == 0 and r == 0 and p == 0:
    print(0)
elif s != 0 and r != 0 and p != 0:
    print(0)
