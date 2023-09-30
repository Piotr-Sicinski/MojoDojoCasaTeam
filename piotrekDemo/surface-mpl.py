import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Create a figure and a 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Define the number of values
num_vals = 20

# Create a meshgrid for the x and y values
x = np.linspace(0, 10, num_vals)
y = np.linspace(0, 10, num_vals)
x, y = np.meshgrid(x, y)

# Define the initial z values as a function of x and y
phi = 0
z = np.sin(np.sqrt(x**2 + y**2) + phi)

# Create the initial surface plot
surf = ax.plot_surface(x, y, z, cmap='viridis')


def update(frame):
    global phi

    # Update phi in each frame
    phi += 0.1

    # Update the z values based on the new phi
    z = np.sin(np.sqrt(x**2 + y**2) + phi)

    # Update the surface plot
    ax.clear()
    ax.plot_surface(x, y, z, cmap='viridis')


# Create an animated plot
ani = FuncAnimation(fig, update, frames=100, interval=50)

# Show the plot
plt.show()
