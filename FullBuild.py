import tkinter as tk
from tkinter import messagebox,ttk
def home():
    homewindow = tk.Tk()

    homewindow.geometry('800x600')
    homewindow.title('Home Menu')


    def sim_bttn():
      homewindow.destroy()
      inputwindow()
      

    simulator_bttn = tk.Button(homewindow,text="Open Simulator",command=sim_bttn).grid(row=0,column=0)
    theory_bttn = tk.Button(homewindow, text='Theory').grid(row=0, column=1)
    homewindow.mainloop()

def inputwindow():

    window = tk.Tk()
    window.geometry('800x600')#def window
    window.title('Conduction Simulator')
    user_temp = tk.Variable() #def user temp input
    def submit(): #def function for submit button
        mtl1 = mtl1_menu.get()
        temp = user_temp.get()

        #messsage box showing output values (Placeholder for future)
        messagebox.showinfo(
            message=f"""Metal 1: {mtl1}
            Temperature: {temp}"""
        )

        print(f'Metal 1 is: {mtl1}')
        print(f'Temperature: {temp}')

        mtl1_menu.set('')
        user_temp.set('')


    Metal1_lbl = tk.Label(window, text='Metal 1').grid(row=0, column=0)#Text label for meltal 1
    #metal 1 dropdown
    mtl1_menu = ttk.Combobox(
        window,
        state='readonly',
        values =['Copper','Iron','Aluminium']  
    )
    mtl1_menu.grid(row=1,column=0) 
    
    Temp_lbl = tk.Label(window, text='Select Temperature').grid(row=0,column=2)#text label for temperature
    temp_input = tk.Entry(window,textvariable=user_temp).grid(row=1, column=2)#user input for temperature
    enter_bttn = tk.Button(window,text='Submit',command=submit).grid(row=2)#enter button
    window.mainloop()

home()