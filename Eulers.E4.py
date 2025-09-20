import numpy as np
import matplotlib.pyplot as plt

t0 = 0
x0 = 0
v0 = 1
t_max = 35
dt = ([0.05, 0.025, 0.0125, 0.00626, 0.005])



def func(x0, v0, t0, t_max, dt):
    x, v, t = x0, v0, t0
    x_values = [x]
    v_values = [v]
    t_values = [t]
    while t <= t_max:
        xinit = x + x * dt
        vinit = v - v * dt
        x = x + 0.5 * dt * (v + vinit)
        v = v - 0.5 * dt * (x + xinit)
        t = t + dt
        x_values.append(x)
        v_values.append(v)
        t_values.append(t)
    
    return np.array(x_values), np .array(v_values), np.array(t_values)

def sine(x,t):
    x_calc , t_calc = [x],[t]
    while t <= t_max:
        x = np.sin(t)
        t = t + dt[0]
        x_calc.append(x)
        t_calc.append(t)
    return x_calc, t_calc
        
x_calc, t_calc = sine(x0, t0)


fig, ax = plt.subplots(1,2)
for a in dt:
    x_vals, v_vals, t_vals = func(x0, v0, t0, t_max, a)
    ax[0].plot(t_vals, x_vals, label="Euler dt={a}")
    ax[1].plot(t_vals, v_vals, label="Euler dt={a}")

ax[0].set_title("Euler's aproximation")
ax[0].set_xlabel("time(s)")
ax[0].set_ylabel("x(t)")     

#ax[1].plot(t_calc, x_calc)
plt.show()