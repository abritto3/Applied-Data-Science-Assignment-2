'''
Importing the modules 
stats module is imported to calculate the Skew and Kurtosis values of a data set
'''   
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import stats
import seaborn as sns

def read_file(filename, Countries, Years):
    """The function read_file is defined to read the excel file and will
    return 2 data frames, one with countries as columns and one with years as
    columns"""
    #Read the data set and delete the first 3 rows of the excel file containing irrelevent data
    x = pd.read_excel(filename, skiprows=3)
    x.drop(columns = ['Country Code', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)
    #index the country name column
    x.set_index(['Country Name'], inplace=True)
    #Call the data set containing only the relevant Countries and Years
    y = x.iloc[Countries, Years]
    #Retrieve the transpose of the data set
    z = y.T
    #Return the data set and the transposed data set
    return y, z

def heat_map(filename, Country, heat_i, cma):
    """The function heat_map is used to plot a heat map taking in the excel file containing
    the initial data set, the particular country, indicators, years and the heat map 
    colour scheme as it's arguments
    """
    a = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Climate Change.xls", skiprows = 3)
    #Drop the irrelevant columns from the data set 
    a.drop(columns = ['Country Code' , 'Indicator Code'], axis=1, inplace=True)
    #Select the columns containing the specified country
    b = a[a.iloc[:,0] == str(Country)]
    b.drop('Country Name' , axis=1, inplace=True)
    b.set_index('Indicator Name', inplace=True)
    #Transpose the data set with year as rows and indicators as columns
    b = b.T
    #retrieve the data set with only the required indicators
    c = b.loc[:, heat_i]
    plt.figure(figsize = (10, 5))
    #Plot the heat map
    sns.heatmap(c.corr(), vmin=-1, vmax=1, annot=True, cmap = str(cma), fmt=".3f")
    #Set the title of the map as country name
    plt.title(str(Country))
    return

#Array containing the index of the required countries
Countries = [35, 40, 55, 81, 109, 119, 70, 205, 251]
#Array containing the index of required years 1995 -2010
Years = [35, 40, 45, 50]

'''Retrieve the data sets into the first set and the transpose of the same in the second set
   Pass the file name and the array containing indexes of Countries and Years as the arguments
   to the function
'''
co2_1, co2_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\CO2 emissions (kt).xls", Countries, Years)
electric_1, electric_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Electric power consumption (kWh per capita).xls", Countries,Years) 
ren_1, ren_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Renewable electricity output (% of total electricity output).xls", Countries,Years) 
energy_1, energy_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Energy use (kg of oil equivalent per capita).xls", Countries,Years) 

'''Plot the graphs with the data sets retrieved and set the title and and labels
   Rotate the x ticks so that the country names do not intertwine in the graph
'''
co2_1.plot(kind="bar", alpha = 0.8)
plt.title("CO2 emissions rate")
plt.xlabel("Countries")
plt.ylabel("CO2 emissions (kt)")
plt.xticks(rotation = 45)

electric_1.plot(kind="bar")
plt.title("Electric power consumption rate")
plt.xlabel("Countries")
plt.ylabel("Electric power consumption (kWh per capita)")
plt.legend(loc='upper right', bbox_to_anchor=(1.3, 1), borderaxespad=0)
plt.xticks(rotation = 45)

ren_1.plot(kind="line")
plt.title("Renewable electricity output ")
plt.xlabel("Countries")
plt.ylabel("Renewable electricity output (% of total electricity output)")
plt.xticks(rotation = 45)

energy_1.plot(kind="line")
plt.title("Total energy use")
plt.xlabel("Countries")
plt.ylabel("Energy use (kg of oil equivalent per capita)")
plt.xticks(rotation = 45)

plt.show()

#Array containing the indicator names specifying the indicators needed to plot on the heat maps
heat_indicators = ["Annual freshwater withdrawals, total (billion cubic meters)", "Population growth (annual %)", "Methane emissions (kt of CO2 equivalent)", "Electricity production from oil sources (% of total)", "Electric power consumption (kWh per capita)"]
#Plot two heat maps with different country names  and the indicators and map collor scheme as arguments
heat_map(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Climate Change.xls", "United States", heat_indicators, 'Pastel1')
heat_map(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Climate Change.xls", "Spain", heat_indicators, 'Set3')

#Print the Skew and Kurtosis of a used data set
print("Skew:", stats.skew(ren_1["1995"]))
print("Kurtosis", stats.kurtosis(ren_1["1995"]))
