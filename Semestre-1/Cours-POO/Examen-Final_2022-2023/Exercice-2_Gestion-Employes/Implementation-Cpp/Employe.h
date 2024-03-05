#ifndef EMPLOYE_H
#define EMPLOYE_H

#include <iostream>
using namespace std;

class Employe {
protected:
    string numeroSecuriteSociale;
    string nom;
    double salaire;
    string emploi;
    Employe * superieur;

public:
    Employe(string numeroSecuriteSociale, string nom, double salaire, string emploi, Employe * superieur);

    virtual double calculerSalaire() const = 0;

    string afficherSuperieur() const;
    virtual string afficherSubordonnes() const;
    string afficheEmploye() const;
};

#endif