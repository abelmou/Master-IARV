import random

liste_mots = ["python", "programme", "algorithme", "intelligence", "artificielle"]
mot_correct = random.choice(liste_mots)
# print(mot_correct)

mot_reponse = ["_ "] * len(mot_correct)
compteur = 1
while(compteur <= len(mot_correct) + 10) :
    reponse_joueur = input("Mot : " + ''.join(mot_reponse) + "\tTentative " + str(compteur) + " : ")
    for i in range(len(mot_correct)) :
        if(mot_correct[i] == reponse_joueur[0].lower()):
            mot_reponse[i] = reponse_joueur.lower() + " "

    if("_" not in ''.join(mot_reponse)):
        print("Correct !", mot_correct)
        break
    compteur += 1
    
if(compteur > len(mot_correct) + 3):
    print("Vous avez perdu, voila le mot Correct :", mot_correct)