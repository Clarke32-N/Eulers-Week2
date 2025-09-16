#Imports
import numpy as np
import matplotlib.pyplot as plt
#Function
def diff(x,t):
    f = t - x**2
    return f
#Initial Values
h = 0.05
x0 = np.array([3,1,0,-0.7])
t_max = 9
t0 = 0
dt = 0.1

#Function Loop
x = x0
t = t0
x_values = [x0]
t_values = [t0]

for a in x:    
    while t <= t_max:
        x = x + h*diff(x,t)
        t = t + h
        x_values.append(x)
        t_values.append(t)
#sqrt(t) line
for a in t_values:
    y = np.sqrt(t_values)
#Graph
plt.plot(t_values,y,color="black",linestyle="--",label="sqrt(t)")  
plt.plot(t_values,x_values,color="black")
plt.xlabel('Time (s)')
plt.ylabel('x')
plt.title("x vs. t ")
plt.legend()
plt.show()
