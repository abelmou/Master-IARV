#include "Employe.h"

Employe::Employe(string nom, int age, int anciennete) {
    this->nom = nom;
    this->age = age;
    this->anciennete = anciennete; 
}

double Employe::calculerSalaire() {
    return calculerBaseSalaire() + (anciennete * 0.10 * calculerBaseSalaire());
}