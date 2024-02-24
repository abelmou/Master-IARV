mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
jours = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]

liste_mois_jours = []
for i in range(12) :
    liste_mois_jours.append(mois[i])
    liste_mois_jours.append(jours[i])

print(liste_mois_jours)