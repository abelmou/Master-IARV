titre_prenom = lambda personne : print('{} {}'.format(personne.split()[-3], personne.split()[-1]))

enseignants = ["Pr Bidaoui Jamal", "Pr Rbati Khadija", "Pr Souiri Hassan", "Pr Tazi Hanane"]

list(map(titre_prenom, enseignants))