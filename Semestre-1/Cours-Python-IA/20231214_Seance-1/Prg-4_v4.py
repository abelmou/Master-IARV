def inverser(chaine) :
    return ''.join(reversed(chaine))

chaine = input("Saisir un chaine : ")
print("Chaine :", chaine)

chaine_renversee = inverser(chaine)
print("Chaine renversée :", chaine_renversee)

if (chaine == chaine_renversee) :
    print(chaine, "est un palindrome")
else :
    print(chaine, "n'est pas un palindrome")