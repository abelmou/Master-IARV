class Vendeur extends Employe {
    private double commission;

    public Vendeur(String numeroSecuriteSociale, String nom, double salaire, Employe superieur, double commission) {
        super(numeroSecuriteSociale, nom, salaire, "Vendeur", superieur);
        this.commission = commission;
    }

    @Override
    public double calculerSalaire() {
        return salaire + commission;
    }

    @Override
    public String afficherSubordonnes() {
        return super.afficherSubordonnes() + " Aucuns";
    }
}
