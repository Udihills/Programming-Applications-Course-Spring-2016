#import numpy and matlibplots module


#generate array of x values from 0 to 6pi

#calculate y values for sin wave

#calculate y values for cosine wave

#plot x and y values for both functions 

#set dashed line for sine wave and solide line for cosine wave

#add legend


#leave comment here with your information
#Name:
#Date:

import numpy, matplotlib
from numpy import sin, cos, pi
from matplotlib import pyplot as plt

#plt.figure(figsize=(38,6))
a = numpy.linspace(0,6*pi,100)
#ysin=sin(a)
#ycos=cos(a)
ysin, ycos = sin(a), cos(a)

plt.plot(a,ysin, linestyle="--")
plt.plot(a,ycos)
plt.ylabel("y")
plt.xlabel("x")
plt.legend(('sin(x)','cos(x)'))
plt.show()
#Arinze Udeh
#01/21/2016