import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def r(x,a, **kwargs):
    pars = kwargs.get("parameters", [1,1,1])
    kappa = pars[0]
    c = np.log(a) - kappa * x **2
    return c


def f(x,a, **kwargs):
    par = kwargs.get('parameters',[1,1,1])
    b = par[1]
    q = par[2]
    dynamic = b * x + (x ** q) / (1 + x ** q) + a
    return dynamic


def kdcost(k, beta, x, a, **kwargs):
    cbk = beta ** k * r(x,a, **kwargs)
    return cbk

# Discount Factor
beta = 0.5

# Parameters
kappa = 1.2
b = 1
q = 1.4

# Stop
epsilon = 0.1


# states and actions space
nx = 100
xs = np.linspace(0, 2.5, nx)
ax = xs



v0 = np.zeros(nx)
v1 = np.ones(nx)


def error(v):
    euc = 1 / nx * np.sum(v ** 2)
    return euc

step = 0

bells = {}
optim = {}

while 1:
    nu = CubicSpline(xs, v0)
    ft = b * xs + (xs ** q) / (xs ** q + 1) + ax
    nut = [nu(t) for t in ft]
    vnut = np.array(nut)
    ntop, npos = vnut.max(), vnut.argmax()
    nu = np.log(v0) - kappa * xs ** 2 

