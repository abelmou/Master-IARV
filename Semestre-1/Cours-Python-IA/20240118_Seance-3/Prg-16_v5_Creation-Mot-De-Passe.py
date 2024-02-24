import random
# import secrets
import string

def tester_force(mot_de_passe) :
    chaine_alpha_maj = string.ascii_uppercase # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    chaine_alpha_min = string.ascii_lowercase # "abcdefghijklmnopqrstuvwxyz"
    chaine_chiffre = string.digits # "0123456789"
    chaine_special = string.punctuation # "*#/!$"

    existe_alpha_maj = False
    existe_alpha_min = False
    existe_chiffre = False
    existe_special = False

    for i in mot_de_passe :
        if (i in chaine_alpha_maj):
            existe_alpha_maj = True
        elif (i in chaine_alpha_min):
            existe_alpha_min = True
        elif (i in chaine_chiffre):
            existe_chiffre = True
        elif (i in chaine_special):
            existe_special = True

    if existe_alpha_maj and existe_alpha_min and existe_chiffre and existe_special:
        return True
    else :
        return False

def creer_mot_de_passe() :
    chaine_lettre = string.ascii_letters
    chaine_chiffre = string.digits
    chaine_special = string.punctuation
    chaine = ''.join(random.choices((chaine_lettre + chaine_chiffre + chaine_special), k=8))

    # chaine = ""
    # for _ in range(8):
    #     chaine += secrets.choice(chaine_lettre + chaine_chiffre + chaine_special)

    return chaine

# mot_de_passe = str(input("Mot de passe : "))
# print("Force :", tester_force(mot_de_passe))

while True:
    mot_de_passe = creer_mot_de_passe()
    if(tester_force(mot_de_passe)):
        print("Mot de passe :", mot_de_passe)
        break