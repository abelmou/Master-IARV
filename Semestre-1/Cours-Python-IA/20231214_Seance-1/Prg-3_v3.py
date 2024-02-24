liste1 = [1, 3, 5, 7, 9]
liste2 = [2, 4, 6, 8]

ensemble = set(liste1).intersection(set(liste2))

if (list(ensemble)) :
    print("Ensemble :", ensemble)
else :
    print("Ensemble vide")