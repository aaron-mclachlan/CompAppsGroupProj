import tkinter as tk
from tkinter import ttk
from tkinter import WORD, PhotoImage
from PIL import Image, ImageTk
import Windows.Home as Home
import Windows.Calculator as Calculator

def theory_page():  
    theory_window = tk.Tk()
    theory_window.geometry('1920x1080')
    theory_window.title('Theory of Heat Transfer')

    # Load the background image
    path = "BG_images/TheoryBG.png"
    load = Image.open(path)

    # Function to scale the background image
    def background_img(event=None):  
        new_width = theory_window.winfo_width()
        new_height = theory_window.winfo_height()
        scaled_img = load.resize((new_width, new_height), Image.Resampling.LANCZOS)
        new_img = ImageTk.PhotoImage(scaled_img)
        backgroundLabel.config(image=new_img)
        backgroundLabel.image = new_img  # Prevent garbage collection

    # Display the background image
    img = ImageTk.PhotoImage(load)
    backgroundLabel = tk.Label(theory_window, image=img)
    backgroundLabel.place(x=0, y=0, relwidth=1, relheight=1)
    backgroundLabel.lower()  

    # Force background to update on startup
    theory_window.after(100, background_img)

    # Bind resize event to update background dynamically
    theory_window.bind("<Configure>", background_img)

    # Frame for content over the background
    content_frame = tk.Frame(theory_window, height=250, width=50, bg='#FFF4DA')
    content_frame.place(relx=0.5, rely=0.60, anchor='center')

    # Adding the content
    #label = tk.Label(content_frame, text="Conduction in Single Material", bg='#FFF4DA', font=("Arial", 20, 'bold'))
    #label.pack(padx=20, pady=20)

    text_box = tk.Text(content_frame, bg='#FFF4DA', height=6, width=120, wrap=WORD, font=("Arial", 14))
    text_box.pack()
    conduction_text = """    Conduction is a form of heat transfer that occurs through collisions of the particles that make up the material. The energy transfer happens when the more energetic particles (hotter) transfer their energy to the tranquil particles (cooler). The particles colliding into each other forms a medium through which the energy is transferred.

    The assumptions our calculations and simulations make is that the heat cannot escape the metal bar being heated. Therefore, the heat put into the bar at one end transfers through the bar linearly to the other end; heat transferring linearly is only true for isotropic materials.
    """
    text_box.insert(tk.END, conduction_text)
    text_box.config(state=tk.DISABLED)

    equation1 = Image.open("BG_images/TheoryEQ3.png")  # CHANGE FILE PATH IF NEEDED
    resized_image = equation1.resize((350, 100), Image.Resampling.LANCZOS)
    new_image1 = ImageTk.PhotoImage(resized_image)  
    image_label = tk.Label(content_frame, image=new_image1)
    image_label.pack()
    image_label.image = new_image1

    label = tk.Label(content_frame, text="Temperature Distribution", bg='#FFF4DA', font=("Arial", 16, 'bold'))
    label.pack(padx=20, pady=20)

    text_box = tk.Text(content_frame, bg='#FFF4DA', height=4, width=120, wrap=WORD, font=("Arial", 14))
    text_box.pack()
    temperature_text = """   Using our calculator, it is possible to calculate the temperature at either end. Calculating the temperature at any given point in the material can be attained from the equation shown below. Knowing the distance from the heat source to the reference point (x), calculate the temperature at point x by rearranging the equation for T."""
    text_box.insert(tk.END, temperature_text)
    text_box.config(state=tk.DISABLED)

    equation2 = Image.open("BG_images/TheoryEQ4.png")  # CHANGE FILE PATH IF NEEDED
    resized_image = equation2.resize((350, 100), Image.Resampling.LANCZOS)
    new_image2 = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(content_frame, image=new_image2)
    image_label.pack()
    image_label.image = new_image2

    label = tk.Label(content_frame, text="Conduction in Different Materials Combined in Series", bg='#FFF4DA', font=("Arial", 16, 'bold'))
    label.pack(padx=20, pady=20)

    text_box = tk.Text(content_frame, bg='#FFF4DA', height=4, width=120, wrap=WORD, font=("Arial", 14))
    text_box.pack()
    series_text = """    When two different materials of the same size are joined together via the ends, the heat flow rate from one material to another is the same as for a single material. However, the temperature drop will differ within each material. Calculating this is done by taking the equations for each material separately, when opposing them with each other the area, length and heat flowrate cancel. Then rearranging for the temperature at the end of the second material, as shown in the image below."""
    text_box.insert(tk.END, series_text)
    text_box.config(state=tk.DISABLED)

    equation3 = Image.open("BG_images/TheoryEQ5.png")  # CHANGE FILE PATH IF NEEDED
    resized_image = equation3.resize((350, 100), Image.Resampling.LANCZOS)
    new_image3 = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(content_frame, image=new_image3)
    image_label.pack()
    image_label.image = new_image3

    # Buttons for navigation
    def home_from_theory():
        theory_window.destroy()
        Home.home()

    def calc_bttn():
        theory_window.destroy()
        Calculator.calculator()

    # Button styling
    style = ttk.Style()
    style.theme_use('clam')

    style.configure(
        "TButton",
        background='#F46960',  # Button color
        foreground='white',  # Text color
        width=20,
        height=2,
        cursor='hand1',
        font=('Arial', 12, 'bold'),
    )

    # Button hover effect
    style.map(
        "TButton",
        background=[('active', '#9ACBF0')],  # Button color
        foreground=[('active', 'black')],  # Text color
    )

    home_bttn = ttk.Button(theory_window, text='Return to Home', command=home_from_theory)
    home_bttn.place(relx=0.05, rely=0.95, anchor='sw')

    calculator_bttn = ttk.Button(theory_window, text='Calculator', command=calc_bttn)
    calculator_bttn.place(relx=0.95, rely=0.95, anchor='se')

    theory_window.mainloop()

if __name__ == "__main__":
    theory_page()