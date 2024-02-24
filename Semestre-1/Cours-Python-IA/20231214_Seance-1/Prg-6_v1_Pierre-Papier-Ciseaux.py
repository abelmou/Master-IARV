print("Pierre - Papier - Ciseaux")

joueur1 = input("Action joueur 1 : ")
joueur2 = input("Action joueur 2 : ")

if(joueur1 == joueur2) :
    print("Égalité !")
elif ((joueur1 == "Papier" and joueur2 == "Pierre") or (joueur1 == "Pierre" and joueur2 == "Ciseaux") or (joueur1 == "Ciseaux" and joueur2 == "Papier")) :
    print("Joueur 1 a gagné !")
else :
    print("Joueur 2 a gagné !")