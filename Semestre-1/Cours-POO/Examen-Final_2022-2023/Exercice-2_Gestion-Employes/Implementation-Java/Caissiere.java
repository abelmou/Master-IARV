public class Caissiere extends Employe {
    public Caissiere(String numeroSecuriteSociale, String nom, double salaire, Employe superieur) {
        super(numeroSecuriteSociale, nom, salaire, "Caissiere", superieur);
    }

    @Override
    public double calculerSalaire() {
        return salaire;
    }

    @Override
    public String afficherSubordonnes() {
        return super.afficherSubordonnes() + " Aucuns";
    }
}