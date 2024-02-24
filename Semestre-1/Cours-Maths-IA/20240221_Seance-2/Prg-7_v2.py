from math import exp

def f(x) :
    return exp(-x)

def methode_rectangle(f, a, b, n):
    resultat = 0
    largeur_interval = (b - a) / n
    for i in range(n):
        x_i = a + i * largeur_interval
        resultat += f(x_i)
    resultat *= largeur_interval
    return resultat

n = int(input("Donnez n : "))
print("Probabilité :", methode_rectangle(f, 1, 2, n))
