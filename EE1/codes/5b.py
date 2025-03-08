import numpy as np #importing the numpy library 
import matplotlib.pyplot as plt #importing the matplotlib.pyplot

#Here in this code, y is mag of F and x is s

# Defining the function y(x)
def y(x):
    return np.sqrt(((40/(x*x+1)+3*np.sqrt(2))*(40/(x*x+1)+3*np.sqrt(2)))+4)

# Generating x values from -10 to 10
x = np.linspace(-10, 10, 400)

# Calculating corresponding y values
y_values = y(x)

# Creating the plot
plt.figure(figsize=(8, 6))#setting the figuresize(in inches)
plt.plot(x, y_values, label='|F|')#Plotting the points

# Adding title and labels using raw strings
plt.title('Plot of Magnitude v/s s')
plt.xlabel('s')
plt.ylabel('Magnitude')
plt.legend()

# Displaying grid and plot
plt.grid(True)#Display the grid
plt.show()

