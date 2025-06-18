from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt


def projectile_motion(v0, theta, time):
    """
    Calculates the trajectory of a projectile.

    Args:
        v0 (float): Initial velocity (m/s).
        theta (float): Launch angle (degrees).
        time (array): Array of time values (seconds).

    Returns:
        tuple: Arrays of x and y coordinates of the trajectory.
    """
    theta_rad = np.radians(theta)
    g = 9.81
    v0x = v0 * np.cos(theta_rad)
    v0y = v0 * np.sin(theta_rad)
    x = v0x * time
    y = v0y * time - 0.5 * g * time**2
    return x, y


# Example usage:
v0 = input("What would you like the initial velocity to be: ")
v01 = float(v0)  # Convert to float for better precision
theta = input("What would you like the launch angle to be: ")
theta1 = float(theta)  # Convert to float for better precision
time = np.linspace(0, 2 * v01 * np.sin(np.radians(theta1)) / 9.81, 100)

# Calculate trajectory
x, y = projectile_motion(v01, theta1, time)

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, max(x) * 1.1)
ax.set_ylim(0, max(y) * 1.1)
ax.set_xlabel("Horizontal distance (m)")
ax.set_ylabel("Vertical distance (m)")
ax.set_title("Projectile Motion Trajectory")
ax.grid(True)

# Create a line and a point for the animation
line, = ax.plot([], [], lw=2, label="Trajectory")
point, = ax.plot([], [], 'ro', label="Projectile")
trail, = ax.plot([], [], 'b--', alpha=0.5, label="Trail")


# Initialize the animation
def init():
    line.set_data([], [])
    point.set_data([], [])
    trail.set_data([], [])
    return line, point, trail


# Update the animation for each frame
def animate(i):
    # Update the trajectory line
    line.set_data(x[:i], y[:i])
    # Update the projectile point (current position)
    point.set_data([x[i]], [y[i]])  # Wrap x[i] and y[i] in lists
    # Update the trail (path already traveled)
    trail.set_data(x[:i], y[:i])
    return line, point, trail


# Create the animation
ani = FuncAnimation(fig, animate, frames=len(
    time), init_func=init, blit=True, interval=50, repeat=False)

# Add a legend and show the plot
plt.legend()
plt.show()
