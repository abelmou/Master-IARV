#ifndef CLIENT_H
#define CLIENT_H

#include <iostream>
using namespace std;

class Client {
private:
    string nomCl;
    double credit;

public:
    Client(string nomCl, double credit);

    string getNomCl() const;
    void setNomCl(string nomCl);
    
    double getCredit() const;
    void setCredit(double credit);
    
    void affichageCl() const;
};

#endif