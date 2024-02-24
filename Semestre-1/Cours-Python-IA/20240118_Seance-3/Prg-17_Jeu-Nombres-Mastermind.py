import random
import string

def creer_nombre() :
    return ''.join(random.sample(string.digits, k=4))

def tester(reponse_joueur, nombre_correct) :
    blanc = 0
    rouge = 0
    for i in range(4) :
        if (nombre_correct[i] == reponse_joueur[i]) :
            blanc += 1
        for j in range(4) :
            if ((i != j) and (nombre_correct[i] == reponse_joueur[j])):
                rouge += 1
    resultat = [rouge, blanc]
    return resultat

compteur = 1
nombre_correct = creer_nombre()
# print(nombre_correct)
while(compteur <= 10):
    reponse_joueur = input(F"Tentative {compteur} : ")
    resultat = tester(reponse_joueur, nombre_correct)
    if(resultat == [0, 4]):
        print("Correct ! Nombre Correct :", nombre_correct)
        break
    else :
        print(resultat[0], "Rouges -", resultat[1], "Blancs")
    compteur += 1

if(compteur >= 10):
    print("Vous avez perdu, voila le Nombre Correct :", nombre_correct)