import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# Numero de Etapas
steps = 20


# Parametros (Segun el problema)
gamma = 0.5
beta = 0.9  # 
ir = 0.06  # Tasa de Interes
pars = [gamma, beta, ir, steps]

## Iteración hacia atrás
apd_steps = list(range(steps))
apd_steps = apd_steps[::-1]

## Conjunto de estados

states = np.linspace(0.001,5,10)

jfunctions = pd.DataFrame(0, index=apd_steps, columns=states)

def last_pay(x):
    p1 = pars[0]
    p2 = pars[1]
    p3 = pars[2]
    p4 = pars[3]
    y = p2 ** p4 * x ** (1 - p1)
    return y
npay = np.vectorize(last_pay)

jfunctions.loc[steps - 1] = npay(states)  # J_N
print(jfunctions.shape)

for k in jfunctions.index:
    for x_n in states:
        Ax = np.linspace(0.00001, x_n, 100)
        ck = (beta ** k) * Ax ** (1 - gamma)
        fx = (1 + ir) * (x_n - Ax)  # Puntos a evaluar.
        interf = CubicSpline(states, jfunctions.loc[int(k)])
        fadjust = [interf(x) for x in fx]
        jfunctions.loc[int(k - 1), x_n] = np.max(ck + np.array(fadjust))
    if k == 1:
        break
print(jfunctions)




grafica, ax = plt.subplots(nrows=2, ncols=2)
ax[0,0].plot(states, jfunctions.loc[19], color = 'red', linestyle = '-.')
ax[0,0].plot(states, jfunctions.loc[19],
             color = 'blue', linestyle = 'dotted',linewidth = 5)
ax[0,0].set_title(r'$J_N$')
ax[0,1].plot(states, jfunctions.loc[0])
ax[0,1].set_title(r'$J_0$')
plt.show()




