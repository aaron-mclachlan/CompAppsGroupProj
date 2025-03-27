import numpy
import re
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.cm as cm
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



def simulate(Height, Length,Q,mat,dt_pos):
    root = tk.Tk()
    root.title("Simulator")
    root.geometry("1920x1080")

    fig = plt.Figure(figsize=(12,5),dpi=100)

    x = [Length]
    y = [f"Bar Height: {Height} m"]
    bar_thick = 0.9

    

    ax = fig.add_subplot(111)
    ax.set_xlim(0, Length * 1.1)  # x- axis limits
    ax.set_ylim(-1, 1)  # y axis limts
    ax.set_xlabel("Bar Length (m)") #x- axis label


    #Defining bar colors for -ve dT values:
    outline_colour = '#4faef7'
    ani_color = '#f7664f'
 
    outline_bar, = ax.barh(y,x,height=bar_thick,color=outline_colour)
    
   
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().grid(row=0,column=0,columnspan=2) #Place in tkinter window

    #Animated Bar design
    ani_bar, = ax.barh(y, [0], height=bar_thick, color=ani_color) # defining bar

    Q_max = 500 #Max Q value for animation speed scaling
    def animate_bar(frame=0):#animates bar
        #Adjusting speed based on Q
        speed_factor = abs(Q/Q_max)
        frame_delay = int(max(5,50*(1-speed_factor))) #Low Q -> slower update
        step_size = max(0.01,0.1*speed_factor) #Large Q -> larger step per frame

        if frame < Length:  # Stop when reaching max length
            ani_bar.set_width(frame)#extending the bar per frame
            canvas.draw()  # Update the canvas
            root.after(frame_delay, animate_bar, frame + step_size)  # Schedule next update
        else:
            ani_bar.set_width(Length)
            #ani_bar.set_facecolor(colormap(0.99))
            canvas.draw()

    # Start the animation
    animate_bar()

    def restart_animation():#for restart animation bttn
        animate_bar()

    def close_window():#For close window bttn
        root.destroy()

    def remove_brac(text):#Removes brackets from material
        return str(re.sub(r"\s*\([^)]*\)", "", text))
    
    
    ttk.Label(root,text=f"Heat flow rate: {Q} J/s across {Length}m of {remove_brac(mat).lower()}").grid(row=1,column=0,columnspan=2)
    ttk.Button(root,text="Restart animation",command=restart_animation).grid(row=2,column=0,columnspan=2)
    ttk.Button(root,text="Exit Simulation",command=close_window).grid(row=3,column=0,columnspan=2)
    



    

    root.mainloop()

