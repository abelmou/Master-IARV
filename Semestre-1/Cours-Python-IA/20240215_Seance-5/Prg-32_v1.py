# doubler = lambda x : [x, x]
# liste = [11, 13, 15, 17, 19]
# liste_double = list(map(doubler, liste))
# print("Liste Doublé :", liste_double)

print("Liste Doublé :", list(map(lambda x : [x, x], [11, 13, 15, 17, 19])))