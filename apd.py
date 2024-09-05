import numpy as np
import pandas as pd

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

states = np.linspace(0.001,5,100)

jfunctions = pd.DataFrame(0, index=apd_steps, columns=states)

def last_pay(x):
    p1 = pars[0]
    p2 = pars[1]
    p3 = pars[2]
    p4 = pars[3]
    y = p2 ** p4 * x ** (1 - p1)
    return y
npay = np.vectorize(last_pay)

jfunctions.loc[steps - 1] = npay(states)

print(jfunctions)
