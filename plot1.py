import pandas as pd
from matplotlib import pyplot


dataset1 = pd.read_csv('/Users/stewart22/Desktop/CSCI040/hw_02/country_populations.csv')
uk = dataset1[dataset1.Location == 'United Kingdom']
france = dataset1[dataset1.Location == 'France']

pyplot.plot(france.Time, france.PopTotal / 10**6)
pyplot.plot(uk.Time, uk.PopTotal / 10**6)
pyplot.title('Population Comparison and Multiple Projections for France and the UK, 1950-2100')
pyplot.legend(['France', 'United Kingdom'])
pyplot.xlabel('Year')
pyplot.ylabel('Population in Millions')
pyplot.show()








