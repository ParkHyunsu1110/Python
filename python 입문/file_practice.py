f = open("a.txt","w")

f.write("반가워요\n")

f.close()

f = open("a.txt","r")
print(f.read())

