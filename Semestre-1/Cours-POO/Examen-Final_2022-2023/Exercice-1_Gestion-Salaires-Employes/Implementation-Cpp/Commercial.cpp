#include "Commercial.h"

const double Commercial::BASE = 2000.0;
const double Commercial::PART = 0.2;

Commercial::Commercial(string nom, int age, int anciennete, double chiffreAffaire) : Employe(nom, age, anciennete) {
    this->chiffreAffaire = chiffreAffaire;
}

void Commercial::afficher() {
    cout << "Commercial : " << nom;
}

double Commercial::calculerBaseSalaire() {
    return BASE + (chiffreAffaire * PART);
}
