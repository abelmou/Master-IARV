public abstract class Employe {
    protected String numeroSecuriteSociale;
    protected String nom;
    protected double salaire;
    protected String emploi;
    protected Employe superieur;

    public Employe(String numeroSecuriteSociale, String nom, double salaire, String emploi, Employe superieur) {
        this.numeroSecuriteSociale = numeroSecuriteSociale;
        this.nom = nom;
        this.salaire = salaire;
        this.emploi = emploi;
        this.superieur = superieur;
    }

    abstract public double calculerSalaire();

    public String afficherSuperieur() {
        return "Supérieur hiérarchique de " + nom + " : " + (superieur != null ? superieur.nom : "Aucun");
    }

    public String afficherSubordonnes() {
        return "\tSubordonnées :";
    }

    public String afficheEmploye() {
        return this.emploi + " : " + this.nom;
    }
}