import numpy as np
import matplotlib.pyplot as plt

# Function to compute the electric potential due to a single charge
def electric_potential(q, r0, x, y):
    
    x0, y0 =r0   # Extract charge position
    dx = x -x0  # Distance in x-direction from charge to grid points
    dy = y -y0  # Distance in y-direction from charge to grid points
    r =np.sqrt(dx**2 + dy**2)  # distance from charge to each grid point
    r =np.where(r != 0, r, np.inf)  # Avoid division by zero by replacing r=0 with infinity
    V =q/r  # Electric potential formula (ignoring Coulomb's constant for simplicity)
    return V

# Define charges and their positions
charges = [
    (1, (0, 1)),   # +1 C at (0,1)
    (1, (0, -1)),  # +1 C at (0,-1)
    (-1, (1, 0)),  # -1 C at (1,0)
    (-1, (-1, 0))  # -1 C at (-1,0)
]

# Create a grid of points where the potential will be calculated
x_range = np.linspace(-2, 2, 100)  # x-coordinates from -2 to 2 with 100 points
y_range = np.linspace(-2, 2, 100)  # y-coordinates from -2 to 2 with 100 points
X, Y = np.meshgrid(x_range, y_range)  # Create a meshgrid for all combinations of x and y

# Initialize the total electric potential array with zeros
V_total = np.zeros(X.shape)

# Compute the total electric potential by summing contributions from all charges
for q, r0 in charges:
    V = electric_potential(q, r0, X, Y)  # Compute potential due to this charge
    V_total += V  # Add this charge's contribution to the total potential

# Plotting the total electric potential as a heatmap
plt.figure(figsize=(6, 6))  # Set figure size

# Use imshow to display the heatmap of the potential
plt.imshow(
    V_total,
    extent=[-2, 2, -2, 2],  # Set bounds of the plot in physical space
    origin='lower', # Ensure (0,0) is at the bottom-left corner
    cmap='hot',# Use 'hot' colormap for visualization
    alpha=0.7 # Slight transparency for better visualization
)

# Add a colorbar to indicate the magnitude of electric potential
plt.colorbar(label="Electric Potential (V)")

# Labeling the axes
plt.xlabel("x-axis") 
plt.ylabel("y-axis")
plt.title("Electric Potential due to Given Charges")

#Marking positions of charges on the plot with scatter points
for q, r0 in charges:
    color = 'red' if q > 0 else 'blue'   # Use red for positive charges and blue for negative charges
    plt.scatter(
        r0[0], r0[1],   # Charge position on the plot
        color=color,      s=100,                 # Size of scatter point
        edgecolors='black', # Black border around scatter points for visibility
        label=f"q={q} C" # Label showing charge magnitude )

# Add legend to identify charges visually on the plot
plt.legend()
# Adding grid lines 
plt.grid()
plt.show()

