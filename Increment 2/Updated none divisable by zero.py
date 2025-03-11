import tkinter as tk
from tkinter import messagebox,ttk
import time

def calculator():  # code for calculator page
    window = tk.Tk()
    window.geometry('800x600')  # def window
    window.title('Conduction Calculator')

    default_font = "Arial", 12  # to set a default font

    user_temp1 = tk.Variable()  # def user inputs
    user_temp2 = tk.Variable()
    bar_length = tk.Variable()
    bar_width = tk.Variable()
    bar_height = tk.Variable()

    def submit():  # def function for submit button
        try:  # error handling
            temp1 = user_temp1.get()  # Getting input values
            temp2 = user_temp2.get()
            length = bar_length.get()
            width = bar_width.get()
            height = bar_height.get()
            steel_constant = 15


            # Calculating heat flow rate
            rate = steel_constant * (float(temp1) - float(temp2)) * (float(height) * float(width) / float(length))

            # Displaying calculated rate within window
            calculated_rate_display.config(state=tk.NORMAL)  # allows calculated value to be entered in the text widget
            calculated_rate_display.delete(1.0, tk.END)  # to clear existing content
            calculated_rate_display.insert(tk.END, f"{rate:.2f} W")
            calculated_rate_display.config(state=tk.DISABLED)  # to disable editing

            # Messagebox showing the output
            messagebox.showinfo(
                message=f"""
                Energy Flow rate: {rate} W"""
            )

        except ValueError:# Checking for number input
            messagebox.showerror("Error", "Invalid input. Please enter a number.")
        
        except ZeroDivisionError: #Div by zero error
            messagebox.showerror("Error", "Please ensure no dimensions are set to zero.")
            
        except Exception as err_found:#Exceptions
            messagebox.showerror("Error", f"An unexpected error occurred: {err_found}")

    # steel material
    material_lbl = tk.Label(window, text='Stainless Steel Constant:')  # label widget
    material_display = tk.Text(window, height=1, width=26, font=default_font, wrap=tk.NONE)  # text widget
    material_display.tag_configure("center", justify="center")  # optional?
    material_display.insert(tk.END, "15 WmK", "center")
    material_display.config(state=tk.DISABLED)  # to disable user input

    # Starting Temp
    Temp1_lbl = tk.Label(window, text='Enter Starting Temperature (K):')  # text label for temperature
    temp_input1 = tk.Entry(window, textvariable=user_temp1)  # user input for temperature

    # Final Temp
    Temp2_lbl = tk.Label(window, text="Enter Final Temperature (K):")
    temp_input2 = tk.Entry(window, textvariable=user_temp2)

    # Bar Dimensions
    leng_lbl = tk.Label(window, text="Enter Bar Length (m):")  # Bar length
    leng_inp = tk.Entry(window, textvariable=bar_length)

    width_lbl = tk.Label(window, text="Enter Bar Width (m):")  # Bar width
    width_inp = tk.Entry(window, textvariable=bar_width)

    height_lbl = tk.Label(window, text="Enter Bar Height (m):")  # Bar height
    height_inp = tk.Entry(window, textvariable=bar_height)

    # Enter button
    enter_bttn = tk.Button(window, text='Calculate', command=submit)

    # Display Calculated Value
    calculated_rate_lbl = tk.Label(window, text="Calculated Rate: ")
    calculated_rate_display = tk.Text(window, height=1, width=26, font=default_font, wrap=tk.NONE)  # text widget
    calculated_rate_display.config(state=tk.DISABLED)  # to disable user input

    # Grid Layout, ONLY CHANGE IF ADDING MORE THINGS TO WINDOW
    def input_window_layout():
        # Labels
        material_lbl.grid(row=0, column=0)
        Temp1_lbl.grid(row=0, column=1)
        Temp2_lbl.grid(row=0, column=2)
        leng_lbl.grid(row=2, column=0)
        width_lbl.grid(row=2, column=1)
        height_lbl.grid(row=2, column=2)

        # Inputs
        material_display.grid(row=1, column=0)
        temp_input1.grid(row=1, column=1)
        temp_input2.grid(row=1, column=2)
        leng_inp.grid(row=3, column=0)
        width_inp.grid(row=3, column=1)
        height_inp.grid(row=3, column=2)

        # Submit
        enter_bttn.grid(row=4, column=0)

        # Calculated value
        calculated_rate_lbl.grid(row=6, column=3)
        calculated_rate_display.grid(row=6, column=4)

    input_window_layout()
    window.mainloop()

calculator()