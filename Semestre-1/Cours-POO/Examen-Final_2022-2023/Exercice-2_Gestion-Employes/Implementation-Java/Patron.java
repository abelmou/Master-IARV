import java.util.ArrayList;
import java.util.List;

public class Patron extends Employe {
    private double primeRisque;
    private List<Employe> subordonnes;

    public Patron(String numeroSecuriteSociale, String nom, double salaire, Employe superieur, double primeRisque) {
        super(numeroSecuriteSociale, nom, salaire, "Patron", superieur);
        this.primeRisque = primeRisque;
        this.subordonnes = new ArrayList<>();
    }

    public void ajouterSubordonne(Employe subordonne) {
        subordonnes.add(subordonne);
    }

    @Override
    public double calculerSalaire() {
        return salaire + primeRisque;
    }

    @Override
    public String afficherSubordonnes() {
        String sub = super.afficherSubordonnes() + "\n";
        for (Employe employe : subordonnes)
            sub += "\t\t" + employe.afficheEmploye() + "\n";
        return sub;
    }
}