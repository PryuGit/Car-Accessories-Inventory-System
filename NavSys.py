from StockItem import StockItem
        
#Inheritance from Parent Class 'StockItem' to Child Class 'NavSys' 
class NavSys(StockItem):
    """
    Docstring for NavSys
    """
    
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