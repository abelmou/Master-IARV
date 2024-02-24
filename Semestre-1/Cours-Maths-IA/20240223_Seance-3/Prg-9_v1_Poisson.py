import math

def loi_de_poisson(n, p, k):
    return math.exp(- (n * p)) * ((n * p) ** k) / math.factorial(k)

print("Poisson(n = 50, p = 0.04, k = 1) :", loi_de_poisson(50, 0.04, 0))