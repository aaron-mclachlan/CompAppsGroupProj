import tkinter as tk
from tkinter import messagebox,ttk
import time
import Calculator
import Home

def simulation_page():#Code for simulation page
    sim_pg = tk.Tk()
    sim_pg.geometry('800x600')
    sim_pg.title('Simulator')

    def close_sim():
        sim_pg.destroy()
        Home.home()

    ExitSimBttn = tk.Button(sim_pg, text="Exit Simulator", command=close_sim).grid(row=0,column=0)
    sim_pg.mainloop()