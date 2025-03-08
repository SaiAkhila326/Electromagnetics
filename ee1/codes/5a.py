import numpy as np #importing numpy library 
import matplotlib.pyplot as plt #import pyplot from matplotlib
#import math #importing the math lib

#In this code, y is mag of F and x is phi

# Defining the function y(x)
def y(x):
    return np.sqrt(38+24*(np.sin(x)+np.cos(x)))

# Generating x values from 10 to 10
x = np.linspace(-10, 10, 400)

# Calculating corresponding y values
y_values = y(x)

# Creating the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y_values, label='|F|')

# Adding title and labels
plt.title(r'Plot of Magnitude v/s angle $\phi$')
plt.xlabel(r'$\phi$')
plt.ylabel('|F|')
plt.legend()

# Displaying the grid and plot
plt.grid(True)
plt.show()

