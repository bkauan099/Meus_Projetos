import java.util.Scanner;

public class Contador {

    public static void main(String[] args) {  
        Scanner scan = new Scanner(System.in);

        System.out.println("Digite o primeiro número: ");
        int n1 = scan.nextInt();
    
        System.out.println("Digite o segundo número: ");
        int n2 = scan.nextInt();

        try {
            contar(n1, n2);
        } catch (ParametroInvalidoException exception) {
            System.out.println("O segundo parâmetro deve ser maior que o primeiro.");
        }
    }

    static void contar(int n1, int n2) throws ParametroInvalidoException {
        if (n1 > n2) {
            throw new ParametroInvalidoException();
        }

        for (int x = n1; x <= n2; x++) {
            System.out.println("Imprimindo o número " + x);
        }
    }
}
class ParametroInvalidoException extends Exception {
    public ParametroInvalidoException() {
        super("Parâmetro inválido.");
    }
}