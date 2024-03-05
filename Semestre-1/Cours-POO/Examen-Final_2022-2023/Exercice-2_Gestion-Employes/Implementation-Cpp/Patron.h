#ifndef PATRON_H
#define PATRON_H

#include <vector>

#include "Employe.h"

class Patron : public Employe {
private:
    double primeRisque;
    vector<Employe *> subordonnes;

public:
    Patron(string numeroSecuriteSociale, string nom, double salaire, Employe * superieur, double primeRisque);

    void ajouterSubordonne(Employe * subordonne);
    double calculerSalaire() const override;
    string afficherSubordonnes() const;
};

#endif