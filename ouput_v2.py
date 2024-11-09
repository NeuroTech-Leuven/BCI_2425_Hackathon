import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define a custom colormap with higher contrast
cmap = plt.get_cmap("plasma")  # Change to a colormap with higher contrast

class MindfulnessApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Real-Time Mindfulness Levels")

        # Create a figure for plotting
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # Initialize mindfulness level
        self.mindfulness_level = 0
        self.current_index = 0  # Start at the first level
        self.mindfulness_levels = list(range(0, 101, 5))  # Loop from 0% to 100%

        # Generate random data for the blobs (this will remain constant)
        self.x = np.linspace(0, 10, 100)
        self.y = np.linspace(0, 10, 100)
        self.X, self.Y = np.meshgrid(self.x, self.y)
        self.Z = np.sin(self.X) + np.cos(self.Y)  # Base data for blobs

        # Create an initial plot
        self.image = self.ax.imshow(self.Z, cmap=cmap, interpolation='bilinear', alpha=0.7, norm=Normalize(vmin=-2, vmax=2))
        self.ax.set_title(f'Mindfulness Level: {self.mindfulness_level}%')
        self.ax.axis('off')  # Turn off the axis for a cleaner look
        self.canvas.draw()  # Initial draw

        # Start the update loop
        self.update_mindfulness()

    def create_glowing_effect(self):
        # Update the color of the blobs based on the mindfulness level
        color_value = self.mindfulness_level / 100  # Normalize to [0, 1]
        
        # Create a color array for the blobs based on the mindfulness level
        color_array = np.full(self.Z.shape, color_value)  # Fill with the normalized mindfulness level

        # Update the image data with the new color
        self.image.set_array(self.Z * color_array)  # Adjust the Z data by the color value
        self.ax.set_title(f'Mindfulness Level: {self.mindfulness_level}%')
        self.canvas.draw()  # Update the canvas

    def update_mindfulness(self):
        # Update mindfulness level based on the current index
        self.mindfulness_level = self.mindfulness_levels[self.current_index]
        self.create_glowing_effect()  # Update the plot with the new mindfulness level

        # Move to the next mindfulness level
        self.current_index = (self.current_index + 1) % len(self.mindfulness_levels)

        # Schedule the next update
        self.master.after(1000, self.update_mindfulness)  # Update every second

if __name__ == "__main__":
    root = tk.Tk()
    app = MindfulnessApp(root)
    root.mainloop()