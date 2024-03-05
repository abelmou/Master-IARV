#ifndef COMMERCIAL_H
#define COMMERCIAL_H

#include <iostream>
using namespace std;

#include "Employe.h"

class Commercial : public Employe {
private:
    double chiffreAffaire;
    static const double BASE;
    static const double PART;

public:
    Commercial(string nom, int age, int anciennete, double chiffreAffaire);
    void afficher() override;
    double calculerBaseSalaire() override;
};

#endif