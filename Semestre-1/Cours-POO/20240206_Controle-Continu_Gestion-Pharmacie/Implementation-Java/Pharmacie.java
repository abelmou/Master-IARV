import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Pharmacie {
    private List<Client> clients;
    private List<Medicament> medicaments;

    public Pharmacie() {
        clients = new ArrayList<>();
        medicaments = new ArrayList<>();
    }

    public void enregCl(Client client) {
        clients.add(client);
    }

    public void enregMed(Medicament medicament) {
        medicaments.add(medicament);
    }

    public void affichage() {
        System.out.println("=====================================================================");
        System.out.println("Clients :\n---------");
        for (Client client : clients) {
            client.affichageCl();
        }
        System.out.println("\nMedicaments :\n-------------");
        for (Medicament medicament : medicaments) {
            medicament.affichageMed();
        }
        System.out.println("=====================================================================");
    }

    public int verifMed(String nomM, int qte) {
        for (int i = 0; i < medicaments.size(); i++) {
            if (medicaments.get(i).getNomMed().equals(nomM)) {
                if (medicaments.get(i).getQuantite() >= qte) {
                    return i;
                } else {
                    System.out.println("Erreur : Quantite du medicament n'est pas assez !");
                    return -1;
                }
            }
        }
        return -1;
    }

    public int verifCl(String nomC) {
        for (int i = 0; i < clients.size(); i++) {
            if (clients.get(i).getNomCl().equals(nomC)) {
                return i;
            }
        }
        return -1;
    }

    Scanner scanner = new Scanner(System.in);
    public void approvisionner(String nomM, int qte) {
        int index = verifMed(nomM, 0);
        if (index != -1) {
            medicaments.get(index).setQuantite(medicaments.get(index).getQuantite() + qte);
        } else {
            System.out.print(nomM + " est un nouvel Medicament, prix : ");
            double prixNouv = scanner.nextDouble();
            Medicament nouvMed = new Medicament(nomM, prixNouv, qte);
            medicaments.add(nouvMed);
        }
    }

    public int[] verifAchat(String nomM, String nomC, int qte, double montant) {
        int[] resultat = new int[2];

        int indexMed = verifMed(nomM, qte);
        if (indexMed != -1) {
            resultat[0] = indexMed;
        } else {
            System.out.println("Erreur : Medicament non trouvé !");
            resultat[0] = -1;
            resultat[1] = -1;
            return resultat;
        }

        int indexCl = verifCl(nomC);
        if (indexCl != -1) {
            resultat[1] = indexCl;
        } else {
            System.out.println(nomC + " est un nouvel Client, montant : " + montant);
            Client nouvCl = new Client(nomC, montant);
            clients.add(nouvCl);
            resultat[1] = clients.size() - 1;
        }

        return resultat;
    }

    public void achat(String nomM, String nomC, int qte, double montant) {
        int[] verification = verifAchat(nomM, nomC, qte, montant);

        if (verification[0] != -1 && verification[1] != -1) {
            medicaments.get(verification[0]).setQuantite(medicaments.get(verification[0]).getQuantite() - qte);
            clients.get(verification[1]).setCredit(clients.get(verification[1]).getCredit() - medicaments.get(verification[0]).getPrix() * qte + montant);
            System.out.println("Achat réussi.");
        } else {
            System.out.println("Erreur : Achat échoué.");
        }
    }
}