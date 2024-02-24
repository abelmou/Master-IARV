f = open("monFichier.txt", "w")
f.write("Bonjour\n")
f.write("Python est mon langage")
f.close()

f = open("monFichier.txt", "r")
b = f.read()
print(b)