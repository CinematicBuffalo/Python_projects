#CSIS2101_assgn12
#this program will calculate yor speeding fine and output the fine using GUI
# File:    Alexander_speedLimit.py
# Project: Assignment 12
# Author:  Jayden Alexander 
# History: Version 3.10

import tkinter
import tkinter.messagebox
class speedlimit_GUI:
    
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.title("Speeding ticket fine Calculator")
        #input frames 1-3
        self.top_frame = tkinter.Frame(self.main_window)
        self.top_frame_sp = tkinter.Frame(self.main_window)
        self.top_frame_sz = tkinter.Frame(self.main_window)
        
        #fine frame
        self.middle_frame = tkinter.Frame(self.main_window)
        
        #buttons frame
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        #speed limit entry
        self.prompt_label  = tkinter.Label(self.top_frame,
                                    text = "Speed Limit")

        self.sl_entry = tkinter.Entry(self.top_frame,
                                        width = 10)
        #speed of vehicle label and entry
        self.prompt_label_sp = tkinter.Label(self.top_frame_sp,
                                    text = "Vehicle speed")

        self.sp_entry = tkinter.Entry(self.top_frame_sp,
                                        width = 10)
        
        #school zone label and entry
        self.prompt_label_sz = tkinter.Label(self.top_frame_sz,
                                    text = "School zone(yes,y,no)")

        self.sz_entry = tkinter.Entry(self.top_frame_sz,
                                        width = 10)
        
        
        #pack the labels and entry point

        self.prompt_label.pack(side = "left")
        self.sl_entry.pack(side = "left")
        
        self.prompt_label_sp.pack(side = "left")
        self.sp_entry.pack(side = "left")

        self.prompt_label_sz.pack(side = "left")
        self.sz_entry.pack(side = "left")
        
        self.desc_label = tkinter.Label(self.middle_frame,
                                        text = "calculated speeding fine")
        #string var object
        self.value = tkinter.StringVar()

        self.celsius_label = tkinter.Label(self.middle_frame,
                                           textvariable = self.value)
        self.desc_label.pack(side ="left")
        self.celsius_label.pack(side="left")
        
         
        #calculate fine button and quit button
        self.button1 = tkinter.Button(self.bottom_frame,
                                      text = "calculate trafic ticket",
                                      command = self.convert)

        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text="Quit",
                                          command = self.main_window.destroy)
        #Packs button
        self.button1.pack(side = "left")
        self.quit_button.pack(side = "left")
        
        #packs
        self.top_frame.pack()
        self.top_frame_sp.pack()
        self.top_frame_sz.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
    #Calculations
    def convert(self):
        
        #get the value in entry point
        speed_limit = float(self.sl_entry.get() )
        speed_vehicle = float(self.sp_entry.get() )
        school_zone =(self.sz_entry.get() )
        
        mph =speed_vehicle - speed_limit
   

        if mph <= 0:
            fine = 0
            #a="Your a good driver"
        elif mph < 10:
            fine = 69.50
            a="Slow down!"
        elif mph < 20:
            fine = 99.50 
            #a="drive with caution!"
        elif mph < 30:
            fine = 129.50
            #a = "You are in danger zone!"
        elif mph < 35:
            fine = 149.50
            #a = "You are over speeding!"
        elif mph >=35:
            fine = (" - Court mandatory fine will be decided in court")
            #a = "see you in court!"
        
        if school_zone == "y" or school_zone == "yes":
           fine*=2
        elif school_zone == "n" or school_zone == "no":
            fine*=1
        else:
            school_zone =("invalid input considered yes")
            fine*=2
            
        self.value.set(fine)
        
       
if __name__ == "__main__":
    my_gui=speedlimit_GUI()
        
