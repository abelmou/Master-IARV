import random

chaine_alpha_maj = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chaine_alpha_min = "abcdefghijklmnopqrstuvwxyz"
chaine_chiffre = "0123456789"
chaine_special = "*#/!$"

mot_de_passe = ''.join(random.sample(chaine_alpha_maj, 2))
mot_de_passe += ''.join(random.sample(chaine_alpha_min, 2))
mot_de_passe += ''.join(random.sample(chaine_chiffre, 2))
mot_de_passe += ''.join(random.sample(chaine_special, 2))

print("Mot De Passe :", mot_de_passe)