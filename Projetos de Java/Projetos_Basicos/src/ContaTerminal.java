import java.util.Scanner;

public class ContaTerminal {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
    
        System.out.println("Digite o numero da conta: ");
        int numero = scan.nextInt();

        System.out.println("Digite o numero da agencia: ");
        String agencia = scan.next();

        System.out.println("Digite o nome do cliente: ");
        String nomeCliente = scan.next();

        System.out.println("Digite o seu saldo: ");
        double saldo = scan.nextDouble();

        System.out.println("Olá " + nomeCliente + ", obrigado por criar uma conta em nosso banco, sua agência é " + agencia + ", conta " + numero + " e seu saldo " + saldo + " já está disponivel para saque.");
        

    }
}
