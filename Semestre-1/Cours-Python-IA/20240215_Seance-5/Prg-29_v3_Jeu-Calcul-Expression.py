import random

def generer_expression():
    return [random.randint(1, 20), random.choice(['+', '-', '*']), random.randint(1, 20)]

def calculer_expression(expression):
    if(expression[1] == '+'):
        return expression[0] + expression[2]
    elif(expression[1] == '-'):
        return expression[0] - expression[2]
    elif(expression[1] == '*'):
        return expression[0] * expression[2]

expression = generer_expression()
reponse_correcte = calculer_expression(expression)
reponse_joueur = input("Guess " + str(expression[0]) + " " + expression[1] + " " + str(expression[2]) + " : ")

if(int(reponse_joueur) == reponse_correcte):
    print("Correct !")
else:
    print("Incorrect !\nThe correct answer is :", reponse_correcte)