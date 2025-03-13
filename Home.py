import tkinter as tk
from tkinter import messagebox,ttk
import time
import Theory_Page as theory
import Calculator
import Simulator as sim

def home():# code for home page
    homewindow = tk.Tk()

    homewindow.geometry('800x600')
    homewindow.title('Home Menu')


    def calc_bttn():
      homewindow.destroy()
      Calculator.calculator()
    
    def theorypg_bttn():
        homewindow.destroy()
        theory.theory_page()

    def sim_bttn():
       homewindow.destroy()
       sim.simulation_page()

    calculator_bttn = ttk.Button(homewindow,text="Open Calculator",command=calc_bttn).grid(row=0,column=0)
    simulator_bttn = ttk.Button(homewindow,text="Open Simulator", command= sim_bttn).grid(row=0,column=1)
    theory_bttn = ttk.Button(homewindow, text='Open theory page',command=theorypg_bttn).grid(row=0, column=2)



    homewindow.mainloop()
