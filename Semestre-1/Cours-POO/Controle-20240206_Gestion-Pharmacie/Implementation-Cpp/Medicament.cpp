#include "Medicament.h"

Medicament::Medicament(string nomMed, double prix, int quantite) {
    this->nomMed = nomMed;
    this->prix = prix;
    this->quantite = quantite;
}

string Medicament::getNomMed() const {
    return this->nomMed;
}

void Medicament::setNomMed(string nomMed) {
    this->nomMed = nomMed;
}

double Medicament::getPrix() const {
    return this->prix;
}

void Medicament::setPrix(double prix) {
    this->prix = prix;
}

int Medicament::getQuantite() const {
    return this->quantite;
}

void Medicament::setQuantite(int quantite) {
    this->quantite = quantite;
}

void Medicament::affichageMed() const {
    cout << "Medicament : " << this->nomMed << " - Prix : " << this->prix << " - Quantité : " << this->quantite << endl;
}