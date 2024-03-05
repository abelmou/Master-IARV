#include "Technicien.h"

const double Technicien::BASE = 1000.0;
const double Technicien::PART = 0.1;
const double Technicien::GAIN_UNITE = 10.0;

Technicien::Technicien(string nom, int age, int anciennete, int nbUniteProduite) : Employe(nom, age, anciennete) {
    this->nbUniteProduite = nbUniteProduite;
}

void Technicien::afficher() {
    cout << "Technicien : " << nom;
}

double Technicien::calculerBaseSalaire() {
    return BASE + (nbUniteProduite * PART * GAIN_UNITE);
}