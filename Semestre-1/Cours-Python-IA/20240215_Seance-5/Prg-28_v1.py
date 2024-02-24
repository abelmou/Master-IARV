def carre(n) :
    return n * n

liste = [1, 2, 3, 4, 5, 6, 7]

carres = map(carre, liste)
liste_carres = list(carres)

print("Liste :", liste)
print("Liste Carrés :", liste_carres)