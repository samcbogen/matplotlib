import pandas as pd
from matplotlib import pyplot


dataset2 = pd.read_csv('/Users/stewart22/Desktop/CSCI040/hw_02/cars.csv')
accel = dataset2.Acceleration
horsepower = dataset2.Horsepower
pyplot.scatter(horsepower, accel)
pyplot.title('The Correlation between Horsepower and Acceleration on Historical Cars')
pyplot.xlabel('Horsepower')
pyplot.ylabel('Acceleration')
pyplot.show()





