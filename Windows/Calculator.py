import tkinter as tk
from tkinter import messagebox,ttk
import time
import Windows.Home as Home

#Defining calculator commands
def solve_for_Q(k, A, delta_T, L):
        if L == 0:
         raise ZeroDivisionError("Length cannot be zero.")
        return (k * A * delta_T) / L

def solve_for_k(Q, A, delta_T, L):
    if A == 0 or delta_T == 0 or L == 0:
        raise ZeroDivisionError("Area, temperature difference, and length cannot be zero.")
    return (Q * L) / (A * delta_T)

def solve_for_L(Q, k, A, delta_T):
    if k == 0 or A == 0 or delta_T == 0:
        raise ZeroDivisionError("Thermal conductivity, area, and temperature difference cannot be zero.")
    return (k * A * delta_T) / Q

def solve_for_T1(T2, Q, k, W, H, L):
    delta_T = solve_for_delta_T(Q, k, W, H, L)
    return T2 + delta_T

def solve_for_T2(T1, Q, k, W, H, L):
    delta_T = solve_for_delta_T(Q, k, W, H, L)
    return T1 - delta_T

def solve_for_delta_T(Q, k, W, H, L):
    A = W * H
    if k == 0 or A == 0 or L == 0:
        raise ZeroDivisionError("Thermal conductivity, area, and length cannot be zero.")
    return Q * L / (k * A)

def solve_for_width(Q, k, H, delta_T, L):
    if k == 0 or H == 0 or delta_T == 0 or L == 0:
         raise ZeroDivisionError("Thermal conductivity, height, temperature difference, and length cannot be zero.")
    return (Q * L) / (k * H * delta_T)

def solve_for_height(Q, k, W, delta_T, L):
    if k == 0 or W == 0 or delta_T == 0 or L == 0:
        raise ZeroDivisionError("Thermal conductivity, width, temperature difference, and length cannot be zero.")
    return (Q * L) / (k * W * delta_T)


def calculator(): #Code for calculator window:
    window = tk.Tk()
    window.geometry('800x600')  # def window
    window.title('Conduction Calculator')


    # Defining Variables:
    user_temp1 = tk.StringVar(value=0.0)
    user_temp2 = tk.StringVar(value=0.0)
    delta_T = tk.StringVar(value=0.0)
    bar_length = tk.StringVar(value=0.0)
    bar_width = tk.StringVar(value=0.0)
    bar_height = tk.StringVar(value=0.0)
    thermal_conductivity = tk.StringVar(value=0.0)
    heat_flow = tk.StringVar(value=0.0)
    
    variable_to_solve = tk.StringVar(value="Q")
    
    def returnhome():
        window.destroy()
        Home.home()  

    def calculate(): #Defining what happens when calculate button is pressed
        try:

            #Getting values from inputs and preventing blank inputs (Defaulting to zero)
            T1 = float(user_temp1.get()) if user_temp1.get() != "" else (user_temp1.set(0.0) or 0.0)
            T2 = float(user_temp2.get()) if user_temp2.get() != "" else (user_temp2.set(0.0) or 0.0)
            L = float(bar_length.get()) if bar_length.get() != "" else (bar_length.set(0.0) or 0.0)
            W = float(bar_width.get()) if bar_width.get() != "" else (bar_width.set(0.0) or 0.0)
            H = float(bar_height.get()) if bar_height.get() != "" else (bar_height.set(0.0) or 0.0)
            k = float(thermal_conductivity.get()) if thermal_conductivity.get() != "" else (thermal_conductivity.set(0.0) or 0.0)
            Q = float(heat_flow.get()) if heat_flow.get() != "" else (heat_flow.set(0.0) or 0.0)

            window.update()

            # Pre calculations to simplify maths later
            A = W * H  # Cross-sectional area
            dT = abs(T1 - T2) #change in temp
            solve_for = variable_to_solve.get() #getting variable to solve for

            #Checking what to solve for and performing calculation:
            if solve_for == "Q":
                result = solve_for_Q(k,A,dT,L)
                heat_flow.set(result)
            elif solve_for == "k":
                result = solve_for_k(Q,A,dT,L)
                thermal_conductivity.set(result)
            elif solve_for == "L":
                result = solve_for_L(Q,k,A,dT)
                bar_length.set(result)
            elif solve_for == "T1":
                result = solve_for_T1(T2,Q,k,W,H,L)
                user_temp1.set(result)
            elif solve_for == "T2":
                result = solve_for_T2(T1,Q,k,W,H,L)
                user_temp2.set(result)
            elif solve_for == "ΔT":
                result = solve_for_delta_T(Q,k,W,H,L)
                delta_T.set(result)
            elif solve_for == "W":
                result = solve_for_width(Q,k,H,dT,L)
                bar_width.set(result)
            elif solve_for == "H":
                result = solve_for_height(Q,k,W,dT,L)
                bar_height.set(result)
            else:
                raise ValueError("Invalid selection.")
            
            #Messagebox for output:
            messagebox.showinfo("Result", f"Calculated {solve_for} to be {result:.3f}")

        except ZeroDivisionError as div0err:
            messagebox.showerror('error',div0err)

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
       
    validate_inp= window.register(callback)


    #Selecting what to solve for
    ttk.Label(window, text="Solve for:").grid(row=0, column=0)
    ttk.Combobox(window, textvariable=variable_to_solve, values=["Q", "k", "L", "T1", "T2", "ΔT", "W", "H"],state='readonly').grid(row=0, column=1)
    
    # Inputs & labels
    ttk.Label(window, text="Temperature 1[T1] (Kelvin):").grid(row=1, column=0)
    ttk.Entry(window, textvariable=user_temp1,validate="key",validatecommand=(validate_inp,"%P")).grid(row=1, column=1)
    ttk.Label(window, text="Temperatre 2[T2] (Kelvin):").grid(row=2, column=0)
    ttk.Entry(window, textvariable=user_temp2,validate="key",validatecommand=(validate_inp,"%P")).grid(row=2, column=1)
    ttk.Label(window, text="Length[L] (Meters):").grid(row=3, column=0)
    ttk.Entry(window, textvariable=bar_length,validate="key",validatecommand=(validate_inp,"%P")).grid(row=3, column=1)
    ttk.Label(window, text="Width[W] (Meters):").grid(row=4, column=0)
    ttk.Entry(window, textvariable=bar_width,validate="key",validatecommand=(validate_inp,"%P")).grid(row=4, column=1)
    ttk.Label(window, text="Height[H] (Meters):").grid(row=5, column=0)
    ttk.Entry(window, textvariable=bar_height,validate="key",validatecommand=(validate_inp,"%P")).grid(row=5, column=1)
    ttk.Label(window, text="Thermal Conductivity[k] (w/mK):").grid(row=6, column=0)
    ttk.Entry(window, textvariable=thermal_conductivity,validate="key",validatecommand=(validate_inp,"%P")).grid(row=6, column=1)
    ttk.Label(window, text="Heat Flow[Q] (Watts):").grid(row=7, column=0)
    ttk.Entry(window, textvariable=heat_flow,validate="key",validatecommand=(validate_inp,"%P")).grid(row=7, column=1)
    
    ttk.Button(window, text="Calculate", command=calculate).grid(row=8, column=0, columnspan=2)
    ttk.Button(window, text='Return Home', command=returnhome).grid(row=9,column=0,columnspan=2)
    
    window.mainloop()


        



