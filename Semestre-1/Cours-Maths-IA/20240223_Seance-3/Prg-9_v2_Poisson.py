import math

def loi_de_poisson(n, p, k):
    return math.exp(- (n * p)) * ((n * p) ** k) / math.factorial(k)

somme = 0
for i in range(9):
    somme += loi_de_poisson(120, 0.05, i)
    
print("Poisson(n = 120, p = 0.05, k <= 8) :", somme)