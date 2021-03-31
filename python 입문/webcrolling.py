##import urllib.request
## 
##html = urllib.request.urlopen("https://www.naver.com/")
##doc = html.read().decode("UTF-8")
##print(doc)

from urllib.request import urlopen

html = urlopen("https://www.naver.com/")
doc = html.read().decode("UTF-8")
print(doc)
