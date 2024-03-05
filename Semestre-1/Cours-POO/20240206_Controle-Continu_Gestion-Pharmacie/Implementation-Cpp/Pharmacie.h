#ifndef PHARMACIE_H
#define PHARMACIE_H

#include <iostream>
using namespace std;
#include <vector>
#include "Client.h"
#include "Medicament.h"

class Pharmacie {
private:
    vector<Client *> clients;
    vector<Medicament *> medicaments;

public:
    void enregCl(Client * client);
    void enregMed(Medicament * medicament);

    void affichage() const;

    int verifMed(string nomM, int qte) const;
    int verifCl(string nomC) const;
    void approvisionner(string nomM, int qte);

    int * verifAchat(string nomM, string nomC, int qte, double montant);
    void achat(string nomM, string nomC, int qte, double montant);
};

#endif