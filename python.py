from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Pendulum parameters
g = 9.8  # Acceleration due to gravity (m/s^2)
# Length of the pendulum (m)
L = input("What would you like the length of the pendulum to be: ")
L1 = float(L)
theta0 = input("what would you like the initial angle to be: ")
theta1 = np.radians(int(theta0))  # Initial angle (rad)
time = np.linspace(0, 10, 500)  # Time array

# Function defining the equations of motion


def pendulum_equations(theta, t, g, L):
    dtheta_dt = [theta[1], -g / L1 * np.sin(theta[0])]
    return dtheta_dt


# Solve the differential equations
initial_state = [theta1, 0]
solution = odeint(pendulum_equations, initial_state, time, args=(g, L))
theta = solution[:, 0]

# Convert to cartesian coordinates
x = L1 * np.sin(theta)
y = -L1 * np.cos(theta)

# Create the animation
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.set_xlim(-1.2 * L1, 1.2 * L1)
ax.set_ylim(-1.2 * L1, 0.2 * L1)
ax.set_aspect('equal')
ax.grid(True)

# Initialize the pendulum arm and ball
ax.set_title("Pendulum Animation")
line, = ax.plot([], [], 'o-', lw=2, label="Pendulum Arm")  # Pendulum arm
bob, = ax.plot([], [], 'ro', markersize=10,
               label="Pendulum Ball")  # Pendulum bob

# Animation function


def animate(i):
    # Update the pendulum arm
    line.set_data([0, x[i]], [0, y[i]])
    # Update the pendulum bob
    bob.set_data(x[[i]], y[[i]])
    return line, bob


# Create the animation
ani = FuncAnimation(fig, animate, frames=len(time), interval=20, blit=True)

# Add a legend
ax.legend()

# Show the animation
plt.show()
