import tkinter as tk
from tkinter import messagebox,ttk
from PIL import ImageTk, Image
import Windows.Calculator as Calculator
import Windows.Home as Home
import Windows.Animation as ani

def simulation_page():#Code for simulation page
    sim_pg = tk.Tk()
    win_width = sim_pg.winfo_screenwidth()
    win_height = sim_pg.winfo_screenheight()
    sim_pg.geometry("%dx%d" % (win_width, win_height))
    sim_pg.title('Simulator')



     #Background image
    def background_img(event=None):  # Scale the background image
        new_width = sim_pg.winfo_width()  # Get current width
        new_height = sim_pg.winfo_height()  # Get current height
        scaled_img = load.resize((new_width, new_height), Image.Resampling.LANCZOS)
        new_img = ImageTk.PhotoImage(scaled_img)
        backgroundLabel.config(image=new_img)
        backgroundLabel.image = new_img  # Prevent garbage collection

    # Load and display the background image
    path = "BG_images/SimpgBG.png"  # Make sure path is correct
    load = Image.open(path)

    # Initial image (will be resized immediately after)
    img = ImageTk.PhotoImage(load)
    backgroundLabel = tk.Label(sim_pg, image=img)
    backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)

    # Force an immediate resize to match the window
    sim_pg.after(100, background_img)

    # Bind resize event to keep updating the background
    sim_pg.bind("<Configure>", background_img)





    #Defining Varaibles
    selected_mat = tk.Variable(value="Mild Steel (50)")
    Temp_1 = tk.StringVar(value=0.0)
    Temp_2 = tk.StringVar(value= 0.0)
    Length = tk.StringVar(value=0.0)
    Width = tk.StringVar(value=0.0)
    Height = tk.StringVar(value=0.0)

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

    def close_sim():#for home button
        sim_pg.destroy()
        Home.home()


    def simulate():#for simulate button
        try:
            
            #Getting values and preventing blank inputs, defaults to 0.0 if blank except length (defaults to 1)
            T1 = (Temp_1.get()) if Temp_1.get() != "" else (Temp_1.set(0.0) or 0.0)
            T2 = (Temp_2.get()) if Temp_2.get() != "" else (Temp_2.set(0.0) or 0.0)
            L = (Length.get()) if Length.get() != "" or Length.get() == 0 else (Length.set(1) or 1)
            W = (Width.get()) if Width.get() != "" else (Width.set(0.0) or 0.0)
            H = (Height.get()) if Height.get() != "" else (Height.set(0.0) or 0.0)
            sim_pg.update()
            if T1 == "-" or T2 == "-" or L == "-" or W == "-" or H == "-":
                raise ValueError("Please Make sure you input a number and not just a symbol on its own")
            
            T1,T2,L,W,H = float(T1),float(T2),float(L),float(W),float(H)

            if L == 0 : #Preventing div/0
                raise ZeroDivisionError('Length cannot be Zero')
            
            if T1 == 0 and T2 == 0: #Preventing zero values breaking animation
                raise ValueError("Please make sure both temperatures are not zero")
            
            if T1 == T2:
                raise ValueError("Please ensure both temperatures are not the same value")
            if W == 0 or H == 0:
                if H == 0 and W == 0:
                    issue = "Height and width are both zero"
                elif W == 0:
                    issue = "Width is zero"
                else:
                    issue = "Height is zero"


                raise ValueError(f"Please make sure no values are equal to zero: {issue}")
            
            
            
            #Getting material and its conductivity
            mat = selected_mat.get()
            k = conductivity.get(mat)

        
            #Additional maths
            dT = T1 - T2 #change in temp
            A = W*H # X sec area

            #Heat flow rate for simulation
            Q = (k*A*dT)/L
            print("Output",f"Variables:\nT1:{T1} \nT2:{T2}\nL:{L} \nW:{W} \nH:{H} \nMaterial:{mat} \nConductivity:{k}\ndt:{dT}\nA:{A}\nQ:{Q:.3f}")
        
            if dT >= 0 :
                dt_pos = True
            else:
                dt_pos = False

            ani.simulate(H,L,Q,mat,dt_pos)#plotting graph for animation
        
        except ValueError as input_err:
            messagebox.showerror('Error',f"An error occured:\n{input_err.args}")
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(input_err).__name__, input_err.args)
            print(f"\nError readout\n{message}\n\n")

        except ZeroDivisionError as div0err:
            messagebox.showerror('Error',f"An error occured:\n{div0err.args}")
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(div0err).__name__, div0err.args)
            print(f"\nError readout\n{message}\n\n")


        except Exception as MiscErr: #misc errors, gives a detailed readout for troubleshooting
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            message = template.format(type(MiscErr).__name__, MiscErr.args)
            messagebox.showerror("error", message)
            print(f"\nError readout\n{message}\n\n")

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



 #Semi-trasparent frame to place inputs in
    Input_frame = tk.Frame(sim_pg,bg="#fff1ef", relief='ridge', padx=10, pady=10)
    Input_frame.place(relx=0.5, rely=0.5,anchor="center")


    #Inputs
    mat_lbl = ttk.Label(Input_frame,text="Select Material\n(Thermal conductivity in W/mK)",justify="center")
    mat_lbl.grid(row=0,column=0,padx=5,pady=5,sticky='e')

    mat_dropdown = ttk.Combobox(Input_frame,textvariable=selected_mat,values=[
        "Aerogel (0.013)", "Aluminium (205)", "Copper (393)", "Diamond (2000)",
        "Firebrick (0.4)", "Glass (1)", "Gold (310)", "Ice (2.4)", "Mild Steel (50)", 
        "Silver (406)", "Stainless Steel (15)"],state='readonly')
    mat_dropdown.grid(row=0,column=1,padx=5,pady=5,sticky='ew')


    
   
      
   #GUI Layout
   
   #Inputs
    fields =  [
        ("Starting Temperature (K)", Temp_1,1),
        ("End Temperature (K)", Temp_2,2),
        ("Length (m)", Length, 3),
        ("Width (m)", Width,4),
        ("Height (m)", Height,5)
    ]

    for text,var,row in fields:
        ttk.Label(Input_frame, text=text,background="#fff1ef").grid(row=row,column=0,padx=5,pady=5,sticky="e")
        ttk.Entry(Input_frame, textvariable=var,validate="key",validatecommand=(validate_inp,"%P")).grid(row=row,column=1,padx=5,pady=5,sticky='ew')

    
    simulate_bttn = ttk.Button(Input_frame,text='Simulate',command=simulate)
    simulate_bttn.grid(row=6,column=0, columnspan=2, pady=10,sticky="ew")

    ExitSimBttn = ttk.Button(Input_frame, text="Exit Simulator", command=close_sim)
    ExitSimBttn.grid(row=7,column=0, columnspan=2, pady=10,sticky="ew")

    Input_frame.grid_columnconfigure(0,weight=1)
    Input_frame.grid_columnconfigure(1,weight=2)
    for rows in range (8):
        Input_frame.grid_rowconfigure(rows, weight=1)



    sim_pg.mainloop()