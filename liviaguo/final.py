
# coding: utf-8

# In[6]:

import csv
import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib
import matplotlib.pyplot as plt

df = pd.read_csv('C:/Users/liviag/Desktop/final-exercise/gapminder_gdp_americas.csv')
gdp = df.ix[:,'gdpPercap_1952':]
gdp = gdp.rename( columns=lambda x: int(x.lstrip('gdpPercap_')),inplace=False)
gdpmean = gdp.mean(axis=0)
#print(gdpmean)
plot=gdpmean.plot(x='Year',y='Average GDP', kind='bar', title='Average GDP across all countries')
fig = plot.get_figure()
fig.savefig('final.png')


# In[ ]:



