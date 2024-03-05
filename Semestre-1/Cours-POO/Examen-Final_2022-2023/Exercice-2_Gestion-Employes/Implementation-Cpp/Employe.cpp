#include "Employe.h"

Employe::Employe(string numeroSecuriteSociale, string nom, double salaire, string emploi, Employe * superieur) {
    this->numeroSecuriteSociale = numeroSecuriteSociale;
    this->nom = nom;
    this->salaire = salaire;
    this->emploi = emploi;
    this->superieur = superieur;
}

string Employe::afficherSuperieur() const {
    return "Supérieur hiérarchique de " + nom + " : " + (superieur != nullptr ? superieur->nom : "Aucun");
}

string Employe::afficherSubordonnes() const {
    return "\tSubordonnées :";
}

string Employe::afficheEmploye() const {
    return emploi + " : " + nom;
}