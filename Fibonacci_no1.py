"""
created by: Sk Rakeeb
created on:06/11/19
created for: assignment1.

"""


from math import *
s = [1,1]
for i in range(0,8):
    t = s[i] + s[i+1]
    s.append(t)
print (s)
