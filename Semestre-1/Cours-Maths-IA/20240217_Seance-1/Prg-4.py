import random

def proba(nombre):
    compteur = 0
    for _ in range(nombre):
        l1 = random.randint(1,6)
        l2 = random.randint(1,6)
        # print("( T1 :", l1, ", T2 :", l2, ")")
        if(l1 + l2 == 6):
            compteur += 1
    return compteur / nombre

nombre = int(input("Donnez un nombre de tentative : "))
print("Probabilité :", proba(nombre))