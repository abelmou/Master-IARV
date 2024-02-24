import random

# Génerer une taille aléatoire entre 1 et 7
taille = random.randint(1, 7)
print("Taille :", taille)

# Génerer une liste aléatoire de nombres entre 10 et 70
liste = []
for i in range(taille) :
    liste.append(random.randint(10, 70))
print("Liste :", liste)