import tkinter as tk
from tkinter import messagebox,ttk
import time
import Windows.Calculator as Calculator
import Windows.Home as Home
import Windows.Animation as ani

def simulation_page():#Code for simulation page
    sim_pg = tk.Tk()
    sim_pg.geometry('800x600')
    sim_pg.title('Simulator')

    #Defining Varaibles
    selected_mat = tk.Variable(value="Aluminium (205)")
    Temp_1 = tk.StringVar(value=100)
    Temp_2 = tk.StringVar(value= 0.0)
    Length = tk.StringVar(value=5)
    Width = tk.StringVar(value=0.6)
    Height = tk.StringVar(value=0.4)

    #Materials List
    conductivity = {  
    "Aerogel (0.013)": 0.013,  
    "Aluminium (205)": 205,  
    "Copper (393)": 393,  
    "Diamond (2000)": 2000,  
    "Firebrick (0.4)": 0.4,  
    "Glass (1)": 1,  
    "Gold (310)": 310,  
    "Ice (2.4)": 2.4,  
    "Mild Steel (50)": 50,  
    "Silver (406)": 406,  
    "Stainless Steel (15)": 15  
}  

    def close_sim():
        sim_pg.destroy()
        Home.home()


    def simulate():
        try:
            #Getting values and preventing blank inputs, defaults to zero if blank except length (defaults to 1)
            T1 = float(Temp_1.get()) if Temp_1.get() != "" else (Temp_1.set(0.0) or 0.0)
            T2 = float(Temp_2.get()) if Temp_2.get() != "" else (Temp_2.set(0.0) or 0.0)
            L = float(Length.get()) if Length.get() != "" or Length.get() == 0 else (Length.set(1) or 1)
            W = float(Width.get()) if Width.get() != "" else (Width.set(0.0) or 0.0)
            H = float(Height.get()) if Height.get() != "" else (Height.set(0.0) or 0.0)
            sim_pg.update()

            if L == 0 : #Preventing div/0
                raise ZeroDivisionError('Length cannot be Zero')
            
            #Getting material and its conductivity
            mat = selected_mat.get()
            k = conductivity.get(mat)

        
            #Additional maths
            dT = T1 - T2 #change in temp
            A = W*H # X sec area

            #Heat flow rate for simulation
            Q = (k*A*dT)/L
            messagebox.showinfo("Output",f"Variables:\nT1:{T1} \nT2:{T2}\nL:{L} \nW:{W} \nH:{H} \nMaterial:{mat} \nConductivity:{k}\ndt:{dT}\nA:{A}\nQ:{Q:.3f}")
        
            ani.simulate(H,L)#plotting graph for animation

        except Exception as MiscErr: #misc errors, gives a detailed readout for troubleshooting
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(MiscErr).__name__, MiscErr.args)
            messagebox.showerror("error", message)
            print(f"Error readout\n{message}\n")





    #input validation, preventing non number inputs
    def callback(input):
        if input == "" or input == "-": #Allow for user to delete input and input "-"
            return True
        try:
            float(input)#Checks input is a float
            return True
        except ValueError:# dissallows other input
            return False
       
    validate_inp= sim_pg.register(callback)


    #Inputs
    mat_lbl = ttk.Label(sim_pg,text="Select Material\n(Thermal conductivity in W/mK)",justify="center").grid(row=0,column=0)
    mat_dropdown = ttk.Combobox(sim_pg,textvariable=selected_mat,values=[
        "Aerogel (0.013)", "Aluminium (205)", "Copper (393)", "Diamond (2000)",
        "Firebrick (0.4)", "Glass (1)", "Gold (310)", "Ice (2.4)", "Mild Steel (50)", 
        "Silver (406)", "Stainless Steel (15)"],state='readonly')
    mat_dropdown.grid(row=0,column=1)

    Temp1_lbl = ttk.Label(sim_pg,text="Starting Temperature (K)").grid(row=1,column=0)
    Temp1_inp = ttk.Entry(sim_pg,textvariable=Temp_1,validate="key",validatecommand=(validate_inp,"%P")).grid(row=1,column=1)
    Temp_2_lbl = ttk.Label(sim_pg,text="End Temperature (K)").grid(row=2,column=0)
    Temp_2_inp = ttk.Entry(sim_pg, textvariable=Temp_2,validate="key",validatecommand=(validate_inp,"%P")).grid(row=2,column=1)

    Length_lb = ttk.Label(sim_pg, text="Bar Length (m)").grid(row=3,column=0)
    Length_inp = ttk.Entry(sim_pg, textvariable=Length,validate="key",validatecommand=(validate_inp,"%P")).grid(row=3,column=1)
    Width_lbl =ttk.Label(sim_pg,text="Bar Width (m)").grid(row=4,column=0)
    Width_inp = ttk.Entry(sim_pg, textvariable= Width,validate="key",validatecommand=(validate_inp,"%P")).grid(row=4,column=1)
    Height_lb =ttk.Label(sim_pg,text='Bar Height (m)').grid(row=5,column=0)
    Height_inp = ttk.Entry(sim_pg,textvariable=Height,validate="key",validatecommand=(validate_inp,"%P")).grid(row=5,column=1)

    #Simulate Button:
    simulate_bttn = ttk.Button(sim_pg,text='Simulate',command=simulate).grid(row=6,column=0,columnspan=2)

    ExitSimBttn = ttk.Button(sim_pg, text="Exit Simulator", command=close_sim).grid(row=7,column=0,columnspan=2)
    sim_pg.mainloop()