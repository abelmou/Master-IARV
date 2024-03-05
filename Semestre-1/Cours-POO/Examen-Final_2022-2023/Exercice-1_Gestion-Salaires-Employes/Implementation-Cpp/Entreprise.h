#ifndef ENTREPRISE_H
#define ENTREPRISE_H

#include <iostream>
using namespace std;
#include <vector>

#include "Employe.h"

class Entreprise {
private:
    string raisonSociale;
    vector<Employe *> employes;

public:
    Entreprise(string raisonSociale);
    void afficherEntreprise();
    template<typename... emps>
    void embaucher(emps*... newEmpls) {
        (employes.push_back(newEmpls), ...);
    }
    void afficherSalaire();
    void afficherSalaireTotal();
    double calculerSalaireMoyen();
};

#endif