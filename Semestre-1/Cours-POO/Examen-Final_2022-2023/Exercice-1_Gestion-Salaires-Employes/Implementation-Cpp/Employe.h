#ifndef EMPLOYE_H
#define EMPLOYE_H

#include <iostream>
using namespace std;

class Employe {
protected:
    string nom;
    int age;
    int anciennete;

public:
    Employe(string nom, int age, int anciennete);
    virtual void afficher() = 0;
    virtual double calculerBaseSalaire() = 0;
    double calculerSalaire();
};

#endif
