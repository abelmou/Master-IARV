import java.util.ArrayList;
import java.util.List;

public class Entreprise {
    private List<Employe> employes;

    public Entreprise() {
        this.employes = new ArrayList<>();
    }

    public void ajouterEmploye(Employe employe) {
        employes.add(employe);
    }

    public double getSalaireTotal() {
        double salaireTotal = 0;
        for (Employe employe : employes) {
            salaireTotal += employe.calculerSalaire();
        }
        return salaireTotal;
    }

    public String organigramme() {
        String organigram = "Organigramme de l'entreprise:\n";
        for (Employe employe : employes) {
            organigram += employe.afficherSuperieur() + "\n";
            organigram += employe.afficherSubordonnes() + "\n";
        }
        return organigram;
    }
}