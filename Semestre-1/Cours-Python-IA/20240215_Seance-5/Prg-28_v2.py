def sum(a, b) :
    return a + b

liste1 = [11, 13, 15, 17, 19]
liste2 = [19, 17, 15, 13, 11]

somme = map(sum, liste1, liste2)
liste_somme = list(somme)

print("Liste 1 :", liste1)
print("Liste 2 :", liste2)
print("Somme :", liste_somme)