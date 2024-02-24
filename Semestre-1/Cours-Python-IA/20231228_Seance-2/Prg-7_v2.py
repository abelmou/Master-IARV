import random

nombre_secret = random.randint(1, 10)
# print("Nombre Secret :", nombre_secret)

nombre_tentatives = 0

while(nombre_tentatives < 5):
    nombre_joueur = input("Donnez un nombre entre 1 et 10 (ou tapez 'exit' pour quitter) : ")
    nombre_tentatives += 1
    if(nombre_joueur == "exit"):
        break
    elif((int)(nombre_joueur) > nombre_secret):
        print("Tentative", nombre_tentatives,": Inferieur")
    elif((int)(nombre_joueur) < nombre_secret):
        print("Tentative", nombre_tentatives,": Superieur")
    elif((int)(nombre_joueur) == nombre_secret):
        print("Tentative", nombre_tentatives,": Correct !")
        break

if(nombre_tentatives >= 5):
    print("\nVous avez dépassé le nombre de tentatives possible !\nNombre Secret : ", nombre_secret)