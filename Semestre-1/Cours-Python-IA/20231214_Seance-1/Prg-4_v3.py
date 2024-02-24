def inverser(chaine) :
    chaine_renversee = ""
    for i in range(len(chaine)) :
        chaine_renversee += chaine[len(chaine) - i - 1]
    return chaine_renversee

chaine = input("Saisir un chaine : ")
print("Chaine :", chaine)

chaine_renversee = inverser(chaine)
print("Chaine renversée :", chaine_renversee)

if (chaine == chaine_renversee) :
    print(chaine, "est un palindrome")
else :
    print(chaine, "n'est pas un palindrome")