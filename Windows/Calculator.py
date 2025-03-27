import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import Windows.Home as Home

# Thermal conduction calculation functions
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

#Units dict
units = {
    "Q":"Watts",
    "k": "W/mk",
    "L" : "Meters",
    "T1" : "Kelvin",
    "T2" : "Kelvin",
    "ΔT" : "Kelvin",
    "W" : "Meters",
    "H" : "Meters"
    
}

def calculator():
    window = tk.Tk()
    window.geometry('1920x1080')
    window.state('zoomed')
    window.title('Conduction Calculator')

    # Try to load background image (must be GIF format)
    try:
        original_image = Image.open(r"BG_images/CalcBG.gif")  # Make sure the path is correct
        resized_image = original_image.resize((1920, 1000), Image.Resampling.LANCZOS)  # Resize to 1920x1080
        bg_image = ImageTk.PhotoImage(resized_image)

        bg_label = tk.Label(window, image=bg_image)
        bg_label.image = bg_image  # Keep a reference to prevent garbage collection
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Stretch to full window

    except Exception as e:
        print(f"Error loading background image: {e}")
        window.configure(bg='lightblue')  # Fallback colo

    # Create a semi-transparent frame for the calculator
    main_frame = tk.Frame(window, bg='white', bd=2, relief='ridge', padx=10, pady=10)
    main_frame.place(relx=0.5, rely=0.6, anchor='center')

    # Variables
    user_temp1 = tk.StringVar(value='0.0')
    user_temp2 = tk.StringVar(value='0.0')
    delta_T = tk.StringVar(value='0.0')
    bar_length = tk.StringVar(value='0.0')
    bar_width = tk.StringVar(value='0.0')
    bar_height = tk.StringVar(value='0.0')
    thermal_conductivity = tk.StringVar(value='0.0')
    heat_flow = tk.StringVar(value='0.0')
    variable_to_solve = tk.StringVar(value="Q")

    def returnhome():
        window.destroy()
        Home.home()
        print("Returning to home...")

    def calculate():
        try:
            # Get values from inputs
            T1 = float(user_temp1.get()) if user_temp1.get() else 0.0
            T2 = float(user_temp2.get()) if user_temp2.get() else 0.0
            L = float(bar_length.get()) if bar_length.get() else 0.0
            W = float(bar_width.get()) if bar_width.get() else 0.0
            H = float(bar_height.get()) if bar_height.get() else 0.0
            k = float(thermal_conductivity.get()) if thermal_conductivity.get() else 0.0
            Q = float(heat_flow.get()) if heat_flow.get() else 0.0

            A = W * H
            dT = abs(T1 - T2)
            solve_for = variable_to_solve.get()

            if solve_for == "Q":
                result = solve_for_Q(k, A, dT, L)
                heat_flow.set(f"{result:.3f}")
            elif solve_for == "k":
                result = solve_for_k(Q, A, dT, L)
                thermal_conductivity.set(f"{result:.3f}")
            elif solve_for == "L":
                result = solve_for_L(Q, k, A, dT)
                bar_length.set(f"{result:.3f}")
            elif solve_for == "T1":
                result = solve_for_T1(T2, Q, k, W, H, L)
                user_temp1.set(f"{result:.3f}")
            elif solve_for == "T2":
                result = solve_for_T2(T1, Q, k, W, H, L)
                user_temp2.set(f"{result:.3f}")
            elif solve_for == "ΔT":
                result = solve_for_delta_T(Q, k, W, H, L)
                delta_T.set(f"{result:.3f}")
            elif solve_for == "W":
                result = solve_for_width(Q, k, H, dT, L)
                bar_width.set(f"{result:.3f}")
            elif solve_for == "H":
                result = solve_for_height(Q, k, W, dT, L)
                bar_height.set(f"{result:.3f}")
            else:
                raise ValueError("Invalid selection.")

            messagebox.showinfo("Result", f"Calculated {solve_for} = {result:.3f} {units.get(solve_for)}")

        except ZeroDivisionError as div0err:
            messagebox.showerror('Error', str(div0err))
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def callback(input):
        if input == "" or input == "-":
            return True
        try:
            float(input)
            return True
        except ValueError:
            return False

    validate_inp = window.register(callback)

    # Create custom styles for colored buttons
    style = ttk.Style()
    
    # Style for calculate button (green)
    style.configure('Calculate.TButton', 
                   foreground='purple',
                   background='#ade1da',
                   font=('Helvetica', 10, 'bold'),
                   padding=5,
                   borderwidth=1)
    style.map('Calculate.TButton',
              background=[('active', '#ade1da')])
    
    # Style for home button (red)
    style.configure('Home.TButton', 
                   foreground='purple',
                   background='#f4b47e',
                   font=('Helvetica', 10, 'bold'),
                   padding=5,
                   borderwidth=1)
    style.map('Home.TButton',
              background=[('active', '#f4b47e')])

    # GUI Layout
    ttk.Label(main_frame, text="Solve for:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
    ttk.Combobox(main_frame, textvariable=variable_to_solve, 
                values=["Q", "k", "L", "T1", "T2", "ΔT", "W", "H"],
                state='readonly').grid(row=0, column=1, padx=5, pady=5, sticky='ew')

    # Input fields
    fields = [
        ("Temperature 1 [T1] (K):", user_temp1, 1),
        ("Temperature 2 [T2] (K):", user_temp2, 2),
        ("Length [L] (m):", bar_length, 3),
        ("Width [W] (m):", bar_width, 4),
        ("Height [H] (m):", bar_height, 5),
        ("Thermal Conductivity [k] (W/mK):", thermal_conductivity, 6),
        ("Heat Flow [Q] (W):", heat_flow, 7)
    ]

    for text, var, row in fields:
        ttk.Label(main_frame, text=text).grid(row=row, column=0, padx=5, pady=5, sticky='e')
        ttk.Entry(main_frame, textvariable=var, validate="key",
                 validatecommand=(validate_inp, "%P")).grid(row=row, column=1, padx=5, pady=5, sticky='ew')

    # Buttons with custom colors
    ttk.Button(main_frame, 
              text="Calculate", 
              command=calculate,
              style='Calculate.TButton').grid(row=8, column=0, columnspan=2, pady=10, sticky='ew')
    
    ttk.Button(main_frame,
              text='Return Home',
              command=returnhome,
              style='Home.TButton').grid(row=9, column=0, columnspan=2, pady=5, sticky='ew')

    # Configure grid to expand properly
    main_frame.grid_columnconfigure(0, weight=1)
    main_frame.grid_columnconfigure(1, weight=2)
    for i in range(10):
        main_frame.grid_rowconfigure(i, weight=1)

    window.mainloop()

if __name__ == "__main__":
    calculator()
