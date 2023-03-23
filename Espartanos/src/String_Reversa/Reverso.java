package String_Reversa;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

//import java.util.Scanner;
public class Reverso {

	public static void main(String[] args) {
		
		/*Scanner scanner = new Scanner(System.in);
		System.out.println("Digite uma palavra: ");
		String palavra = scanner.nextLine();
		StringBuffer invertido = new StringBuffer(palavra);
		invertido.reverse();
		System.out.println(invertido);*/
		
		//Criando um array(lista de nomes)importar o metodo array
		
		Scanner teclado = new Scanner(System.in);
		ArrayList <String> ListaNomes = new ArrayList<String>();
		System.out.println("Digite a quantidade de nomes: ");
		int qtd = teclado.nextInt();
		
		for(int i=0; i<=qtd; i++) {
			String nome = teclado.nextLine();
			ListaNomes.add(nome);
			//ListaNomes.add(teclado.nextLine()); outro jeito de fazer
		}// .get = usa com arraylist e [] com array
		/*for ( int i = ListaNomes.size() - 1; i >=0; i--) {
				System.out.println(ListaNomes.get(i));
				
				
			}*/ 
		System.out.println("Ordem Normal");
		System.out.println(ListaNomes);
		
		System.out.println("Ordem Inversa");
		
		Collections.reverse(ListaNomes);
		System.out.println(ListaNomes);
		
		
		

	}

}
