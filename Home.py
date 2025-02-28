import tkinter as tk
from tkinter import messagebox,ttk
import time
import Theory_Page as theory
import Calculator

def home():# code for home page
    homewindow = tk.Tk()

    homewindow.geometry('800x600')
    homewindow.title('Home Menu')


    def sim_bttn():
      homewindow.destroy()
      Calculator.calculator()
    
    def theorypg_bttn():
        homewindow.destroy()
        theory.theory_page()

    simulator_bttn = tk.Button(homewindow,text="Open Calculator",command=sim_bttn).grid(row=0,column=0)
    theory_bttn = tk.Button(homewindow, text='Open theory page',command=theorypg_bttn).grid(row=0, column=1)


    homewindow.mainloop()
