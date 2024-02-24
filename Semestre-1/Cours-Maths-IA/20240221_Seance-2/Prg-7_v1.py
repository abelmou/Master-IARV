from math import exp
from scipy import integrate

def f(x) :
    return exp(-x)

print("Probabilité :", integrate.quad(f, 1, 2)[0])