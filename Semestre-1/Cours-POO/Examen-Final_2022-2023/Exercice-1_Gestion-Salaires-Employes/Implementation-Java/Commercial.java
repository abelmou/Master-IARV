class Commercial extends Employe {
    private double chiffreAffaire;
    private static final double BASE = 2000.0;
    private static final double PART = 0.2;

    public Commercial(String nom, int age, int anciennete, double chiffreAffaire) {
        super(nom, age, anciennete);
        this.chiffreAffaire = chiffreAffaire;
    }

    @Override
    public void afficher() {
        System.out.print("Commercial : " + nom);
    }

    @Override
    public double calculerBaseSalaire() {
        return BASE + (chiffreAffaire * PART);
    }
}
