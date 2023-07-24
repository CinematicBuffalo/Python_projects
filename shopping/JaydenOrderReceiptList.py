
#This program is the main were a list is used to get to get the output
# File: JaydenOrderReceiptList.py
# Project: CSIS2101 Assignment 11
# Author:  Jayden Alexander 
# History: Version 3.10

import Apparel

def main():
    dTotalCost = 0.0         
    iTotalWeight = 0

    apparel1 = Apparel.Apparel(18.99, 27, "Large", "Denim Jacket")         
    apparel2 = Apparel.Apparel(9.49, 15, "Medium", "Track Pants")         
    apparel3 = Apparel.Apparel(109.99, 35, "Small", "Cashmere Sweater")         
    apparel4 = Apparel.Apparel(5.49, 7, "X-Large", "Woolen Socks")   
    apparel2.set_quantity(3)      
    apparel4.set_quantity(2)
    #list of apparel 1-4
    apparel_list = [apparel1,apparel2,apparel3,apparel4]
#for loop that iterates through list
    print("Here are your shopping cart contents.")
    for a in apparel_list:
    
        dTotalCost += a.get_order_cost()
        iTotalWeight += a.get_order_weight_in_ounces()
        print(a)

    print(f"The cost of your order is ${dTotalCost:0.2f}")        
    print(f"The shipping weight is {iTotalWeight // 16} pounds {iTotalWeight % 16} ounces")
        
if __name__ == "__main__":

          main()
        
