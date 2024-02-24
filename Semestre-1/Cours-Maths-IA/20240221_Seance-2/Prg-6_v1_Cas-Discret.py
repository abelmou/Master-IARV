from math import sqrt

def esperance(X) :
    n = 0
    somme = 0
    for i in X:
        n += 1
        somme += i
    return somme / n

def variance(X) :
    n = 0
    somme = 0
    for i in X:
        n += 1
        somme += (i - esperance(X)) ** 2
    return somme / n

X = [7, 5, 4, 9, 12, 45]
    
print("Esperance :", esperance(X))
print("Variance :", variance(X))
print("Écart-type :", sqrt(variance(X)))