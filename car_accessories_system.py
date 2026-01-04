class StockItem:
    stock_category='Car accessories'
    
    #Initializing stock code,unit and price
    def __init__(self,stock_code,stock_quantity,stock_price):
        self.__stock_code=stock_code
        self.__stock_quantity=stock_quantity
        self.__stock_price=stock_price
     
    #Getter Methods   
    def getStockCode(self):
        return self.__stock_code
    
    def getStockQuantity(self):
        return self.__stock_quantity
    
    def getStockPrice(self):
        return self.__stock_price
    
    def getStockName(self): 
        return "Unknown Stock Name"
    
    def getStockDescription(self):
        return "Unknown Stock Description"
    
    def getVAT(self):
        return 17.5
    
    def getPriceWithVAT(self):
        return self.getStockPrice()+(self.getStockPrice()*(self.getVAT()/100)) 
    
    #Setter Methods
    def setStockCode(self,stock_code):
        self.__stock_code=stock_code
        
    def setStockQuantity(self,stock_quantity):
        self.__stock_quantity=stock_quantity
        
    def setStockPrice(self,stock_price):
        self.__stock_price=stock_price  
    
    #Increase Stock Units   
    def increaseStock(self,amount):
        if amount<1:
            print("Error, The unit quantity must be at least 1")
            return False
        elif amount+self.getStockQuantity()>100:
            print("Error, The unit quantity must not exceed more than 100")
            return False
        else:
            self.setStockQuantity(self.getStockQuantity()+amount)
            return True
    
    #Removing Sold Units
    def sellStock(self,amount):
        if amount<1:
            print("Error, The unit quantity must be at least 1")
            return False
        elif amount<=self.getStockQuantity():
            self.setStockQuantity(self.getStockQuantity()-amount)
            return True
        else:
            print("Error, Insufficient unit quantity")
            return False
    
    #Display the information of the stock       
    def __str__(self):
        return (f"Printing item stock information:\n"
                f"Stock Category:{self.stock_category}\n"
                f"Stock Type:{self.getStockName()}\n"
                f"Description:{self.getStockDescription()}\n"
                f"Stock Code:{self.getStockCode()}\n"
                f"Price Without VAT:{self.getStockPrice():.2f}\n"
                f"Price With VAT:{self.getPriceWithVAT():.2f}\n"
                f"Total unit in stock:{self.getStockQuantity()}\n")
        
#Inheritance from Parent Class 'StockItem' to Child Class 'NavSys' 
class NavSys(StockItem):
    
    #Initializing stock code, quantity, price and brand
    def  __init__(self,stock_code,stock_quantity,stock_price,brand):
        #Calls __init__ from StockItem
        super().__init__(stock_code,stock_quantity,stock_price)
        self.__brand= brand
    
    #Overrides the getStockName method from StockItem
    def getStockName(self):
        return "Navigation System"
    
    #Overrides the getStockDescription method from StockItem
    def getStockDescription(self):
        return "GeoVision Sat Nav"
    
    def getBrand(self):
        return "TomTom"
    
    #Print stock information including the brand of the stock
    def __str__(self):
        #Calls __str__ method from StockItem
        return super().__str__()+f"Brand:{self.getBrand()}\n"

#Main Program     
print("\nCar Parts and Accessories Management System\n")    
code=input("Enter Stock Code:")  
unit=int(input("Enter Total Unit:"))
price=float(input("Enter Price per Unit:"))
brand=input("Enter Brand:")
     
sys=NavSys(code,unit,price,brand)

print(f"\nCreating a stock with {sys.getStockQuantity()} units {sys.getStockName()}, price {sys.getStockPrice()} each, and item code {sys.getStockCode()}")
print(sys)

print("Edit:")
print("1)Quantity Increment")
print("2)Quantity Decrement")
print("3)Set New Price Per Unit")
choice=int(input("Select Option:"))

match(choice):
    case 1:
        add=int(input("\nEnter additional units:"))
        print(f"\nIncreasing {add} more units")
        if sys.increaseStock(add)==True:
            print(sys)

    case 2:
        sell=int(input("\nEnter sold units:"))
        print(f"\nSold {sell} units")
        if sys.sellStock(sell)==True:
            print(sys)

    case 3:
        new_price=float(input("\nSet new price per unit:"))
        sys.setStockPrice(new_price)
        print(f"\nSet new price {new_price:.2f} per unit")
        print(sys)
        
    case _:
        print("Invalid")