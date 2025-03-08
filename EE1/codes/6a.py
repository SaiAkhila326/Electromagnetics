import numpy as np
import matplotlib.pyplot as plt

def electric_field(q, r0, x, y):
    x0,y0=r0 #extracting coordinates from r0
    dx = x-x0
    dy=y-y0 #computes displacement vector from charge to point
    r=np.sqrt(dx**2+dy**2)
    r3=np.where(r!=0, r**3,np.inf) #avoid division by zero, sets r^3 to infinity to prevent an error
    Ex=q*dx/r3
    Ey=q*dy/r3# Calculating the Electric field components
    return Ex, Ey

# Defining charge positions and magnitudes
charges = [
    (1, (0, 1)),   # +1 C at (0,1)
    (1, (0, -1)),  # +1 C at (0,-1)
    (-1, (1, 0)),  # -1 C at (1,0)
    (-1, (-1, 0))  # -1 C at (-1,0)
]

# Defining grid for field computation
x_range = np.linspace(-2, 2, 30)  # x from -2 to 2
y_range = np.linspace(-2, 2, 30)  # y from -2 to 2
X, Y = np.meshgrid(x_range, y_range)  # Creating a mesh grid

# Initializing field components(all to 0 first)
Ex_total = np.zeros(X.shape)
Ey_total = np.zeros(Y.shape)

# Compute total electric field at each point
for q, r0 in charges:#r0 is a tuple (x0,y0)
    Ex, Ey = electric_field(q, r0, X, Y)
    Ex_total += Ex
    Ey_total += Ey

# Plotting
plt.figure(figsize=(6,6))#setting the figur size (in inches)
plt.quiver(X, Y, Ex_total, Ey_total, color='b', scale=50, scale_units='xy', width=0.003, headwidth=3, headlength=5)  #plotting the vector lines, scale adjusts the arrow size
plt.xlabel("x-axis") #labelling the x-axis
plt.ylabel("y-axis") #labeling the y-axis
plt.title("Electric Field of Given Charges")
plt.xlim(-2, 2) #sets limits of x-axis
plt.ylim(-2, 2) #sets limits of y-axis

# Plot charge positions
for q, r0 in charges:
    color = 'red' if q > 0 else 'blue' #assigning red color to +ve charges and blue otherwise 
    plt.scatter(r0[0], r0[1], color=color, s=100, edgecolors='black', label=f"q={q} C") #plotting the 4 charges 


plt.legend()
plt.grid()
plt.show()

