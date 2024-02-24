def est_premier(nombre):
    if(nombre == 0 or nombre == 1):
        return False
    for i in range(2, nombre // 2 + 1):
        if (nombre % i == 0):
            return False
    return True

while(True):
    nombre = input("Donnez un nombre (ou tapez 'exit' pour quitter) : ")
    if(nombre.lower() == "exit"):
        break
    print(nombre, "est", "" if est_premier(int(nombre)) else "non", "premier\n")