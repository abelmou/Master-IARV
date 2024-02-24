chaine = input("Saisir un chaine : ")
print("Chaine :", chaine)

chaine_renversee = chaine[::-1]
print("Chaine renversée :", chaine_renversee)

if (chaine == chaine_renversee) :
    print(chaine, "est un palindrome")
else :
    print(chaine, "n'est pas un palindrome")