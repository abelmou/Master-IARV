#include <iostream>
using namespace std;

#include "Client.h"
#include "Medicament.h"
#include "Pharmacie.h"

int main(int argc, char * argv[]) {
    Client c1("Ahmed", 150);
    Client c2("Omar", 100);
    Client c3("Ali", 50);
    Medicament m1("Med1", 10, 10);
    Medicament m2("Med2", 20, 20);
    Medicament m3("Med3", 30, 30);
    Pharmacie ph;

    ph.enregCl(c1); ph.enregCl(c2); ph.enregCl(c3);
    ph.enregMed(m1); ph.enregMed(m2); ph.enregMed(m3);
    ph.affichage();

    ph.approvisionner("Med1", 60); cout << "Approvision Med1 60" << endl;
    ph.approvisionner("Med4", 5); cout << "Approvision Med4 5" << endl;
    ph.affichage();

    ph.achat("Med3", "Omar", 9, 0); cout << "Achat 9 Med3 par Omar" << endl;
    ph.affichage();

    return 0;
}