#include "Caissiere.h"

Caissiere::Caissiere(string numeroSecuriteSociale, string nom, double salaire, Employe * superieur) : Employe(numeroSecuriteSociale, nom, salaire, "Caissiere", superieur) {}

double Caissiere::calculerSalaire() const {
    return salaire;
}

string Caissiere::afficherSubordonnes() const {
    return Employe::afficherSubordonnes() + " Aucun";
}