dictionnaire = {}

def inverser(dictionnaire) :
    dictionnaire_inverse = {}
    for i in dictionnaire :
        dictionnaire_inverse[dictionnaire[i]] = i
    return dictionnaire_inverse

dictionnaire["Mouse"] = "Souris"
dictionnaire["Keyboard"] = "Clavier"
dictionnaire["Screen"] = "Monitor"

print("Dictionnaire :", dictionnaire)
dictionnaire_inverse = inverser(dictionnaire)
print("Dictionnaire inversé :", dictionnaire_inverse)