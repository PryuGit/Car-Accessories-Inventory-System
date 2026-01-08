from NavSys import NavSys

def SaveStockToFile(sys):
    try:
        with open('StockItem.txt','w') as file:
            file.write(f"Stock Code: {sys.getStockCode()}\n")
            file.write(f"Stock Category: {sys.stock_category}\n")
            file.write(f"Brand: {sys.getBrand()}\n")
            file.write(f"Name:{sys.getStockName()}\n")
            file.write(f"Description: {sys.getStockDescription()}\n")
            file.write(f"Quantity: {sys.getStockQuantity()}\n")
            file.write(f"Price per Unit: {sys.getStockPrice():.2f}\n")
            file.write(f"Price with VAT (per unit): {sys.getPriceWithVAT():.2f}\n")
    except Exception as e:
        print(f"Error:{e}")

def LoadStockFromFile(sys):
    try:
        with open('StockItem.txt','r') as file:
            content=file.read()
            print(content)
    except Exception as e:
        print(f"Error:{e}")
               
#Main Program
def main():    
    print("\nCar Parts and Accessories Management System\n")    
    code=input("Enter Stock Code:")  
    unit=int(input("Enter Total Unit:"))
    price=float(input("Enter Price per Unit:"))
    brand=input("Enter Brand:")
        
    sys=NavSys(code,unit,price,brand)

    print(f"\nCreating a stock with {sys.getStockQuantity()} units {sys.getStockName()}, price {sys.getStockPrice()} each, and item code {sys.getStockCode()}")
    print(sys)
    SaveStockToFile(sys)

    print("Edit:")
    print("1)Quantity Increment")
    print("2)Quantity Decrement")
    print("3)Set New Price Per Unit")
    choice=int(input("Select Option:"))

    match(choice):
        case 1:
            add_stock=int(input("\nEnter additional units:"))
            print(f"\nIncreasing {add_stock} more units")
            if sys.increaseStock(add_stock)==True:
                print(sys)
                SaveStockToFile(sys)

        case 2:
            sell_stock=int(input("\nEnter sold units:"))
            print(f"\nSold {sell_stock} units")
            if sys.sellStock(sell_stock)==True:
                print(sys)
                SaveStockToFile(sys)

        case 3:
            new_price=float(input("\nSet new price per unit:"))
            sys.setStockPrice(new_price)
            print(f"\nSet new price {new_price:.2f} per unit")
            print(sys)
            SaveStockToFile(sys)
            
        case _:
            print("Invalid")

    LoadStockFromFile(sys)
if __name__=='__main__':
    main()
                