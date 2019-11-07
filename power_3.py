"""
created by: Sk Rakeeb
created on:06/11/19
created for: assignment1.

"""

from math import *
L = [1,2,4,8,16,32,64]
X = 5
for i in range(len(L)):
    if 2**X == L[i]:
        s=L[i]
    i=i+1
print (L.index(s))
