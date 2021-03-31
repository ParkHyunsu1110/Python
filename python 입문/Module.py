##첫번째 실습
##import Prod
##print(Prod.prod(1,2,3))

##두번째 실습
import random
list=['','','','','','','']
for i in range(len(list)):
    list[i] = random.randint(1,25)
print(list) ##정렬 전
list.sort()
print(list) ##정렬 후
