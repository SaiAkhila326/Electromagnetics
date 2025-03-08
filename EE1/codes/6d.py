import numpy as np
import matplotlib.pyplot as plt

# Define the electric field from a point charge
def electric_field(q, r0, x, y):
    x0, y0 = r0  # Extract coordinates of the charge
    dx = x - x0  # Calculate displacement along x-axis
    dy = y - y0  # Calculate displacement along y-axis
    r = np.sqrt(dx**2 + dy**2)  # Compute the distance from charge
    r3 = np.where(r != 0, r**3, np.inf)  # Avoid division by zero (set r^3 to infinity if r=0)
    Ex = q * dx / r3  # Electric field in x-direction
    Ey = q * dy / r3  # Electric field in y-direction
    return Ex, Ey

# Define charge positions and magnitudes
charges = [
    (1, (0, 1)),   # +1 C at (0,1)
    (1, (0, -1)),  # +1 C at (0,-1)
    (-1, (1, 0)),  # -1 C at (1,0)
    (-1, (-1, 0))  # -1 C at (-1,0)
]

# Set up grid for computing the electric field
x_range = np.linspace(-2, 2, 30)  # x from -2 to 2
y_range = np.linspace(-2, 2, 30)  # y from -2 to 2
X, Y = np.meshgrid(x_range, y_range)  # Creating mesh grid

# Initialize electric field components
Ex_total = np.zeros(X.shape)
Ey_total = np.zeros(Y.shape)

# Calculate the total electric field due to all charges
for q, r0 in charges:
    Ex, Ey = electric_field(q, r0, X, Y)
    Ex_total += Ex
    Ey_total += Ey

# Numerical calculation of the divergence (using finite difference method)
dx = x_range[1] - x_range[0]  # Grid spacing in x
dy = y_range[1] - y_range[0]  # Grid spacing in y

# Approximate the divergence using the finite difference formula
div_E = (np.gradient(Ex_total, axis=1) / dx) + (np.gradient(Ey_total, axis=0) / dy)

# Plot the divergence of the electric field
plt.figure(figsize=(6,6))
plt.contourf(X, Y, div_E, 20, cmap='coolwarm')  # Contour plot of divergence
plt.colorbar(label="Divergence of Electric Field")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Divergence of Electric Field")
plt.grid()
plt.show()


