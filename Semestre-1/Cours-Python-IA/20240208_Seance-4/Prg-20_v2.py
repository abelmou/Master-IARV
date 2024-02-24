import random

def melanger(mot):
    mot = list(mot)
    random.shuffle(mot) # Mélange les lettres du mot
    return ''.join(mot)

liste_mots = ["Jeu", "Livre", "Bien", "Jointure", "Stylo", "Données"]
mot = random.choice(liste_mots)
# print("Mot choisi :", mot)
mot2 = melanger(mot)
print("Veuillez deviner le mot :", ''.join(mot2))

compteur = 1
while(compteur <= 5) :
    reponse_joueur = input("Tentative " + str(compteur) + " : ")
    if(reponse_joueur == mot or reponse_joueur == mot.lower()) :
        print("Correct !", mot)
        break
    print(f"Faux ! Il vous reste {5 - compteur} tentatives !")
    compteur += 1
    
if(compteur > 5):
    print("Vous avez perdu, voila le mot Correct :", mot)