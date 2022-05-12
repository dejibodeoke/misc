# -*- coding: utf-8 -*-
"""
Created on Thu May 12 16:06:39 2022

@author: deji.bodeoke
"""

"""script is used to read in digitized profile and in return, the polynomial
equation is extracted"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


start=0
stop=50
n_steps=100

#filepath
filepath=r'C:\Users\deji.bodeoke\Downloads\temp_profile.csv'

#read data file
files=pd.read_csv(filepath, header=None)
xp=files[files.columns[0]]
fp=files[files.columns[1]]

#get polynomial coeffiecients
coeffs=np.polyfit(xp,fp,10)

#fitted data
x=np.linspace(start,stop,n_steps)
y=np.polyval(coeffs,x)

#compare the curve fit to the data
plt.plot(xp,fp,'o',x,y)