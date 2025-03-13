import tkinter as tk
from tkinter import messagebox, ttk

def calculator():
    window = tk.Tk()
    window.geometry('800x600')
    window.title('Conduction Calculator')

    default_font = "Arial", 12

    # User input variables
    user_temp1 = tk.DoubleVar()
    user_temp2 = tk.DoubleVar()
    bar_length = tk.DoubleVar()
    bar_width = tk.DoubleVar()
    bar_height = tk.DoubleVar()
    heat_flow = tk.DoubleVar()

    steel_constant = 15  # Thermal conductivity (W/m·K)

    # Variable selection dropdown
    variable_options = ["Heat Flow Rate (Q)", "Starting Temp (T1)", "Final Temp (T2)", "Bar Length (L)", "Bar Width (W)", "Bar Height (H)"]
    variable_to_solve = tk.StringVar(value="Heat Flow Rate (Q)")

    def submit():
        try:
            # Get user input values
            temp1 = user_temp1.get()
            temp2 = user_temp2.get()
            length = bar_length.get()
            width = bar_width.get()
            height = bar_height.get()
            Q = heat_flow.get()

            area = width * height  # Cross-sectional area
            delta_T = temp1 - temp2

            # Determine which variable to solve for
            solve_for = variable_to_solve.get()

            if solve_for == "Heat Flow Rate (Q)":
                if length == 0:
                    messagebox.showerror("Error", "Bar length cannot be zero.")
                    return
                Q = steel_constant * (area * delta_T / length)
                result = f"Heat Flow Rate: {Q:.2f} W"

            elif solve_for == "Starting Temp (T1)":
                if area == 0 or length == 0:
                    messagebox.showerror("Error", "Bar dimensions cannot be zero.")
                    return
                temp1 = (Q * length) / (steel_constant * area) + temp2
                result = f"Starting Temperature: {temp1:.2f} K"

            elif solve_for == "Final Temp (T2)":
                if area == 0 or length == 0:
                    messagebox.showerror("Error", "Bar dimensions cannot be zero.")
                    return
                temp2 = temp1 - (Q * length) / (steel_constant * area)
                result = f"Final Temperature: {temp2:.2f} K"

            elif solve_for == "Bar Length (L)":
                if Q == 0:
                    messagebox.showerror("Error", "Heat Flow Rate cannot be zero.")
                    return
                length = steel_constant * (area * delta_T) / Q
                result = f"Bar Length: {length:.2f} m"

            elif solve_for == "Bar Width (W)":
                if Q == 0 or height == 0:
                    messagebox.showerror("Error", "Heat Flow Rate or Height cannot be zero.")
                    return
                width = (Q * length) / (steel_constant * delta_T * height)
                result = f"Bar Width: {width:.2f} m"

            elif solve_for == "Bar Height (H)":
                if Q == 0 or width == 0:
                    messagebox.showerror("Error", "Heat Flow Rate or Width cannot be zero.")
                    return
                height = (Q * length) / (steel_constant * delta_T * width)
                result = f"Bar Height: {height:.2f} m"

            # Display result
            calculated_rate_display.config(state=tk.NORMAL)
            calculated_rate_display.delete(1.0, tk.END)
            calculated_rate_display.insert(tk.END, result)
            calculated_rate_display.config(state=tk.DISABLED)
            messagebox.showinfo("Result", result)

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numbers.")
        except Exception as err_found:
            messagebox.showerror("Error", f"An unexpected error occurred: {err_found}")

    # Dropdown for variable selection
    variable_menu = ttk.Combobox(window, textvariable=variable_to_solve, values=variable_options, state="readonly")

    # Labels & Inputs
    material_lbl = tk.Label(window, text='Stainless Steel Constant:')
    material_display = tk.Text(window, height=1, width=26, font=default_font, wrap=tk.NONE)
    material_display.insert(tk.END, "15 WmK")
    material_display.config(state=tk.DISABLED)

    temp1_lbl = tk.Label(window, text='Enter Starting Temperature (K):')
    temp_input1 = tk.Entry(window, textvariable=user_temp1)

    temp2_lbl = tk.Label(window, text="Enter Final Temperature (K):")
    temp_input2 = tk.Entry(window, textvariable=user_temp2)

    length_lbl = tk.Label(window, text="Enter Bar Length (m):")
    length_inp = tk.Entry(window, textvariable=bar_length)

    width_lbl = tk.Label(window, text="Enter Bar Width (m):")
    width_inp = tk.Entry(window, textvariable=bar_width)

    height_lbl = tk.Label(window, text="Enter Bar Height (m):")
    height_inp = tk.Entry(window, textvariable=bar_height)

    heat_lbl = tk.Label(window, text="Enter Heat Flow Rate (W):")
    heat_inp = tk.Entry(window, textvariable=heat_flow)

    enter_bttn = tk.Button(window, text='Calculate', command=submit)

    calculated_rate_lbl = tk.Label(window, text="Calculated Value: ")
    calculated_rate_display = tk.Text(window, height=1, width=30, font=default_font, wrap=tk.NONE)
    calculated_rate_display.config(state=tk.DISABLED)

    # Layout
    def input_window_layout():
        material_lbl.grid(row=0, column=0)
        material_display.grid(row=1, column=0)

        variable_menu.grid(row=0, column=1, columnspan=2)

        temp1_lbl.grid(row=2, column=0)
        temp_input1.grid(row=3, column=0)

        temp2_lbl.grid(row=2, column=1)
        temp_input2.grid(row=3, column=1)

        length_lbl.grid(row=4, column=0)
        length_inp.grid(row=5, column=0)

        width_lbl.grid(row=4, column=1)
        width_inp.grid(row=5, column=1)

        height_lbl.grid(row=4, column=2)
        height_inp.grid(row=5, column=2)

        heat_lbl.grid(row=2, column=2)
        heat_inp.grid(row=3, column=2)

        enter_bttn.grid(row=6, column=1)

        calculated_rate_lbl.grid(row=7, column=0)
        calculated_rate_display.grid(row=7, column=1, columnspan=2)

    input_window_layout()
    window.mainloop()

calculator()
