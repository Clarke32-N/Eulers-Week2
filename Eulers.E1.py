#Imports
import numpy as np
import matplotlib.pyplot as plt

#Initial Conditions
dt = 0.5         
tmax = 10        
tau = 2.0        
t0 = 0           
N0 = 10         

#Arrays to hold values
t_values = [t0]
N_values = [N0]

#Eulers loop start
t = t0
N = N0

while abs(t - tmax) > dt/2:
    N = N - (N / tau) * dt     
    t = t + dt                 
    N_values.append(N)
    t_values.append(t)

#Eulers Loop End

#Arrays for Calculated curve
t_values = np.array(t_values)
N_values = np.array(N_values)

#Calculated Curve
true_N = N0 * np.exp((-t_values)/tau)
#Error Between Curves
error = np.abs(true_N - N_values)

#Graph 1
fig, axs = plt.subplots(2,1)
axs[0].plot(t_values, N_values, label="Euler's Approximation", color="black",linestyle="--")
axs[0].plot(t_values, true_N, label="Exact Values", color="black")
axs[0].legend()
axs[0].set_title("Exponential Decay using Euler's Method")
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Amount of Nuclei (N)")
#Graph 2
axs[1].plot(t_values, error, 'm-', label="Error")
axs[1].set_title("Error Between Euler and Exact Curves vs. Time")
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Error")
axs[1].legend()

plt.grid(False)
plt.show()

