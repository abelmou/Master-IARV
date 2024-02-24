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

expressions = [generer_expression() for _ in range(5)]

liste_correctes = list(map(calculer_expression, expressions))

reponses_joueur = []
for i in range(5):
    reponses_joueur.append(int(input(f"{i+1} - Guess " + str(expressions[i][0]) + " " + expressions[i][1] + " " + str(expressions[i][2]) + " : ")))

print("\nEvaluation :\n------------")
score = 0
for i in range(5):
    if(reponses_joueur[i] == liste_correctes[i]):
        print(f"Expression {i+1} : Correct")
        score += 1
    else:
        print(f"Expression {i+1} : Incorrect ! The correct answer is : {liste_correctes[i]}")

print("\nScore : ", score)