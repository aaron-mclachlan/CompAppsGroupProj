import tkinter as tk
from tkinter import messagebox, ttk

def solve_for_Q(k, A, delta_T, L):
    if L == 0:
        raise ValueError("Length cannot be zero.")
    return (k * A * delta_T) / L

def solve_for_k(Q, A, delta_T, L):
    if A == 0 or delta_T == 0 or L == 0:
        raise ValueError("Area, temperature difference, and length cannot be zero.")
    return (Q * L) / (A * delta_T)

def solve_for_L(Q, k, A, delta_T):
    if k == 0 or A == 0 or delta_T == 0:
        raise ValueError("Thermal conductivity, area, and temperature difference cannot be zero.")
    return (k * A * delta_T) / Q

def calculator():
    window = tk.Tk()
    window.geometry('800x600')
    window.title('Conduction Calculator')

    default_font = ("Arial", 12)

    user_temp1 = tk.DoubleVar()
    user_temp2 = tk.DoubleVar()
    bar_length = tk.DoubleVar()
    bar_width = tk.DoubleVar()
    bar_height = tk.DoubleVar()
    thermal_conductivity = tk.DoubleVar()
    heat_flow = tk.DoubleVar()
    
    variable_to_solve = tk.StringVar(value="Q")  # Default solve for Q
    
    entry_fields = {}
    
    def update_entry_state():
        """Disable the entry of the selected variable to solve for and clear its value."""
        for key, entry in entry_fields.items():
            entry.config(state=tk.NORMAL)
            entry.delete(0, tk.END)
        
        selected = variable_to_solve.get()
        entry_fields[selected].config(state=tk.DISABLED)
    
    def calculate():
        try:
            T1, T2, L, W, H, k, Q = (
                user_temp1.get(), user_temp2.get(), bar_length.get(),
                bar_width.get(), bar_height.get(), thermal_conductivity.get(), heat_flow.get()
            )
            A = W * H  # Cross-sectional area
            delta_T = abs(T1 - T2)
            solve_for = variable_to_solve.get()
            
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
                
            entry_fields[solve_for].config(state=tk.NORMAL)
            entry_fields[solve_for].delete(0, tk.END)
            entry_fields[solve_for].insert(0, round(result, 3))
            
            messagebox.showinfo("Result", f"Calculated {solve_for}: {round(result, 3)}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    ttk.Label(window, text="Solve for:").grid(row=0, column=0)
    ttk.Combobox(window, textvariable=variable_to_solve, values=["Q", "k", "L"], command=update_entry_state).grid(row=0, column=1)
    
    # Input fields
    labels = [
        ("Temp 1:", user_temp1), ("Temp 2:", user_temp2), ("Length:", bar_length),
        ("Width:", bar_width), ("Height:", bar_height), ("Thermal Conductivity:", thermal_conductivity),
        ("Heat Flow (Q):", heat_flow)
    ]
    
    for i, (label_text, var) in enumerate(labels, start=1):
        ttk.Label(window, text=label_text).grid(row=i, column=0)
        entry = ttk.Entry(window, textvariable=var)
        entry.grid(row=i, column=1)
        entry_fields[label_text.split()[0][0]] = entry  # Store reference to entry field
    
    ttk.Button(window, text="Calculate", command=calculate).grid(row=8, column=0, columnspan=2)
    
    update_entry_state()  # Set the initial state
    window.mainloop()

calculator()
