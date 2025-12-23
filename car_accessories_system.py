class StockItem:
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
        return self.__stock_name
    
    def getStockDescription(self):
        return self.__stock_desc