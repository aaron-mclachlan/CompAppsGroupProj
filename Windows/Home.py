import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import time
import Windows.Theory_Page as theory
import Windows.Calculator as Calculator
import Windows.Simulator as sim

def home(): #code for home page
    homewindow = tk.Tk()

    winwidth = homewindow.winfo_screenwidth()
    winheight = homewindow.winfo_screenheight()
    homewindow.geometry("%dx%d" % (winwidth, winheight))
    homewindow.title('Home Menu')

    def calc_bttn():
        homewindow.destroy()
        Calculator.calculator()  

    def theorypg_bttn():
        homewindow.destroy()
        theory.theory_page() 

    def sim_bttn():
        homewindow.destroy()
        sim.simulation_page()  

    def background_img(event=None):  # Scale the background image
        new_width = homewindow.winfo_width()  # Get current width
        new_height = homewindow.winfo_height()  # Get current height
        scaled_img = load.resize((new_width, new_height), Image.Resampling.LANCZOS)
        new_img = ImageTk.PhotoImage(scaled_img)
        backgroundLabel.config(image=new_img)
        backgroundLabel.image = new_img  # Prevent garbage collection

    # Load and display the background image
    path = "BG_images/homeBG.png"  # Make sure path is correct
    load = Image.open(path)

    # Initial image (will be resized immediately after)
    img = ImageTk.PhotoImage(load)
    backgroundLabel = tk.Label(homewindow, image=img)
    backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

    # Force an immediate resize to match the window
    homewindow.after(100, background_img)

    # Bind resize event to keep updating the background
    homewindow.bind("<Configure>", background_img)


    #colors for the buttons
    color1= '#DFF2FF' #pale blue
    color2= '#9ACBF0' #sky blue
    color3= '#0576D1' #dark blue
    
    #frames to add the buttons in front of the image
    button_frame = tk.Frame(homewindow, bg=color1)
    button_frame.place(relx=0.5, rely=0.5, anchor="center")

    #buttons style
    style= ttk.Style()
    style.theme_use('clam')
    
    style.configure(
    "TButton",
    background=color3, #button color
    foreground='white', #text color
    width=20,
    height=2,
    cursor='hand1',
    font= ('Arial', 12, 'bold'),
    )

    #button change color when hovered
    style.map(
    "TButton",
    background=[('active', color2)], #button color
    foreground=[('active', 'black')], #text color
    )
    
    #buttons
    calculator_bttn = ttk.Button(
        button_frame,
        text="Calculator",
        command=calc_bttn)
    calculator_bttn.grid(row=0, column=0, padx=0, pady=0) #added a grid for the frame placement

    simulator_bttn = ttk.Button(button_frame,text="Simulation", command= sim_bttn)
    simulator_bttn.grid(row=2, column=0, padx=10, pady=10)

    theory_bttn = ttk.Button(button_frame, text='Theory',command=theorypg_bttn)
    theory_bttn.grid(row=4, column=0, padx=0, pady=0)

    homewindow.mainloop()




