import tkinter as tk
from tkinter import messagebox,ttk
import time
import Windows.Home as Home

def theory_page():#code for theory page
    theory_window = tk.Tk()
    theory_window.geometry('800x600')
    theory_window.title('Theory of Heat transfer')

    def home_from_theory():
        theory_window.destroy()
        Home.home()
    
    home_bttn = ttk.Button(theory_window, text='Return home',command=home_from_theory).grid(row=0,column=0)
    theory_window.mainloop()