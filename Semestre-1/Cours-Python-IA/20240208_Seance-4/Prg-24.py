dictionnaire = {}

def saisie(nom, age, poids) :
    dictionnaire[nom] = (age, poids)

def consultation(nom) :
    if(nom in dictionnaire) :
        print("Nom :", nom, "- Age :", dictionnaire[nom][0], "- Poids :", dictionnaire[nom][1])
    else :
        print("Pas d'information !")

def affichage() : 
    for i in dictionnaire.keys() :
        consultation(i)

while(True):
    reponse = input("Saisir votre choix (A:affichage, S:saisie, C:consultation, E:exit) : ").lower()
    if(reponse == "a"):
        affichage()
    elif(reponse == "s"):
        nom = input("Nom : ")
        age = input("Age : ")
        poids = input("Poids : ")
        saisie(nom, age, poids)
    elif(reponse == "c"):
        nom = input("Nom à consulter : ")
        consultation(nom)
    elif(reponse == "e"):
        break