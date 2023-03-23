package Empresa;
import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		Scanner in = new Scanner(System.in);
		double altura;
		int peso;
		double imc = 0;
		
		System.out.println("Digite seu peso e altura: ");
		peso = in.nextInt();
		altura = in.nextDouble();
		
		imc = peso / (altura * altura);
		
		System.out.printf("O seu IMC é de: %.2f", imc);
		
		
		

	}

}
