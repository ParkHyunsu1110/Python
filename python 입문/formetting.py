import math
print("pi is%f"%(math.pi))

print("%d"%(100,))
print("%20d"%(100,))
print("%020d"%(100,))
print("%-20d"%(100,))

print("%.10f"%(math.pi))

	
print(""" 
〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
%30s
〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
 
제목: %s
가격: %d
설명: %s
"""%("컴퓨터개론","컴퓨터개론",20000,"컴퓨터의 기초에 대해서 설명하고 있다."))

	
print(""" 
〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
%(title)30s
〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓〓
 
제목: %(title)s
가격: %(price)d
설명: %(desc)s
"""%{"title":"컴퓨터 개론","price":20000,"desc":"컴퓨터의 기초에 대해서 설명하고 있다."})


print("{0}*{1}is{2}".format(2,3,2*3))
print("{1}*{0}is{2}".format(2,3,2*3))
print("{x}*{y}is{result}".format(x=3,y=5,result=3*5))
