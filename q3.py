import numpy as np
import matplotlib.pyplot as plt
import statistics
# First we uniformly generate points in the given ellipse
a = 10 #Major axis
b = 5 #Minor axis
weight1 = np.random.uniform(0,1)
weight2 = np.random.uniform(0,1)
weights = np.array([weight1,weight2])# Weight matrix
learn = 10**(-5)
#lst = []
for i in range(1000000):
    print(i)
    x0 = np.random.uniform(-a/2,a/2)
    y0 = np.random.uniform((-b/(2*a))*(np.sqrt((a*a)-(4*x0*x0))),(b/(2*a))*(np.sqrt((a*a)-(4*x0*x0))))
    x = (x0 - y0)/np.sqrt(2)
    y = (x0 + y0)/np.sqrt(2)
    # (x,y) is a random vector sampled unifromly in the required ellipse
    input = np.array([x,y])
    output = np.dot(input,weights)
    weights = weights + learn*output*(input - output*weights)#Updating the weights
    #plt.scatter(x,y,color='blue')
#plt.show()
print('Eigenvector:',weights)
#To compute the Eigenvalue and compute the variance
sum = 0
for j in range(1000000):
    x0 = np.random.uniform(-a/2,a/2)
    y0 = np.random.uniform((-b/(2*a))*(np.sqrt((a*a)-(4*x0*x0))),(b/(2*a))*(np.sqrt((a*a)-(4*x0*x0))))
    x = (x0 - y0)/np.sqrt(2)
    y = (x0 + y0)/np.sqrt(2)
    input = np.array([x,y])
    output = np.dot(input,weights)
    #lst.append(output)
    sum = sum + (output*output)
var = sum/1000000

print('Eigenvalue:',var)
