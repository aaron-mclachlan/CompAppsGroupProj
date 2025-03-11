import tkinter as tk
from tkinter import messagebox,ttk
import time
import Theory_Page as theory
import Home
import Simulator


def calculator():#code for calculator page

    window = tk.Tk()
    window.geometry('800x600')#def window
    window.title('Conduction Calculator')
    user_temp1 = tk.IntVar() #def user inputs
    user_temp2 = tk.IntVar()
    bar_length = tk.IntVar()
    bar_width  = tk.IntVar()
    bar_height = tk.IntVar()


    def submit(): #def function for submit button
        mtl1 = mtl1_menu.get()
        temp1 = user_temp1.get()
        temp2 = user_temp2.get()
        length = bar_length.get()
        width = bar_width.get()
        height = bar_height.get()
        #messsage box showing output values (Placeholder for future)
        messagebox.showinfo(
            message=f"""Metal 1: {mtl1}
            Starting Temperature: {temp1}
            Final Temperature: {temp2} 
            Bar Length: {length}
            Bar Width: {width}
            Bar Height: {height}"""
        )


        mtl1_menu.set('')
        user_temp1.set('')
        Simulator.simulation_page() #parse calculator values in future through here
    def returnhome():
        window.destroy()
        Home.home()
    
    #metal 1 dropdown
    Metal1_lbl = tk.Label(window, text='Metal 1')
    mtl1_menu = ttk.Combobox(
        window,
        state='readonly',
        values =['Copper','Iron','Aluminium', 'Titanium', 'Steel']  
    )

    #Starting Temp    
    Temp1_lbl = tk.Label(window, text='Enter Starting Temperature:')#text label for temperature
    temp_input1 = tk.Entry(window,textvariable=user_temp1)#user input for temperature


    #Final Temp
    Temp2_lbl = tk.Label(window, text="Enter Final Temperature:" )
    temp_input2 = tk.Entry(window,textvariable=user_temp2)

    #Bar Dimensions
    leng_lbl = tk.Label(window, text="Enter Bar length:")#Bar length
    leng_inp = tk.Entry(window,textvariable=bar_length)

    width_lbl = tk.Label(window, text="Enter Bar width:")#Bar width
    width_inp = tk.Entry(window, textvariable=bar_width)

    height_lbl = tk.Label(window, text="Enter Bar height:")#Bar height
    height_inp = tk.Entry(window, textvariable=bar_height)
    #Enter button
    enter_bttn = tk.Button(window,text='Submit',command=submit)

    #Return Home
    homebttn = tk.Button(window,text="Return Home",command=returnhome)

#Grid Layout
    def input_window_layout():
        #Lables
        Metal1_lbl.grid(row=0,column=0)
        Temp1_lbl.grid(row=0,column=1)
        Temp2_lbl.grid(row=0,column=2)
        leng_lbl.grid(row=2,column=0)
        width_lbl.grid(row=2,column=1)
        height_lbl.grid(row=2,column=2)
    
        #Inputs
        mtl1_menu.grid(row=1, column=0)
        temp_input1.grid(row=1, column=1)
        temp_input2.grid(row=1, column=2)
        leng_inp.grid(row=3, column=0)
        width_inp.grid(row=3, column=1)
        height_inp.grid(row=3,column=2)

        #Submit
        enter_bttn.grid(row=4,column=0)

        #Home
        homebttn.grid(row=5, column=0)
    
    input_window_layout()
    window.mainloop()

    