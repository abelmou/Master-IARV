est_pair = lambda x : x % 2 == 0

liste_nombre = [11, 12, 13, 14, 15, 16, 17, 18, 19]

liste_nombre_pair = filter(est_pair, liste_nombre)

print("Liste Nombres Pairs :", list(liste_nombre_pair))