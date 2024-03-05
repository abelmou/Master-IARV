import java.util.ArrayList;
import java.util.List;

class Entreprise {
    private String raisonSociale;
    private List<Employe> employes;

    public Entreprise(String raisonSociale) {
        this.raisonSociale = raisonSociale;
        this.employes = new ArrayList<>();
    }

    public void afficherEntreprise() {
        System.out.println("Entreprise : " + raisonSociale);
    }

    public void embaucher(Employe ... newEmpls) {
        for (Employe employe : newEmpls) {
            employes.add(employe);
        }
    }

    public void afficherSalaire() {
        System.out.println("Salaire des employés :");
        for (Employe employe : employes) {
            employe.afficher();
            System.out.println(" - Salaire : " + employe.calculerSalaire());
        }
    }

    public void afficherSalaireTotal() {
        double salaireTotal = 0.0;
        for (Employe employe : employes) {
            salaireTotal += employe.calculerSalaire();
        }
        System.out.println("Salaire total des employés : " + salaireTotal);
    }

    public double calculerSalaireMoyen() {
        if (employes.isEmpty()) {
            return 0.0;
        }

        double salaireTotal = 0.0;
        for (Employe employe : employes) {
            salaireTotal += employe.calculerSalaire();
        }
        return salaireTotal / employes.size();
    }
}
