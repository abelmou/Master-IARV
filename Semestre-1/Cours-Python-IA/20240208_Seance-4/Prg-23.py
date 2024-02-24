dictionnaire = {} # Vide

dictionnaire["Mouse"] = "Souris"
dictionnaire["Keyboard"] = "Clavier"
dictionnaire["Screen"] = "Monitor"
print("Affichage dictionnaire :", dictionnaire, "\n")

del dictionnaire["Keyboard"]
print("Suppression keyboard :", dictionnaire, "\n")

if "Mouse" in dictionnaire :
    print("Mouse in dictionnaire ? Oui\n")
else :
    print("Mouse in dictionnaire ? Introuvable\n")

print("dictionnaire.keys() :", dictionnaire.keys(), "\n")
print("dictionnaire.values() :", dictionnaire.values(), "\n")

print("key in dictionnaire.keys() :")
for key in dictionnaire.keys() :
    print(key, '', end='')
print()