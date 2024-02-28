#ifndef MEDICAMENT_H
#define MEDICAMENT_H

#include <iostream>
using namespace std;

class Medicament {
private:
    string nomMed;
    double prix;
    int quantite;

public:
    Medicament(string nomMed, double prix, int quantite);

    string getNomMed() const;
    void setNomMed(string nomMed);
    
    double getPrix() const;
    void setPrix(double prix);

    int getQuantite() const;
    void setQuantite(int quantite);
    
    void affichageMed() const;
};

#endif