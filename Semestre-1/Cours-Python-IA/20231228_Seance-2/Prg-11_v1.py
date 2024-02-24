def est_premier(nombre):
    if(nombre == 0 or nombre == 1):
        return False
    for i in range(2, nombre // 2 + 1):
        if (nombre % i == 0):
            return False
    return True

nombre = int(input("Donnez un nombre : "))
if(est_premier(nombre)):
    print(nombre, "est premier")
else:
    print(nombre, "n'est pas premier")