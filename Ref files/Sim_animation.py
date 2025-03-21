import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plotgraph(Height, Length):
    y_labels = [f"Bar Height {Height} m"]  # Label for the bar
    x_values = [Length]  # Final length of the animated bar
    bar_thickness = 0.9  # Bar thickness

    fig, ax = plt.subplots(figsize=(10, 4))

    # Plot the outlined bar
    ax.barh(y_labels, x_values, height=bar_thickness, color='none', edgecolor='grey', linewidth=2)  

    # Animated bar - (y-label,inital len,thickness)
    animated_bar = ax.barh(y_labels, [0], height=bar_thickness, color='red', alpha=0.5)  

    ax.set_xlim(0, Length * 1.1)  # x- axis limits
    ax.set_ylim(-1, 1)  # y axis limts
    ax.set_xlabel("Bar Length (m)") #x- axis label

    def update(len):
        """Updates the length of the red bar for animation"""
        animated_bar[0].set_width(len)  # Gradually increase the bar length
        
        #if len>= Length:#Stopping animation at end of bar
           # ani.event_source.stop()
        #return animated_bar,

    # Create the animation
    ani = animation.FuncAnimation(
        fig, update, frames=range(0, int(Length) + 1), interval=100, blit=False)
  
    plt.tight_layout()
    plt.show()



plotgraph(0.5,8)








