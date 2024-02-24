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
print("Expression aléatoire :", expression[0], expression[1], expression[2], "=", calculer_expression(expression))