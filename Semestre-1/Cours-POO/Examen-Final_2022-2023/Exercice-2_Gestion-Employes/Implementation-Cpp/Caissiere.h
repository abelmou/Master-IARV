#ifndef CAISSIERE_H
#define CAISSIERE_H

#include "Employe.h"

class Caissiere : public Employe {
public:
    Caissiere(string numeroSecuriteSociale, string nom, double salaire, Employe * superieur);
    double calculerSalaire() const override;
    string afficherSubordonnes() const;
};

#endif