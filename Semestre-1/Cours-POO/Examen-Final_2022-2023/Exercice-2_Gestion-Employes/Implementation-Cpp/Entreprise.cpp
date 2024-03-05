#include "Entreprise.h"
#include "Employe.h"

Entreprise::Entreprise() {}

void Entreprise::ajouterEmploye(Employe * employe) {
    employes.push_back(employe);
}

double Entreprise::getSalaireTotal() const {
    double salaireTotal = 0;
    for (const Employe * employe : employes) {
        salaireTotal += employe->calculerSalaire();
    }
    return salaireTotal;
}

string Entreprise::organigramme() const {
    string organigram = "Organigramme de l'entreprise:\n";
    for (const Employe * employe : employes) {
        organigram += employe->afficherSuperieur() + "\n";
        organigram += employe->afficherSubordonnes() + "\n";
    }
    return organigram;
}