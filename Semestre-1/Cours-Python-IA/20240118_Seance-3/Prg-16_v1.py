import random

liste1 = [1, 2, 3, 4, 5, 6, 7]
liste2 = random.sample(liste1, 5) # Sélection aléatoire Sans Répétition
liste3 = random.choices(liste1, k=5) # Sélection aléatoire Avec Répétition

print("Liste 1 :", liste1)
print("Liste 2 (Sans Répétition) :", liste2)
print("Liste 3 (Avec Répétition) :", liste3)