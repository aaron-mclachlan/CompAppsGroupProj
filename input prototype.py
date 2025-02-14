from tkinter import ttk, messagebox
import tkinter as tk


window = tk.Tk()

window.geometry('800x600')#def window
window.title('Conduction Simulator')


user_temp = tk.Variable() #def user temp input
def submit(): #def function for submit button
    mtl1 = mtl1_menu.get()
    mtl2 = mtl2_menu.get()
    temp = user_temp.get()

    #messsage box showing output values (Placeholder for future)
    messagebox.showinfo(
        message=f"""Metal 1: {mtl1}
        Metal 2: {mtl2}
        Temperature: {temp}"""
    )

    print(f'Metal 1 is: {mtl1}')
    print(f'Metal 2 is: {mtl2}')
    print(f'Temperature: {temp}')
   



Metal1_lbl = tk.Label(window, text='Metal 1').grid(row=0, column=0)#Text label for meltal 1
#metal 1 dropdown
mtl1_menu = ttk.Combobox(
    state='readonly',
    values =['Copper','Iron','Aluminium']  
)
mtl1_menu.grid(row=1,column=0) 


Metal2_lbl = tk.Label(window, text='Metal 2').grid(row=0, column=2)#text label for metal 2
#metal 2 dropdown
mtl2_menu = ttk.Combobox(
    state='readonly',
    values =['Copper','Iron','Aluminium']  
)
mtl2_menu.grid(row=1,column=2) 


Temp_lbl = tk.Label(window, text='Select Temperature').grid(row=0,column=4)#text label for temperature
temp_input = tk.Entry(window,textvariable=user_temp).grid(row=1, column=4)#user input for temperature






enter_bttn = tk.Button(window,text='Submit',command=submit).grid(row=2)#enter button




window.mainloop()