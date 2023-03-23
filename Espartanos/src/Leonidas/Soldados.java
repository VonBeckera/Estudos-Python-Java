package Leonidas;

import java.util.Scanner;

public class Soldados {

	public static void main(String[] args) {
		int palpite = 0; 
		int ValorCorreto = 10000;
		
		Scanner teclado = new Scanner(System.in);
		System.out.println("Quanto soldados o eército de leonidas vai enfrentar?\n");
        System.out.println("Digite um Palpite ");
        palpite = teclado.nextInt();
        String msg;
        while (palpite != ValorCorreto) {
        	
        	//Operador ternário
        	msg = palpite > ValorCorreto?"Tento de novo, um pouco menos...":"Um pouco Mais...";
        	System.out.println(msg);
        	
        	/*if (palpite > ValorCorreto) {
        		System.out.println("Tento de novo, um pouco menos");
        	}
        		else {
        			System.out.println("Um pouco Mais");
        		}*/
        	
        	System.out.println("Digite outro palpite");
            palpite = teclado.nextInt();
        }
        System.out.println("Parabéns Você acertou");
	}

}
