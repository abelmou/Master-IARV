from functools import reduce

somme = lambda a, b : a + b

liste = [11, 13, 15, 17, 19]

print("Somme : ", reduce(somme, liste))