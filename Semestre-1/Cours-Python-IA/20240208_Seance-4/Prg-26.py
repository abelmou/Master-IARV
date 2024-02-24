questions = [
    {"Question":"Calculez 12 * 12 + 6", "Reponse": '150'},
    {"Question":"Calculez 56 - 11 * 4", "Reponse": '12'},
    {"Question":"Calculez 70 * 5 + 105", "Reponse": '455'},
    {"Question":"Calculez 80 * 12 + 19", "Reponse": '979'},
    {"Question":"Calculez 20 * 10 + 20", "Reponse": '220'}
]

score = 0
for question in questions:
    reponse = input(question["Question"] + " : ")
    if(reponse == question["Reponse"]) :
        print("Correct !")
        score += 1
    else :
        print("Incorrect !")

print("\nScore :", score)