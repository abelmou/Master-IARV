nombre = int(input("Donnez un nombre : "))

diviseurs = []

for i in range(1, int(nombre) + 1):
    if(nombre % i == 0):
        diviseurs.append(i)

print(f"Les diviseurs de {nombre} sont : {diviseurs}")