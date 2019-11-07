"""
created by: Sk Rakeeb
created on:06/11/19
created for: assignment1.

"""

from math import *
s = [1,1]
b=lambda n:s[n] if n<2 else b(n-1)+b(n-2)
for n in range(10):
 print (b(n))

