abstract class Employe {
    protected String nom;
    protected int age;
    protected int anciennete;

    public Employe(String nom, int age, int anciennete) {
        this.nom = nom;
        this.age = age;
        this.anciennete = anciennete;
    }

    public abstract void afficher();

    public abstract double calculerBaseSalaire();

    public double calculerSalaire() {
        return calculerBaseSalaire() + (anciennete * 0.10 * calculerBaseSalaire());
    }
}
