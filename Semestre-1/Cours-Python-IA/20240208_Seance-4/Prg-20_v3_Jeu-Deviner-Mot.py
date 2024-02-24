import random

def melanger(mot):
    mot2 = list(mot)
    # print(''.join(mot2))
    random.shuffle(mot2)
    return mot2

liste_mots = ["Conversation", "Information", "Actuellement", "Jointure", "Organisation", "Données", "Association"]
mot = random.choice(liste_mots)
# print("Mot choisi :", mot)
mot2 = melanger(mot)
print("Veuillez deviner le mot :", ''.join(mot2))

compteur = 0
hint = 1
while(compteur < 5) :
    reponse_joueur = input("Tentative " + str(compteur + 1) + ' (ou tapez "hint" pour un indice) : ')
    if((reponse_joueur.lower() == "hint")):
        if(hint == 1):
            hint_1_mot = "\033[92m" + ''.join(mot[0:2]) + "\033[0m" + ''.join(mot2[2:])
            print(f"Hint {hint} :", hint_1_mot)
        elif(hint == 2):
            hint_2_mot = "\033[92m" + ''.join(mot[0:2]) + "\033[0m" + ''.join(mot2[2:-2]) + "\033[92m" + ''.join(mot[-2:]) + "\033[0m"
            print(f"Hint {hint} :", hint_2_mot)
        elif(hint == 3):
            length = (int)(len(mot) / 2)
            hint_3_mot = ( "\033[92m" + ''.join(mot[0:2]) + "\033[0m"
                           + ''.join(mot2[2:(length - 1)]) + "\033[92m" + ''.join(mot[(length - 1):(length + 1)]) + "\033[0m" + ''.join(mot2[(length + 1):-2])
                           + "\033[92m" + ''.join(mot[-2:]) + "\033[0m")
            print(f"Hint {hint} :", hint_3_mot)
        else:
            print("Vous avez dépassé 3 Hints !")
        hint += 1
    else:
        if(reponse_joueur == mot or reponse_joueur == mot.lower()) :
            print("Correct !", mot, "- Score :", (5 - compteur), "/ 5")
            break
        print(f"Faux ! Il vous reste {5 - compteur - 1} tentatives !")
        compteur += 1
    
if(compteur > 5):
    print("Vous avez perdu, voila le mot Correct :", mot)