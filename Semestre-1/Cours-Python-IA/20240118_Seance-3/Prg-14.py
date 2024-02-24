def sans_duplication(liste1) :
    # return list(set(liste1))
    liste2 = []
    for i in liste1 :
        if i not in liste2 :
            liste2.append(i)
    return liste2

liste_avec_duplication = [1, 3, 5, 5, 7, 9, 7, 1, 3]
liste_sans_duplication = sans_duplication(liste_avec_duplication)

print("Liste avec duplication : ", liste_avec_duplication)
print("Liste sans duplication : ", liste_sans_duplication)