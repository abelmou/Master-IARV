public class Client {
    private String nomCl;
    private double credit;

    public Client(String nomCl, double credit) {
        this.nomCl = nomCl;
        this.credit = credit;
    }

    public String getNomCl() {
        return this.nomCl;
    }

    public void setNomCl(String nomCl) {
        this.nomCl = nomCl;
    }

    public double getCredit() {
        return this.credit;
    }

    public void setCredit(double credit) {
        this.credit = credit;
    }

    public void affichageCl() {
        System.out.println("Client : " + this.nomCl + " - Crédit : " + this.credit);
    }
}