mois = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet", "Aout", "Septembre", "Octobre", "Novembre", "Decembre"]
jours = [31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]

# mois[1:1] = jours[0:1]
# mois[3:3] = jours[1:2]
# mois[5:5] = jours[2:3]
# mois[7:7] = jours[3:4]
# mois[9:9] = jours[4:5]
# mois[11:11] = jours[5:6]
# mois[13:13] = jours[6:7]
# mois[15:15] = jours[7:8]
# mois[17:17] = jours[8:9]
# mois[19:19] = jours[9:10]
# mois[21:21] = jours[10:11]
# mois[23:23] = jours[11:12]

i,j = 1,0

while(i <= len(mois)) :
    mois[i:i] = jours[j:j+1]
    i,j = i+2,j+1

print(mois)