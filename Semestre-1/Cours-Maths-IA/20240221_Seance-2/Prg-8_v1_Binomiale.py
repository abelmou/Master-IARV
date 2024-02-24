from math import comb

def binomiale(n, p, k) :
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

print("Binomiale :", binomiale(10, 1/2, 2))