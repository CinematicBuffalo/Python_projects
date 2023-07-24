#This program is the class were the the cost, weightInOunces, size and description and quantity is private
# File: JaydenOrderReceiptList.py
# Project: CSIS2101 Assignment 11
# Author:  Jayden Alexander 
# History: Version 3.10

class Apparel:
    #initilz funtion
    def __init__(self,c,w,s,d):

        self.__cost= c
        self.__weight=w
        self.__size=s
        self.__description=d
        self.__quantity = 1

    #get funtions

    def get_cost(self):
        return self.__cost

    def get_weight(self):
        return self.__weight

    def get_size(self):
        return self.__size

    def get_description(self):
        return self.__description

    def get_quantity(self):
        q = self.__quantity
        return q
    
    #set funtions

    def set_cost(self,c):
        self.__cost = c

    def set_weight(self,w):
        self.__weigth = w

    def set_size(self,s):
        self.__size = s

    def set_description(self,d):
        self.__description = d
    #quantity values is changed
    def set_quantity(self,q):
        self.__quantity = q//self.__quantity
        
        
        
        
    
    #operations
        
    def get_order_cost(self):
        return self.__quantity * self.__cost


    def get_order_weight_in_ounces(self):
        return self.__quantity * self.__weight

    #string finish str

    def __str__(self):
        ret_str=""
        ret_str ="\n" "$" + str(self.__cost) + " for " + str(self.__quantity)+ " " + self.__size +" "+ self.__description + "\n"
        return ret_str

        
        
        
    
