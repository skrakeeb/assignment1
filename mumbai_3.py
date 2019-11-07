"""
created by: Sk Rakeeb
created on:06/11/19
created for: assignment1.

"""

#by list method

s= "mumbai"
k=[]
for i in s:
    k.append(ord(i))
print ("by list method: ",k)

#by list comprehension method

L= [ord(L) for L in s]
print ("by list comprehension method: ",L)

#by map method

x= map(lambda j: ord(j),s)
print ("by map method: ",(list(x)))
