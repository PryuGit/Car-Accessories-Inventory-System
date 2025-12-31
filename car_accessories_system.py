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
        if self.__stock_quantity<100:
            self.__stock_quantity=stock_quantity
        else:
            print("Error, The value must be less than 100!!")
    
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
           print("Error, The value must be at least 1")
    
    def sellStock(self,amount):
        if amount<1:
            print("Error, The value must be at least 1")
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
                f"Price Without VAT:{self.getStockPrice():.2f}\n"
                f"Price With VAT:{self.getPriceWithVAT():.2f}\n"
                f"Total unit in stock:{self.getStockQuantity()}\n")

class NavSys(StockItem):
    
    def  __init__(self,stock_code,stock_quantity,stock_price,brand):
        super().__init__(stock_code,stock_quantity,stock_price)
        self.__brand= brand
    
    def getStockName(self):
        return "Navigation System"
    
    def getStockDescription(self):
        return "GeoVision Sat Nav"
    
    def getBrand(self):
        return "TomTom"
    
    def __str__(self):
        return super().__str__()+f"Brand:{self.getBrand()}\n"

print("\nCar Parts and Accessories Management System\n")    
code=input("Enter Stock Code:")  
unit=int(input("Enter Total Unit:"))
price=float(input("Enter Price per Unit:"))
brand=input("Enter Brand:")
      
sys=NavSys(code,unit,price,brand)

print(f"\nCreating a stock with {sys.getStockQuantity()} units {sys.getStockName()}, price {sys.getStockPrice()} each, and item code {sys.getStockCode()}")
print(sys)

print("Edit:")
print("1)Increase unit")
print("2)Decrease unit")
print("3)Set new price per unit")
choice=int(input("Select Option:"))
match(choice):
    case 1:
        print(f"Increasing 10 more units")
        sys.increaseStock(10)
        print(sys)

    case 2:
        print(f"Sold 10 units")
        sys.sellStock(10)
        print(sys)

    case 3:
        sys.setStockPrice(100.9)
        print(f"Set new price 100.9 per unit")
        print(sys)
        
    case _:
        print("Invalid")