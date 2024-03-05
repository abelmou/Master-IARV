public class Main {
    public static void main(String[] args) {
        Client c1 = new Client("Ahmed", 150);
        Client c2 = new Client("Omar", 100);
        Client c3 = new Client("Ali", 50);
        Medicament m1 = new Medicament("Med1", 10, 10);
        Medicament m2 = new Medicament("Med2", 20, 20);
        Medicament m3 = new Medicament("Med3", 30, 30);
        Pharmacie ph = new Pharmacie();

        ph.enregCl(c1); ph.enregCl(c2); ph.enregCl(c3);
        ph.enregMed(m1); ph.enregMed(m2); ph.enregMed(m3);
        ph.affichage();

        ph.approvisionner("Med1", 60); System.out.println("Approvision Med1 60 pieces");
        ph.approvisionner("Med4", 5); System.out.println("Approvision Med4 5 pieces");
        ph.affichage();

        ph.achat("Med3", "Omar", 9, 0); System.out.println("Achat 9 pieces Med3 par Omar");
        ph.affichage();
    }
}
