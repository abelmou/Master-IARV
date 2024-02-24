def premier_dernier(liste):
    # return [liste[0], liste[len(liste) - 1]]
    # return [liste[- len(liste)], liste[-1]]
    return [liste[0], liste[-1]]

liste = [0, 1, 2, 3, 4, 5, 6]
print("Liste :", liste)
print("premier_dernier(liste) :", premier_dernier(liste))