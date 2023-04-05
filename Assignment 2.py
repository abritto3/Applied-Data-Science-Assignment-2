   
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gmean, variation
from scipy.stats import stats
from matplotlib import cm
import seaborn as sns

def read_file(filename, Countries, Years):
    """The function read_file is defined to read the excel file and will
    return 2 dataframes, one with countries as coloumns and one with years as
    coloumns"""
    x = pd.read_excel(filename, skiprows=3)
    x.drop(columns = ['Country Code', 'Indicator Name', 'Indicator Code'], axis=1, inplace=True)
    x.set_index(['Country Name'], inplace=True)
    y = x.iloc[Countries, Years]
    z = y.T

    return y, z

def heat_map(filename, Country, heat_i, heat_y, cma):
    a = pd.read_excel(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Climate Change.xls", skiprows = 3)
    a.drop(columns = ['Country Code' , 'Indicator Code'], axis=1, inplace=True)
    b = a[a.iloc[:,0] == str(Country)]
    b.drop('Country Name' , axis=1, inplace=True)
    b.set_index('Indicator Name', inplace=True)
    b = b.T
    c = b.loc[:, heat_i]
    plt.figure(figsize = (10, 5))
    sns.heatmap(c.corr(), vmin=-1, vmax=1, annot=True, cmap = str(cma), fmt=".3f")
    plt.title(str(Country))
    return

#Countries = [35, 40, 55, 81, 109, 119, 202, 205, 251]
Countries = [35, 40, 55, 81, 109, 119, 70, 205, 251]
Years = [35, 40, 45, 50]

co2_1, co2_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\CO2 emissions (kt).xls", Countries, Years)
electric_1, electric_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Electric power consumption (kWh per capita).xls", Countries,Years) 
ren_1, ren_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Renewable electricity output (% of total electricity output).xls", Countries,Years) 
energy_1, energy_2 = read_file(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Energy use (kg of oil equivalent per capita).xls", Countries,Years) 

co2_1.plot(kind="bar", alpha = 0.8)
plt.title("CO2 emissions rate")
plt.xlabel("Countries")
plt.ylabel("CO2 emissions (kt)")
plt.xticks(rotation = 45)

electric_1.plot(kind="bar")
plt.title("Electric power consumption rate")
plt.xlabel("Countries")
plt.ylabel("Electric power consumption (kWh per capita)")
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

heat_indicators = ["Annual freshwater withdrawals, total (billion cubic meters)", "Population growth (annual %)", "Methane emissions (kt of CO2 equivalent)", "Electricity production from oil sources (% of total)", "Electric power consumption (kWh per capita)"]
heat_years = ['2000','2005','2010','2015','2020']

heat_map(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Climate Change.xls", "China", heat_indicators, heat_years, 'prism')
heat_map(r"C:\Users\HP\OneDrive - University of Hertfordshire\Assignments\Assignment 2\Climate Change.xls", "India", heat_indicators, heat_years, 'prism')

print("Skew:", stats.skew(ren_1["1995"]))
print("Kurtosis", stats.kurtosis(ren_1["1995"]))
