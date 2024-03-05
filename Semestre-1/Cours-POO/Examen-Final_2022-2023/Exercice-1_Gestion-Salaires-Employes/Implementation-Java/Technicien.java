class Technicien extends Employe {
    private int nbUniteProduite;
    private static final double BASE = 1000.0;
    private static final double PART = 0.1;
    private static final double GAIN_UNITE = 10.0;

    public Technicien(String nom, int age, int anciennete, int nbUniteProduite) {
        super(nom, age, anciennete);
        this.nbUniteProduite = nbUniteProduite;
    }

    @Override
    public void afficher() {
        System.out.print("Technicien : " + nom);
    }

    @Override
    public double calculerBaseSalaire() {
        return BASE + (nbUniteProduite * PART * GAIN_UNITE);
    }
}
