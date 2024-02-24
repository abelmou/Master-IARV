import random

chaine1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789*#/!$"
chaine2 = ''.join(random.sample(chaine1, 8))

print("Chaine 1 :", chaine1)
print("Chaine 2 :", chaine2)