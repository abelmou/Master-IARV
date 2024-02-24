import math

def factorielle(nombre):
    if(nombre == 0 or nombre == 1):
        return 1
    else:
        return nombre * factorielle(nombre - 1)

nombre = int(input("Donnez un nombre : "))

print("Factorielle :", factorielle(nombre))