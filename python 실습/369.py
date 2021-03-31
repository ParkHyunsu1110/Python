##★369게임
N = int(input("N : "))
count = 0
for i in range(1, N+1):
    if i // 10 == 3 or i // 10 == 6 or i // 10 == 9:
        print("짝!")
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("짝짝!!")
        count += 1
    else:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            print("짝!")
            count += 1
        else:
            print(i)
print("짝! or 짝짝!! : ",count)
