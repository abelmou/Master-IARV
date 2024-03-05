public class TestEntreprise {
    public static void main(String[] args) {
        Entreprise entreprise = new Entreprise("Ma Société");
        entreprise.afficherEntreprise();

        Employe commercial1 = new Commercial("Ahmed", 35, 5, 5000.0);
        Employe commercial2 = new Commercial("Ali", 37, 7, 7000.0);
        Employe commercial3 = new Commercial("Khaled", 33, 3, 3000.0);

        Employe technicien1 = new Technicien("Aisha", 25, 5, 90);
        Employe technicien2 = new Technicien("Omar", 24, 4, 80);
        Employe technicien3 = new Technicien("Hassan", 23, 3, 70);
        Employe technicien4 = new Technicien("Fatima", 22, 2, 60);
        Employe technicien5 = new Technicien("Soufiane", 21, 1, 50);

        entreprise.embaucher(commercial1, commercial2, commercial3 , technicien1, technicien2, technicien3, technicien4, technicien5);

        entreprise.afficherSalaire();
        entreprise.afficherSalaireTotal();
        System.out.println("Salaire moyen : " + entreprise.calculerSalaireMoyen());
    }
}
