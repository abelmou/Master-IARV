import random

nombre_secret = random.randint(1, 10)
# print("Nombre Secret :", nombre_secret)

while(True):
    nombre_joueur = input("Donnez un nombre entre 1 et 10 (ou tapez 'exit' pour quitter) : ")
    if(nombre_joueur == "exit"):
        break
    elif((int)(nombre_joueur) > nombre_secret):
        print("Inferieur")
    elif((int)(nombre_joueur) < nombre_secret):
        print("Superieur")
    elif((int)(nombre_joueur) == nombre_secret):
        print("Correct !")
        break