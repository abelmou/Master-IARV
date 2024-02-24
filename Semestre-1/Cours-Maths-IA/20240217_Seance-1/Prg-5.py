import random

Urne = ["rouge", "jaune", "jaune", "vert", "vert", "vert", "vert"]

def proba(nombre):
    compteur_rouge = 0
    compteur_jaune = 0
    compteur_rouge_2 = 0
    compteur_autre_2 = 0
    score = 0

    for _ in range(nombre):
        t = random.choice(Urne)
        if(t == 'rouge'):
            compteur_rouge += 1
            score += 10
        elif(t == 'jaune'):
            compteur_jaune += 1
            score -= 5
        elif(t == 'vert'):
            t = random.choice(Urne)
            if(t == 'rouge'):
                compteur_rouge_2 += 1
                score += 8
            elif(t == 'jaune' or t == 'vert'):
                compteur_autre_2 += 1
                score -= 4

    return [(compteur_rouge / nombre), (compteur_jaune / nombre), (compteur_rouge_2 / nombre), (compteur_autre_2 / nombre), score]


nombre = int(input("Donnez un nombre de tentative : "))
p = proba(nombre)
print("Probabilités :")
print("P(X = 10) :", p[0])
print("P(X = -5) :", p[1])
print("P(X = 8) :", p[2])
print("P(X = -4) :", p[3])
print("Score :", p[4])