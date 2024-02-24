def Fibonacci_Iterative_Liste(nombre):
    Fpp = 0
    Fp = 1
    F = 0
    Liste = [0, 1]
    for i in range(2, nombre + 1):
        F = Fpp + Fp
        Fpp = Fp
        Fp = F
        Liste.append(Fp)
    return Liste

def Fibonacci_Recursive(nombre) :
    if(nombre == 0 or nombre == 1):
        return nombre
    else:
        return Fibonacci_Recursive(nombre - 1) + Fibonacci_Recursive(nombre - 2)

def Fibonacci_Recursive_Liste(nombre):
    Liste = [0, 1]
    for i in range(2, nombre + 1):
        Liste.append(Fibonacci_Recursive(i))
    return Liste

while(True):
    nombre = input("Donnez un nombre (ou tapez 'exit' pour quitter) : ")
    if(nombre == "exit"):
        break
    print("Fibonacci_Iteraive_Liste(",nombre,") : ", Fibonacci_Iterative_Liste((int)(nombre))) # Plus rapide, complexité linéaire
    print("Fibonacci_Recursive_Liste(",nombre,") : ", Fibonacci_Recursive_Liste((int)(nombre)), "\n") # Plus lente, complexité exponentielle