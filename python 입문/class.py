##첫번째 문제
##SuperMarket
class Supermarket(object) :
    def __init__(self,location,name,product,customer) :
        self.location = location ##위치
        self.name = name         ##가게 이름
        self.product = product   ##파는 물건
        self.customer = customer ##고객의 수
        
    def printLocation(self) :
        print(self.location)

    def changeCategory(self, productNew) :
        self.product = productNew
        
        
    def showList(self) :
        print(self.prodeuct)


    def enterCustomer(self) :
        print(self.customer + 1)

    def showInfo(self) :
        print("가게 이름 : ", self.name)
        print("가게 위치 : ", self.location)
        print("파는 물건 : ", self.product)
        print("손님 수 : ", self.customer)
    
