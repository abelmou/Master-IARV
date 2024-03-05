#include "Vendeur.h"

Vendeur::Vendeur(string numeroSecuriteSociale, string nom, double salaire, Employe * superieur, double commission) : Employe(numeroSecuriteSociale, nom, salaire, "Vendeur", superieur) {
    this->commission = commission;
}

double Vendeur::calculerSalaire() const {
    return salaire + commission;
}

string Vendeur::afficherSubordonnes() const {
    return Employe::afficherSubordonnes() + " Aucun";
}