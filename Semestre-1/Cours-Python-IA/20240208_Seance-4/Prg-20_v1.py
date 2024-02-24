import random

def melanger(mot):
    mot = list(mot)
    random.shuffle(mot) # Mélange les lettres du mot
    return ''.join(mot)

print("Program")
print(melanger("Program"))