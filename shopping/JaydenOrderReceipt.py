
#This program is the main given for the Apperal class
# File: JaydenOrderReceipt.py
# Project: CSIS2101 Assignment 11
# Author:  Jayden Alexander 
# History: Version 3.10

import Apparel

def main():
    dTotalCost = 0.0         
    iTotalWeight = 0
    # Put the 4 apparels being ordered in apparel1 through apparel 4         
    apparel1 = Apparel.Apparel(18.99, 27, "Large", "Denim Jacket")         
    apparel2 = Apparel.Apparel(9.49, 15, "Medium", "Track Pants")         
    apparel3 = Apparel.Apparel(109.99, 35, "Small", "Cashmere Sweater")         
    apparel4 = Apparel.Apparel(5.49, 7, "X-Large", "Woolen Socks")   
    apparel2.set_quantity(3)      
    apparel4.set_quantity(2)   
    # Show the details of the order using:         
    print("Here are your shopping cart contents.")         
    print(apparel1)         
    print(apparel2)
    print(apparel3)         
    print(apparel4) 
    # Compute the total cost and total weight in this section        
    dTotalCost += apparel1.get_order_cost()         
    dTotalCost += apparel2. get_order_cost()         
    dTotalCost += apparel3. get_order_cost()         
    dTotalCost += apparel4. get_order_cost()         
    iTotalWeight += apparel1.get_order_weight_in_ounces()        
    iTotalWeight += apparel2. get_order_weight_in_ounces ()         
    iTotalWeight += apparel3. get_order_weight_in_ounces ()         
    iTotalWeight += apparel4. get_order_weight_in_ounces ()         
    # Here we show the order details        
    print(f"The cost of your order is ${dTotalCost:0.2f}")        
    print(f"The shipping weight is {iTotalWeight // 16} pounds {iTotalWeight % 16} ounces")     
    #End of main
   
if __name__ == "__main__":

          main()
