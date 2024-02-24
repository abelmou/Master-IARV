def Fibonacci_Iterative(nombre):
    Fpp = 0
    Fp = 1
    F = 0
    for _ in range(2, nombre + 1):
        F = Fpp + Fp
        Fpp = Fp
        Fp = F
    return Fp

def Fibonacci_Recursive(nombre):
    if(nombre == 0 or nombre == 1):
        return nombre
    else:
        return Fibonacci_Recursive(nombre - 1) + Fibonacci_Recursive(nombre - 2)

while(True):
    nombre = input("Donnez un nombre (ou tapez 'exit' pour quitter) : ")
    if(nombre == "exit"):
        break
    print("Fibonacci_Iteraive(",nombre,") : ", Fibonacci_Iterative((int)(nombre))) # Plus rapide, complexité linéaire
    print("Fibonacci_Recursive(",nombre,") : ", Fibonacci_Recursive((int)(nombre)), "\n") # Plus lente, complexité exponentielle