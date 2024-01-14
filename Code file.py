import pandas as pd # Importing pandas library as pd
import numpy as np # Importing numpy library as np
import matplotlib.pyplot as plt # Importing Linear Regression library from sklearn.linear_model

# Reading the data into Python numpy array
data7= np.array(pd.read_csv('inputdata7.csv')) # Reads the csv file into numpy array
print("the input data 7 as an array: \n", data7) # Printing the data into an array
rainfall_array = data7[:, 0] # Creating the columns as numpy array variables
productivity_array = data7[:, 1] # Creating the columns as numpy array variables
print("the rainfall column: \n", rainfall_array) # Prints the Rainfall array column
print("the productivity column: \n", productivity_array) # Prints the Rainfall array column

plt.figure(figsize=(8,6)) # To Create a figure
plt.scatter(rainfall_array, productivity_array, color  = 'green',label='Rainfall vs Productivity') # Plotting the scatter plot for rainfall vs productivity
plt.title('Rainfall vs Productivity', fontsize = 20) # Defining the title of the plot
plt.xlabel('Rainfall', fontsize = 13 ) # Defining the X-Label 
plt.ylabel('Productivity', fontsize = 13) # Defining the Y-Label
plt.legend(loc='upper left') # Defining the legend
plt.show() # To Show the plot

f, g = np.polyfit(rainfall_array, productivity_array, 1) # Fitting using the numpy
slope = f # Defining the slope
intercept = g # Defining the intercept
predict = np.poly1d([f, g]) # Creating polynomial object from the coefficients,
y_pred = predict(rainfall_array) # Prediciting the y_pred variable
print(y_pred) # Printing the y_pred values

# Predicting y value for the given x value
predicted_x = 310 
predicted_y = predict(predicted_x)
x = predicted_x
y = slope * x + intercept
productivity_coefficient = slope * x + intercept # Finding the productivity coefficient
print(f"Productivity coefficient for x={x}: {productivity_coefficient}") # Printing the Productive coefficient

# Create text labels
x1 = "Rainfall: " + str(predicted_x) + "mm"
y1 = "Predicted coefficient: " + str(productivity_coefficient)

plt.figure(figsize=(8,6)) # To Create the figure
plt.plot(rainfall_array, y_pred,color='blue',label='Regression Line') # plotting the regression line
plt.scatter(predicted_x, predicted_y, c='green', marker='8', edgecolor='black', label='Predicted point', s=42) # plotting the predicted plot
plt.scatter(rainfall_array, productivity_array,color='magenta',label='Rainfall vs Productivity', s=42) # plotting the rainfall vs productivity plot
plt.title('Rainfall Vs Productivity',fontsize=20) # Defining the title of the plot
plt.xlabel('Rainfall',fontsize=15) # Defining the x label
plt.ylabel('Productivity',fontsize=15) # Defining the y label
plt.text(60, .0808, x1, fontsize=10) # To print the text on the plot
plt.text(60, .0770, y1, fontsize=10) # To print the text on the plot
plt.legend(loc='upper left') # To show the legend
plt.show() # To show the plot