class Point(object):
    "Point géometrique"

P1 = Point()
print(P1)
print(P1.__doc__)

P1.x = 5.0
P1.y = 7.0
print("(", P1.x, ",", P1.y, ")")
print("(", P1.x ** 2, ",", P1.y ** 2, ")")

def affiche_point(p) :
    return "Coordonnées horisontale : " + str(p.x) + " | Coordonnées verticale : " + str(p.y)

print(affiche_point(P1))

class Rectangle(object):
    "classe rectangle defini par un largeur et un longueur est un coin"
    coin = Point()

rectangle1 = Rectangle()
rectangle1.largeur = 5
rectangle1.longueur = 4
rectangle1.coin.x = 3
rectangle1.coin.y = 5

def affiche_rectangle(p) :
    print("Largeur :", p.largeur, "--- Longueur :", p.longueur, "--- Coin : (", affiche_point(rectangle1.coin), ")")

affiche_rectangle(rectangle1)