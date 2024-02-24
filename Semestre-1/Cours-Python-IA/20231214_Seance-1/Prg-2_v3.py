nombre = int(input("Saisir un nombre : "))
nombre_tester = int(input("Saisir un nombre à tester : "))

if (nombre % nombre_tester == 0) :
    print(nombre, "est divisible par", nombre_tester)
else :
    print(nombre, "n'est pas divisible par", nombre_tester)