#ifndef VENDEUR_H
#define VENDEUR_H

#include "Employe.h"

class Vendeur : public Employe {
private:
    double commission;

public:
    Vendeur(string numeroSecuriteSociale, string nom, double salaire, Employe * superieur, double commission);
    double calculerSalaire() const override;
    string afficherSubordonnes() const;
};

#endif