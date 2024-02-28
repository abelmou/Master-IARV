public class Medicament {
    private String nomMed;
    private double prix;
    private int quantite;

    public Medicament(String nomMed, double prix, int quantite) {
        this.nomMed = nomMed;
        this.prix = prix;
        this.quantite = quantite;
    }

    public String getNomMed() {
        return this.nomMed;
    }

    public void setNomMed(String nomMed) {
        this.nomMed = nomMed;
    }

    public double getPrix() {
        return this.prix;
    }

    public void setPrix(double prix) {
        this.prix = prix;
    }

    public int getQuantite() {
        return this.quantite;
    }

    public void setQuantite(int quantite) {
        this.quantite = quantite;
    }

    public void affichageMed() {
        System.out.println("Medicament : " + this.nomMed + " - Prix : " + this.prix + " - Quantité : " + this.quantite);
    }
}