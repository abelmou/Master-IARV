import random

def tester(nombre):
    return nombre * 2

liste1 = random.sample(range(1,10), 7)
liste2 = random.sample(range(1,10), 3)

print("Liste 1 :", liste1)
print("Liste 2 :", liste2)

print("\n[i for i in liste1] :", [i for i in liste1])
print("[i*2 for i in liste1 if i in liste2] :", [i*2 for i in liste1 if i in liste2])

print("\n[tester(i) for i in liste1 if i in liste2] :", [tester(i) for i in liste1 if i in liste2])
print("[tester(i) for i in set(liste1) if i in liste2] :", [tester(i) for i in set(liste1) if i in liste2])

liste3 = [2, 4, 4, 6]
liste4 = [4, 5, 2, 8]

print("\nListe 3 :", liste3)
print("Liste 4 :", liste4)

print("[i for i in liste3 if i in liste4] :", [i for i in liste3 if i in liste4])