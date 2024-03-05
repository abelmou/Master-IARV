#include "Pharmacie.h"

void Pharmacie::enregCl(Client * client) {
    clients.push_back(client);
}

void Pharmacie::enregMed(Medicament * medicament) {
    medicaments.push_back(medicament);
}

void Pharmacie::affichage() const {
    cout << "=====================================================================" << endl;
    cout << "Clients :" << endl << "---------" << endl;
    for (int i = 0; i < clients.size(); i++)
        clients[i]->affichageCl();
    cout << endl << "Medicaments :" << endl << "-------------" << endl;
    for (int i = 0; i < medicaments.size(); i++)
        medicaments[i]->affichageMed();
    cout << "=====================================================================" << endl;
}

int Pharmacie::verifMed(string nomM, int qte) const {
    if (medicaments.size() != 0) {
        for(int i = 0; i < medicaments.size(); i++) {
            if (medicaments[i]->getNomMed() == nomM) {
                if (medicaments[i]->getQuantite() >= qte) {
                    return i;
                } else {
                    cout << "Erreur : La quantité du médicament '" << nomM << "' n'est pas suffisante !" << endl;
                    return -1;
                }
            }
        }
    }
    return -1;
}

int Pharmacie::verifCl(string nomC) const {
    if (clients.size() != 0) {
        for(int i = 0; i < clients.size(); i++) {
            if(clients[i]->getNomCl() == nomC)
                return i;
        }
    }
    return -1;
}

void Pharmacie::approvisionner(string nomM, int qte) {
    int index = verifMed(nomM, 0);
    if (index != -1) {
        medicaments[index]->setQuantite(medicaments[index]->getQuantite() + qte);
    } else {
        int prixNouv;
        cout << nomM << " est un nouvel Medicament, prix : ";
        cin >> prixNouv;
        Medicament * nouvMed = new Medicament(nomM, prixNouv, qte);
        medicaments.push_back(nouvMed);
    }
}

int * Pharmacie::verifAchat(string nomM, string nomC, int qte, double montant) {
    int * resultat = (int *)malloc(sizeof(int) * 2);

    int indexMed = verifMed(nomM, qte);
    if (indexMed != -1) {
        resultat[0] = indexMed;
    } else {
        cout << "Erreur : Medicament non trouvé !" << endl;
        resultat[0] = -1; resultat[1] = -1;
        return resultat;
    }

    int indexCl = verifCl(nomC);
    if (indexCl != -1) {
        resultat[1] = indexCl;
    } else {
        double montantNouv;
        cout << nomC << " est un nouvel Client, montant : " << montant << endl;
        Client * nouvCl = new Client(nomC, montant);
        clients.push_back(nouvCl);
        resultat[1] = clients.size() - 1;
    }

    return resultat;
}

void Pharmacie::achat(string nomM, string nomC, int qte, double montant) {
    int * verification = verifAchat(nomM, nomC, qte, montant);

    if(verification[0] != -1 && verification[1] != -1) {
        medicaments[verification[0]]->setQuantite(medicaments[verification[0]]->getQuantite() - qte);
        clients[verification[1]]->setCredit(clients[verification[1]]->getCredit() - medicaments[verification[0]]->getPrix() * qte + montant);
        cout << "Achat réussi." << endl;
    } else {
        cout << "Erreur : Achat échoué." << endl;
    }
}