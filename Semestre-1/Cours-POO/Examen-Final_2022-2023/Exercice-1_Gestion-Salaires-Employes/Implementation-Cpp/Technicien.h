#ifndef TECHNICIEN_H
#define TECHNICIEN_H

#include <iostream>
using namespace std;

#include "Employe.h"

class Technicien : public Employe {
private:
    int nbUniteProduite;
    static const double BASE;
    static const double PART;
    static const double GAIN_UNITE;

public:
    Technicien(string nom, int age, int anciennete, int nbUniteProduite);
    void afficher() override;
    double calculerBaseSalaire() override;
};

#endif