import matplotlib.pyplot as plt
import matplotlib.animation as animation

def plotgraph(Height, Length):
    y_labels = [f"Bar Height {Height} m"]  # Label for the bars
    x_values = [Length]  # Final length of the animated bar
    bar_thickness = 0.9  # Bar thickness

    fig, ax = plt.subplots(figsize=(10, 4))

    # Plot the outlined bar
    ax.barh(y_labels, x_values, height=bar_thickness, color='none', edgecolor='blue', linewidth=2)  

    # Create the animated bar (starting with 0 length)
    animated_bar = ax.barh(y_labels, [0], height=bar_thickness, color='red', alpha=0.5)  

    ax.set_xlim(0, Length * 1.1)  # Set axis limits with padding
    ax.set_ylim(-1, 1)  # Keep y-axis limited for better appearance
    ax.set_xlabel("Bar Length (m)")

    def update(frame):
        """Updates the length of the red bar for animation"""
        animated_bar[0].set_width(frame)  # Gradually increase the bar width
        return animated_bar,

    # Create the animation
    ani = animation.FuncAnimation(fig, update, frames=range(0, int(Length) + 1), interval=100, blit=False)

    plt.tight_layout()
    plt.show()

plotgraph(0.5, 10)