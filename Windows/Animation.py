import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.cm as cm
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate(Height, Length,Q):
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

    outline_bar, = ax.barh(y,x,height=bar_thick,color='blue')
    
   
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    #Animated Bar design
    ani_bar, = ax.barh(y, [0], height=bar_thick, color='red') # defining bar
    colormap = plt.cm.Reds

    Q_max = 500 #Max Q value for animation speed scaling
    def animate_bar(frame=0):#Bar animation
        #Adjusting speed based on Q
        speed_factor = Q/Q_max
        frame_delay = int(max(5,50*(1-speed_factor))) #Low Q -> slower update
        step_size = max(0.01,0.1*speed_factor) #Large Q -> larger step per frame

        if frame < Length:  # Stop when reaching max length
            ani_bar.set_width(frame)#extending the bar per frame
            color = colormap(frame/Length) #get color from colormap
            ani_bar.set_facecolor(color)
            canvas.draw()  # Update the canvas
            root.after(frame_delay, animate_bar, frame + step_size)  # Schedule next update
        else:
            ani_bar.set_width(Length)
            ani_bar.set_facecolor(colormap(0.99))
            canvas.draw()

    # Start the animation
    animate_bar()

    def restart_animation():#Restart animation
        animate_bar()

    def close_window():
        root.destroy()

    ttk.Button(root,text="Restart animation",command=restart_animation).pack()
    ttk.Button(root,text="Exit Simulation",command=close_window).pack()




    

    root.mainloop()

