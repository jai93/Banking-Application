
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import *
import pickle

def main_page():
    window = tk.Tk()
    
    # get screen width and height
    ws = window.winfo_screenwidth() # width of the screen
    hs = window.winfo_screenheight() # height of the screen
    
    w = 800 # width for the Tk root
    h = 800 # height for the Tk root
    
    # calculate x and y coordinates for the Tk root window
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
      

    window.title("Bank application")
    
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    window.configure(background='LightSkyBlue4')

    
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)
    
    
    title = tk.Label(window, text="Bank Application" ,bg="light sea green"  ,fg="white"  ,width=30  ,height=1,font=('times', 22, 'italic bold ')) 
    
    title.place(x=170, y=10)
  
    # ===================== sex setting ================
    # sex label 
    message = tk.Label(window, text="sex:" ,bg="light sea green"  ,fg="white"  ,width=8  ,height=1,font=('times', 16 )) 
    message.place(x=10, y=125)
    
    # create combobox object 

    combo_male = ttk.Combobox(window, 
                            values=[
                                    "male", 
                                    "female",
                                    ], font=('times', 16))
    combo_male.place(x=100, y=125)
    combo_male.current(0)  #default value of combo box
    
    #===============================================
    
    
    # ===================== merchant setting ================
    # merchant label 
    message = tk.Label(window, text="merchant:" ,bg="light sea green"  ,fg="white"  ,width=8  ,height=1,font=('times', 16 )) 
    message.place(x=10, y=200)
    
    # create combobox object 

    combo_merchant = ttk.Combobox(window, 
                            values=['M1823072687', 'M349281107', 'M348934600', 'M45060432', 'M1352454843', 'M85975013', 'M1053599405', 'M480139044'],
                                     font=('times', 16))
    combo_merchant.place(x=100, y=200)
    combo_merchant.current(0)  #default value of combo box
    
    #===============================================
    
    # ===================== age setting ================
    # age label 
    message = tk.Label(window, text="age:" ,bg="light sea green"  ,fg="white"  ,width=8  ,height=1,font=('times', 16 )) 
    message.place(x=10, y=275)
    
    # create combobox object 

    combo_age= ttk.Combobox(window, 
                            values=['1', '2', '3', '4', '5', '6'],
                                     font=('times', 16))
    combo_age.place(x=100, y=275)
    combo_age.current(2)  #default value of combo box
    
    #===============================================    
    
    
    
    # ===================== category setting ================
    # category label 
    message = tk.Label(window, text="category:" ,bg="light sea green"  ,fg="white"  ,width=8  ,height=1,font=('times', 16 )) 
    message.place(x=10, y=350)
    
    # category combobox object 

    combo_category= ttk.Combobox(window, 
                            values=['es_transportation', 'es_health', 'es_food','es_sportsandtoys','es_barsandrestaurants','es_hyper'

                            ,'es_wellnessandbeauty' ,'es_fashion','es_barsandrestaurants' ],
                                     font=('times', 16))
    combo_category.place(x=100, y=350)
    combo_category.current(2)  #default value of combo box
    
    #===============================================
    
    
    # ===================== amount setting ================
    # amount label 
    message = tk.Label(window, text="amount:" ,bg="light sea green"  ,fg="white"  ,width=6  ,height=1,font=('times', 16 )) 
    message.place(x=10, y=425)
    
    # es_transportation combobox object 
    v = tk.StringVar()
    amount_edit= tk.Entry(window,width=20  ,bg="light yellow" ,fg="black",font=('times', 15, ' bold '),textvariable=v)
    
    amount_edit.place(x=100, y=425)
    v.set('50')
      #default value of combo box
    
    #===============================================    
    
    
    # ===================== name setting ================
    # amount label 
    message = tk.Label(window, text="name:" ,bg="light sea green"  ,fg="white"  ,width=6  ,height=1,font=('times', 16 )) 
    message.place(x=400, y=125)
    
    # es_transportation combobox object 
    v = tk.StringVar()
    name_edit= tk.Entry(window,width=20  ,bg="light yellow" ,fg="black",font=('times', 15, ' bold '),textvariable=v)
    
    name_edit.place(x=500, y=125)
    v.set('Andrew')
      #default value of combo box
    
    #===============================================     

    # ===================== address setting ================
    # amount label 
    message = tk.Label(window, text="address:" ,bg="light sea green"  ,fg="white"  ,width=6  ,height=1,font=('times', 16 )) 
    message.place(x=400, y=200)
    
    # es_transportation combobox object 
    v = tk.StringVar()
    address_edit= tk.Entry(window,width=20  ,bg="light yellow" ,fg="black",font=('times', 15, ' bold '),textvariable=v)
    
    address_edit.place(x=500, y=200)
    v.set('1747 Linden Avenue')
    #default value of combo box
    
    #===============================================    

    # ============= status label ===================
    status = tk.Label(window, text="" ,bg="light sea green"  ,fg="white"  ,width=30  ,height=1,font=('times', 16, 'italic bold ')) 
    
    status.place(x=230, y=600)
    
    # ==============================================
    
  
    def fraud_detection():
        #window.destroy() 
        age = int(combo_age.get())
        male = combo_male.current()
        amount = int(amount_edit.get()) 
        
        merchant = combo_merchant.current()
        category = combo_category.current()
        
        
        filename = 'finalized_model.sav'
        # load the model from disk
        loaded_model = pickle.load(open(filename, 'rb'))
        
        X_test=np.array([age,male,amount,merchant,category]).reshape(1,-1);
        
        print(X_test)
        y_pred = loaded_model.predict(X_test)
        
        if  y_pred:
            res = 'The fraud is detected'
        else: 
            res = 'The fraud is not detected'
        status.configure(text= res) 
        
    
    OK_button = tk.Button(window, text="Ok", command=fraud_detection  ,fg="black"  ,bg="gray40"  ,width=15  ,height=2, activebackground = "gray30" ,font=('times', 15, ' bold '))
    OK_button.place(x=300, y=720)
    
    #main_window = tk.Button(window, text="Main Window", command=mainWindow  ,fg="black"  ,bg="gray40"  ,width=15  ,height=2, activebackground = "gray30" ,font=('times', 15, ' bold '))
    #main_window.place(x=500, y=420)    
    
    window.mainloop()
main_page()