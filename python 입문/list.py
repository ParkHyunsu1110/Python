fruits=['apple','strawberry','banana','melon','grape','kiwi']
##첫번째 문제
print(fruits[2:4])
##두번째 문제
print(fruits[3:])
##세번째 문제
fruits1=['appple','strawberry','banana','watermelon']
fruits2=['melon','grape','kiwi']
if len(fruits1) > len(fruits2): print(fruits1)
else: print(fruits2)
##네번째 문제
countries=['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam']
countries.append('China')
print(countries)
##다섯번째 문제
countries=['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam']
countries.extend(['China','Japan'])
print(countries)
##여섯번째 문제
countries=['Korea', 'America', 'Spain', 'Germany', 'Mexico', 'Vietnam']
countries.remove('Spain')
print(countries)
##일곱번째 문제
num=[1,3,5,7,9]
print(sum(num))
##여덟번째 문제
num=[13,29,54,31,67]
sumnum = int(min(num)+max(num))
print(sumnum)
print(fruits1 if (len(fruits1)>len(fruits2)) else fruits2)
print( 1 if (len(fruits1)>len(fruits2))else  0)
