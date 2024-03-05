#include <iostream>
using namespace std;

#include "Entreprise.h"
#include "Patron.h"
#include "Vendeur.h"
#include "Caissiere.h"

int main() {
    Entreprise entreprise;

    Patron * patron1 = new Patron("123", "Ahmed", 5000, nullptr, 100);
    Patron * patron2 = new Patron("234", "Ali", 3000, nullptr, 50);
    Vendeur * vendeur1 = new Vendeur("345", "Khaled", 2000, patron1, 0.1);
    Vendeur * vendeur2 = new Vendeur("456", "Omar", 3000, patron1, 0.2);
    Vendeur * vendeur3 = new Vendeur("456", "Hassan", 1500, patron2, 0.1);
    Caissiere * caissiere1 = new Caissiere("567", "Aisha", 3000, patron1);
    Caissiere * caissiere2 = new Caissiere("678", "Fatima", 3000, patron2);

    patron1->ajouterSubordonne(vendeur1); patron1->ajouterSubordonne(vendeur2); patron1->ajouterSubordonne(caissiere1);
    patron2->ajouterSubordonne(vendeur3); patron2->ajouterSubordonne(caissiere2);

    entreprise.ajouterEmploye(patron1); entreprise.ajouterEmploye(patron2);
    entreprise.ajouterEmploye(vendeur1); entreprise.ajouterEmploye(vendeur2); entreprise.ajouterEmploye(vendeur3);
    entreprise.ajouterEmploye(caissiere1); entreprise.ajouterEmploye(caissiere2);

    cout << "Salaire total de l'entreprise : " << entreprise.getSalaireTotal() << endl;
    cout << entreprise.organigramme() << endl;

    return 0;
}