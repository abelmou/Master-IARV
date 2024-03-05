#ifndef ENTREPRISE_H
#define ENTREPRISE_H

#include <iostream>
using namespace std;
#include <vector>

#include "Employe.h"

class Entreprise {
private:
    vector<Employe *> employes;

public:
    Entreprise();

    void ajouterEmploye(Employe * employe);
    double getSalaireTotal() const;
    string organigramme() const;
};

#endif