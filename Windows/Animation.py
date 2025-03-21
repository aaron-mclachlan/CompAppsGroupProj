import numpy
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def simulate(Height, Length):
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

    outline_bar, = ax.barh(y,x,height=bar_thick,color='none',edgecolor='grey',linewidth=2)
    ani_bar, = ax.barh(y, [0], height=bar_thick, color='red',alpha=0.5)
   
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().pack()

    def animate_bar(frame=0):
        if frame < Length:  # Stop when reaching max length
            ani_bar.set_width(frame)
            canvas.draw()  # Update the canvas
            root.after(10, animate_bar, frame + 0.05)  # Schedule next update
        else:
            ani_bar.set_width(Length)
            canvas.draw()

    # Start the animation
    animate_bar()

    def restart_animation():
        animate_bar()

    def close_window():
        root.destroy()

    ttk.Button(root,text="Restart animation",command=restart_animation).pack()
    ttk.Button(root,text="Exit Simulation",command=close_window).pack()




    

    root.mainloop()

