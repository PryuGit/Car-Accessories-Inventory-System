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
        if amount < 1:
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