#include "Patron.h"

Patron::Patron(string numeroSecuriteSociale, string nom, double salaire, Employe * superieur, double primeRisque) : Employe(numeroSecuriteSociale, nom, salaire, "Patron", superieur) {
    this->primeRisque = primeRisque;
}

void Patron::ajouterSubordonne(Employe * subordonne) {
    subordonnes.push_back(subordonne);
}

double Patron::calculerSalaire() const {
    return salaire + primeRisque;
}

string Patron::afficherSubordonnes() const {
    string sub = Employe::afficherSubordonnes() + "\n";
    for (const Employe * employe : subordonnes) {
        sub += "\t\t" + employe->afficheEmploye() + "\n";
    }
    return sub;
}