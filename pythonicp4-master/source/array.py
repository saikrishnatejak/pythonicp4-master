import numpy as np  #import numpy
number=np.random.randint(0,20,(10,10))
print(number)  #print the number
min,max = number.min(axis=1),number.max(axis=1) #here we are doing it based on row wise so, axis=1
print("Minimum Elements of 10 size Array is",min)# print elements of the minimum elements of the rows
print("Maximum Elements of 10 size Array is",max)#prints the maximum elements of the rows
