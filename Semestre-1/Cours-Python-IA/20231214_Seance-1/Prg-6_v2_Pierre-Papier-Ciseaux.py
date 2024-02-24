import random

choices = ["Pierre", "Papier", "Ciseaux"]

joueur = input("Action joueur : ")
machine = random.choice(choices)

print("Joueur :", joueur)
print("Machine :", machine)

if(joueur == machine) :
    print("Égalité !")
elif ((joueur == "Papier" and machine == "Pierre") or (joueur == "Pierre" and machine == "Ciseaux") or (joueur == "Ciseaux" and machine == "Papier")) :
    print("Joueur a gagné !")
else :
    print("Machine a gagné !")