"""
created by: Sk Rakeeb
created on:06/11/19
created for: assignment1.

"""

# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 23:20:18 2019

@author: user
"""

import matplotlib.pyplot as plt

import numpy as np

freq= np.loadtxt("nasa_txt.txt",delimiter="   ",usecols=[0])
cmb= np.loadtxt("nasa_txt.txt",delimiter="   ",usecols=[1])
frequency=100*freq[:]
cmb_flux=1.0e-20*cmb[:]
plt.plot(frequency,cmb_flux)
plt.xlabel('Frequency(1/m)')
plt.ylabel('CMB Radiation Flux(SI)')
plt.title('Plot of CMB-Flux vs Frequency')
