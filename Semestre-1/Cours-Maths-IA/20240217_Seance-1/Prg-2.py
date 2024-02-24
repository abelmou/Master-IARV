import math

def is_prime(nombre):
    if(nombre == 0 or nombre == 1):
        return False
    for i in range(2, nombre // 2 + 1):
        if (nombre % i == 0):
            return False
    return True

nombre = int(input("Donnez un nombre : "))

print(f"{nombre} est {'premier' if is_prime(nombre) else 'non premier'}")