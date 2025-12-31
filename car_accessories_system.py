class StockItem:
    stock_category='Car accessories'
    
    def __init__(self,stock_code,stock_quantity,stock_price):
        self.__stock_code=stock_code
        self.__stock_quantity=stock_quantity
        self.__stock_price=stock_price
        
    def getStockCode(self):
        return self.__stock_code
    
    def getStockQuantity(self):
        return self.__stock_quantity
    
    def getStockPrice(self):
        return self.__stock_price
    
    def setStockCode(self,stock_code):
        self.__stock_code=stock_code
        
    def setStockQuantity(self,stock_quantity):
        self.__stock_quantity=stock_quantity
    
    def setStockPrice(self,stock_price):
        self.__stock_price=stock_price
    
    def getStockName(self): 
        return "Unknown Stock Name"
    
    def getStockDescription(self):
        return "Unknown Stock Description"
    
    def getVAT(self):
        return 17.5
    
    def getPriceWithVAT(self):
        return self.getStockPrice()+(self.getStockPrice()*(self.getVAT()/100))   
       
    def increaseStock(self,amount):
        if amount>1:
            self.setStockQuantity(self.getStockQuantity()+amount)
        else:
           print("Error, The value must be at least 1 or less than 100!!")
    
    def sellStock(self,amount):
        if amount<1:
            print("Error, The value must be at least 1 or less than 100!!")
            return False
        elif amount<=self.getStockQuantity():
            self.setStockQuantity(self.getStockQuantity()-amount)
            return True
        else:
            return False
           
    def __str__(self):
        return (f"Printing item stock information:\n"
                f"Stock Category:{self.stock_category}\n"
                f"Stock Type:{self.getStockName()}\n"
                f"Description:{self.getStockDescription()}\n"
                f"Stock Code:{self.getStockCode()}\n"
                f"Price Without VAT:{self.getStockPrice()}\n"
                f"Price With VAT:{self.getPriceWithVAT()}\n"
                f"Total unit in stock:{self.getStockQuantity()}\n")
        
sys=StockItem("W1S1",2,200)

print(f"Creating a stock with {sys.getStockQuantity()} units {sys.getStockName()}, price {sys.getStockPrice()} each, and item code {sys.getStockCode()}")
print(sys)

print(f"Increasing 10 more units")
sys.increaseStock(10)
print(sys)

print(f"Sold 10 units")
sys.sellStock(10)
print(sys)

sys.setStockPrice(100.9)
print(f"Set new price 100.9 per unit")
print(sys)