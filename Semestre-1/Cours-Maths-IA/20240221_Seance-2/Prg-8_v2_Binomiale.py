from math import comb

def binomiale(n, p, k) :
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomiale_inf(n, p, k) :
    sum = 0
    for i in range(k + 1) :
        sum += binomiale(n, p, i)
    return sum

print("Binomiale :", binomiale(10, 1/2, 2))
print("Binomiale (X <= k) :", binomiale_inf(10, 1/2, 2))