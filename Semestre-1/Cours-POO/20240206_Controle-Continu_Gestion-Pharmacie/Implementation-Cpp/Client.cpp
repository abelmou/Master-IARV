#include "Client.h"

Client::Client(string nomCl, double credit) {
    this->nomCl = nomCl;
    this->credit = credit;
}

string Client::getNomCl() const {
    return this->nomCl;
}

void Client::setNomCl(string nomCl) {
    this->nomCl = nomCl;
}

double Client::getCredit() const {
    return this->credit;
}

void Client::setCredit(double credit) {
    this->credit = credit;
}

void Client::affichageCl() const {
    cout << "Client : " << this->nomCl << " - Crédit : " << this->credit << endl;
}