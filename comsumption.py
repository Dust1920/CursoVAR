import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


# Parámetros 

irate = 0.06  # 6%
## Estimados por Utility Theory
gamma = 0.5
beta = 0.9

## Condiciones iniciales
N = 20  # Numero de etapas.


def Ak(b, g, i, k):
    if k > N or k<0:
        print("Fuera de Rango")
        return 0
    if k == N:
        return 1
    else:
        p1 = (1 + i)**(1-g) * b
        ak1 = Ak(b, g, i, k + 1)
        p2 = p1 * ak1
        p3 = 1 + p2 ** (1 / g)
        pf = p3 ** g
    return pf


def afk(k):
    """
    Función Ak resumida. 
    """
    return Ak(beta, gamma, irate, k)

def Jk(b, g, i, k, x):
    y = Ak(b, g, i, k) * b ** k * x ** (1 - g)
    return y

def Jfk(k, x):
    y = Jk(beta, gamma, irate, k, x)
    return y


def dyn(i, x,a):
    y = (1 + i) * (x - a)
    return y






xn = np.linspace(0.001,2, 100)  # Mientras más fino mejor.

valsf = np.zeros((N,len(xn)))
optpolicys = np.zeros((N-1,len(xn)))
valsf[0] = beta ** N * (xn) ** (1-gamma)  # JN = CN

for i in range(N - 1):
    for j in range(len(xn)):
        Ax = np.linspace(0.00001, xn[j], 1000)
        ck = beta ** (N - i) * Ax ** (1-gamma)
        xk1 = (1 + irate) * (xn[j] - Ax)
        jfv = [ck[ia] + Jfk(N - i, xk1[ia]) for ia in range(len(Ax))]
        valsf[i + 1, j], a = np.array(jfv).max(), np.array(jfv).argmax()
        optpolicys[i,j] = Ax[a]


# plt.plot(xn, valsf[1])

def optk(x, k):
    f = CubicSpline(x, optpolicys[k])
    return f

## Simulación
x_0 = 1  # Cantidad inicial en millones. 
track = [x_0]

situation = []
for i in range(N - 1):
    opt = optk(xn,  N-2-i)
    xk = (1 + irate) * (x_0 - (opt(x_0)))
    st = [x_0, opt(x_0)]
    track.append(xk)
    situation.append(st)
    x_0 = xk




def optim_crit(S):
    X = [s[0] for s in S]
    A = [s[1] for s in S]
    A = np.array(A)
    p1 = beta ** N * (X[-1]) ** (1 - gamma)
    p2 = np.sum(beta ** np.arange(N - 1) * (A ** (1 - gamma)))
    p = p1 + p2
    return p

plt.plot(list(range(1,N+1)), track, 'ro')
plt.title(f'Valor: {optim_crit(situation)}')
plt.show()
