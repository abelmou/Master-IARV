import random

def generer_expression():
    return [str(random.randint(1, 20)), random.choice(['+', '-', '*']), str(random.randint(1, 20))]

expression = ' '.join(generer_expression())
print("Expression aléatoire :", expression)