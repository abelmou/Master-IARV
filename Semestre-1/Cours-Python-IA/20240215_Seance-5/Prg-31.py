import math

est_carre_parfait = lambda x : True if math.sqrt(x).is_integer() else False

liste = list(range(0, 500))

liste_carre_parfait = filter(est_carre_parfait, liste)

print("Liste Carrés Parfaits :", list(liste_carre_parfait))