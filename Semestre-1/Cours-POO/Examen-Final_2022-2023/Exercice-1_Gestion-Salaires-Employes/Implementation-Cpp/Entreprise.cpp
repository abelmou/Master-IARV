#include "Entreprise.h"

Entreprise::Entreprise(string raisonSociale) : raisonSociale(raisonSociale) {}

void Entreprise::afficherEntreprise() {
    cout << "Entreprise : " << raisonSociale << endl;
}

void Entreprise::afficherSalaire() {
    cout << "Salaire des employés :" << endl;
    for (Employe * employe : employes) {
        employe->afficher();
        cout << " - Salaire : " << employe->calculerSalaire() << endl;
    }
}

void Entreprise::afficherSalaireTotal() {
    double salaireTotal = 0.0;
    for (Employe * employe : employes) {
        salaireTotal += employe->calculerSalaire();
    }
    cout << "Salaire total des employés : " << salaireTotal << endl;
}

double Entreprise::calculerSalaireMoyen() {
    if (employes.empty()) {
        return 0.0;
    }

    double salaireTotal = 0.0;
    for (Employe * employe : employes) {
        salaireTotal += employe->calculerSalaire();
    }
    return salaireTotal / employes.size();
}
