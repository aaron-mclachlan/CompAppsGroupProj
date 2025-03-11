import tkinter as tk
from tkinter import messagebox,ttk
import time

def calculator(): #Code for calculator window:
    window = tk.Tk()
    window.geometry('800x600')  # def window
    window.title('Conduction Calculator')

    default_font = "Arial", 12  # to set a default font

    # Defining Variables:
    user_temp1 = tk.DoubleVar()
    user_temp2 = tk.DoubleVar()
    bar_length = tk.DoubleVar()
    bar_width = tk.DoubleVar()
    bar_height = tk.DoubleVar()
    thermal_conductivity = tk.DoubleVar()
    heat_flow = tk.DoubleVar()
    
    variable_to_solve = tk.StringVar(value="Q")

    #Defining maths equations to be used:
    def solve_for_Q(k, A, delta_T, L):

        if L == 0:
            raise ValueError("Length cannot be zero.")#preventing div/zero errors
        return (k * A * delta_T) / L

    def solve_for_k(Q, A, delta_T, L):
        if A == 0 or delta_T == 0 or L == 0:
            raise ValueError("Width, height, temperature difference, and length cannot be zero.")#for /0 errors 
        return (Q * L) / (A * delta_T)

    def solve_for_L(Q, k, A, delta_T):
        if k == 0 or A == 0 or delta_T == 0:
            raise ValueError("Thermal conductivity, width, height, and temperature difference cannot be zero.")#for /0 errors 
        return (k * A * delta_T) / Q


    def calculate(): #Defining what happens when calculate button is pressed
        try: #error handling start

            #assiging values from variables:
            T1, T2, L, W, H, k, Q = (
                user_temp1.get(), user_temp2.get(), bar_length.get(),
                bar_width.get(), bar_height.get(), thermal_conductivity.get(), heat_flow.get()
            )
        
            # Pre calculations to simplify maths later
            A = W * H  # Cross-sectional area
            delta_T = abs(T1 - T2) #change in temp
            solve_for = variable_to_solve.get() #getting variable to solve for

            #Checking what to solve for and performing calculation:
            if solve_for == "Q":
                result = solve_for_Q(k, A, delta_T, L)
                heat_flow.set(result)
            elif solve_for == "k":
                result = solve_for_k(Q, A, delta_T, L)
                thermal_conductivity.set(result)
            elif solve_for == "L":
                result = solve_for_L(Q, k, A, delta_T)
                bar_length.set(result)
            else:
                raise ValueError("Invalid selection.")
            
            #Messagebox for output:
            messagebox.showinfo("Result", f"Calculated {solve_for} to be {result:.3f}")

            #Error Exceptions
        except tk.TclError as blank_input_err: #blank inputs
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(blank_input_err).__name__, blank_input_err.args)
            print("\n",message)
            messagebox.showerror("error",'Please ensure that there are no blank inputs')
            
        except Exception as MiscErr: #misc errors, gives a detailed readout for troubleshooting
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(MiscErr).__name__, MiscErr.args)
            messagebox.showerror("error", message)
            print("\n",message)
            

    #Selecting what to solve for
    ttk.Label(window, text="Solve for:").grid(row=0, column=0)
    ttk.Combobox(window, textvariable=variable_to_solve, values=["Q", "k", "L"],state='readonly').grid(row=0, column=1)
    
    # Inputs & labels
    ttk.Label(window, text="Temp 1:").grid(row=1, column=0)
    ttk.Entry(window, textvariable=user_temp1).grid(row=1, column=1)
    ttk.Label(window, text="Temp 2:").grid(row=2, column=0)
    ttk.Entry(window, textvariable=user_temp2).grid(row=2, column=1)
    ttk.Label(window, text="Length (L):").grid(row=3, column=0)
    ttk.Entry(window, textvariable=bar_length).grid(row=3, column=1)
    ttk.Label(window, text="Width:").grid(row=4, column=0)
    ttk.Entry(window, textvariable=bar_width).grid(row=4, column=1)
    ttk.Label(window, text="Height:").grid(row=5, column=0)
    ttk.Entry(window, textvariable=bar_height).grid(row=5, column=1)
    ttk.Label(window, text="Thermal Conductivity (k):").grid(row=6, column=0)
    ttk.Entry(window, textvariable=thermal_conductivity).grid(row=6, column=1)
    ttk.Label(window, text="Heat Flow (Q):").grid(row=7, column=0)
    ttk.Entry(window, textvariable=heat_flow).grid(row=7, column=1)
    
    ttk.Button(window, text="Calculate", command=calculate).grid(row=8, column=0, columnspan=2)
    
    window.mainloop()

calculator()

        



