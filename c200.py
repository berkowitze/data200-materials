import os
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import pandas as pd

print('wide_data (original):')
wide_data = pd.read_csv('datasets/clean/fertility-two-countries-example.csv')
print(wide_data)

raw_dat = pd.read_csv('datasets/clean/life-expectancy-and-fertility-two-countries-example.csv')

# gather equivalent
long_data = wide_data.melt(id_vars='country',
                           var_name='year',
                           value_name='fertility')
print('long_data (tidied):')
print(long_data.head())

# spread equivalent
rewidened_data = long_data.pivot(index='country', columns='year', values='fertility')
print('rewidened_data:')
print(rewidened_data)


# A separate equivalent (there are other ways to do this)
def doit(substr):
    cols = raw_dat.columns

    # tidy ('gather'/'lengthen') columns that contain the substring
    filt_dat = raw_dat.melt(id_vars='country',
                            value_vars=[c for c in cols if substr in c],
                            value_name=substr)
    # match yyyy_variable and extract yyyy
    splitter = r"([0-9]{4})_(.*)"
    # set year column
    filt_dat['year'] = filt_dat.variable.str.split(splitter, expand=True,)[1]

    # set the index to be (year, country) and get rid of the variable column
    return filt_dat.set_index(['country', 'year']).drop(columns=['variable'])

fert = doit('fertility')
lexp = doit('life_expectancy')
separated_data = pd.merge(lexp, fert, on=['year', 'country']).reset_index()
print('separated_data:')
print(separated_data.head())

# no unite equivalent, doesn't seem relevant for this example