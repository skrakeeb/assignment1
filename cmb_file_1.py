"""
created by: Sk Rakeeb
created on:06/11/19
created for: assignment1.

"""

import matplotlib.pyplot as plt
import numpy as np 

h=6.625e-34
c=3.0e+8
k=1.38e-23
T=2.725
def u(a):
    I=(2*h*c*a**3)/(np.exp(h*c*a/(k*T))-1.0)
    return I
a=np.arange(200,2500,0.5)
plt.plot(a,u(a),'r-')

plt.xlabel('Frequency(1/m)')
plt.ylabel('Black body Radiation Flux(SI)')
plt.title('Plot of Black body Radiation vs Frequency')
