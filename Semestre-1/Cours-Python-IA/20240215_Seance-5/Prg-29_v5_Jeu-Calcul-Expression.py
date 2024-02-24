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

def evaluer(expression, reponse):
    if(reponse == calculer_expression(expression)):
        return "Correct !"
    else:
        return f"Incorrect ! The correct answer is : {calculer_expression(expression)}"

expression = []
for i in range(5):
    expression.append(generer_expression())

reponses_joueur = []
for i in range(5):
    reponses_joueur.append(int(input(f"{i+1} - Guess " + str(expression[i][0]) + " " + expression[i][1] + " " + str(expression[i][2]) + " : ")))

evaluation = list(map(evaluer, expression, reponses_joueur))
                       
print("\nEvaluation :\n------------")
for i in range(5):
    print(f"Expression {i+1} :", evaluation[i])