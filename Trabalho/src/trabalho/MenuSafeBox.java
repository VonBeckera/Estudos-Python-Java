package trabalho;

import java.text.DecimalFormat;
import java.util.Scanner;
//import trabalho.Cofre.SubMenu;

public class MenuSafeBox {
	
	protected int OpcaoDeMoeda;
	//protected String Opcao;
	protected String ValorEmTextoDamoeda;
	/*"private Scanner sc;" é uma declaração de variável que armazena uma instância
	 *da classe Scanner que só pode ser acessada dentro da classe em que foi declarada.
	 *Isso significa que outras classes não podem acessar diretamente a variável "sc",
	 *mas a classe em que foi declarada pode usá-la para ler entradas de dados.
	 */
	private Scanner sc;
	private Cofre cofre;
	
	//classe metodo contrutor da classe Menu
	public MenuSafeBox() {
		
		sc = new Scanner(System.in);
		cofre = new Cofre();
		
		//SubMenu chama;
	}
	//Criando Menu Principal
	public void MenuOpcoesCofre() {
		
	    while (true) {
	        System.out.println("-==- Seja bem vindo ao sistema SAFE BOX sua moeda em segurança-==-\n ----Escolha uma Opção----\n");
	        System.out.println("1 - Adicionar Moeda");
	        System.out.println("2 - Remover Moeda");
	        System.out.println("3 - Listar Todas as Moedas");
	        System.out.println("4 - Exibir Valor Total em Reais das moedas");
	        System.out.println("0 - Sair do Cofre");

	        String opcao = sc.next();

	        switch (opcao) {
	            case "1":
	            	subMenuAdcionarMoedas();
	                continue;

	            case "2":
	            	subMenuRemoverMoedas();// Adicione aqui a lógica para remover moedas
	                continue;

	            case "3":
	               cofre.listarMoedas();
	                continue;

	            case "4":
	            	double moedaTotalConvertido = cofre.totalConvertido();
	            	
	            	DecimalFormat formato = new DecimalFormat("0.00");
	            	String valorFormatado = formato.format(moedaTotalConvertido);
	            	//String valorTextualMoeda = String.valueOf(moedaTotalConvertido);
	            	//valorTextualMoeda = valorTextualMoeda.replace(".", ",");
	            	System.out.println("Valor total de moedas convertidas para Real R$" +valorFormatado);//);valorTextualMoeda);
	                // Adicione aqui a lógica para exibir o valor total em reais
	                continue;

	            case "0":
	                System.out.println("Obrigado por utilizar o COFRE!! Saindo do Programa...");
	                return;

	            default:
	                System.out.println("Opção digitada inválida");
	                break;
	        }
	    }
	}
  
      private void subMenuAdcionarMoedas() {
	  while(true) {
	    System.out.println("Escolha o tipo de Moeda e ser inserida: ");
		System.out.println("1 - Real ");
		System.out.println("2 - Dolar ");
		System.out.println("3 - Euro ");
		System.out.println("4 - Sair deste Menu ");
		
		int OpcaoDeMoeda = sc.nextInt();
		
		Moeda moeda = null;
		//contorle de opçao de moeda escolhida
		if(OpcaoDeMoeda == 1) {
			
			System.out.println("Agora diga o valor da moeda: ");
			String ValorEmTextoDamoeda = sc.next();
			
			ValorEmTextoDamoeda = ValorEmTextoDamoeda.replace("," , ".");//convertendo de "," para "." caso o usuario digite vírgula
			double valorMoeda = Double.valueOf(ValorEmTextoDamoeda);
			
			moeda = new Real(valorMoeda);
			cofre.inserirMoeda(moeda);
			System.out.println("Moeda Inserida com sucesso");
		}
		else if(OpcaoDeMoeda == 2) {
		
			System.out.println("Agora diga o valor da moeda: ");
			ValorEmTextoDamoeda = sc.next();
			
			ValorEmTextoDamoeda = ValorEmTextoDamoeda.replace("," , ".");//convertendo de "," para "." caso o usuario digite vírgula
			double valorMoeda = Double.valueOf(ValorEmTextoDamoeda);
			
		    moeda = new Dollar(valorMoeda);
			cofre.inserirMoeda(moeda);
			System.out.println("Moeda Inserida com sucesso");
		}
		else if(OpcaoDeMoeda == 3) {
			
			System.out.println("Agora diga o valor da moeda: ");
			ValorEmTextoDamoeda = sc.next();
			
			ValorEmTextoDamoeda = ValorEmTextoDamoeda.replace("," , ".");//convertendo de "," para "." caso o usuario digite vírgula
			double valorMoeda = Double.valueOf(ValorEmTextoDamoeda);
			
			moeda = new Euro(valorMoeda);
			cofre.inserirMoeda(moeda);
			System.out.println("Moeda Inserida com sucesso");
		}
		else if (OpcaoDeMoeda == 4) {
			System.out.println("Saindo do Menu...");
			break;
		}
		else  {
			System.out.println("Opção inválida! Selecione novamente");
			continue;
		  } 
	  }
   }
      
      private void subMenuRemoverMoedas() {
    	  while(true) {
    	    System.out.println("Escolha o tipo de Moeda e ser Removida do Cofre: ");
    		System.out.println("1 - Real ");
    		System.out.println("2 - Dolar ");
    		System.out.println("3 - Euro ");
    		System.out.println("4 - Sair deste Menu ");
    		
    		int OpcaoDeMoeda = sc.nextInt();
    		
    		Moeda moeda = null;
    		//contorle de opçao de moeda escolhida
    		if(OpcaoDeMoeda == 1) {
    			
    			System.out.println("Agora diga o valor da moeda: ");
    			String ValorEmTextoDamoeda = sc.next();
    			
    			ValorEmTextoDamoeda = ValorEmTextoDamoeda.replace("," , ".");//convertendo de "," para "." caso o usuario digite vírgula
    			double valorMoeda = Double.valueOf(ValorEmTextoDamoeda);
    			
    			moeda = new Real(valorMoeda);
    			
    			if(cofre.removerMoeda(moeda)) {
    				System.out.println("Moeda Removida com sucesso");
        		}
    			else {
        			System.out.println("Moeda Não econtrada");
    			}
    		}
    		    else if(OpcaoDeMoeda == 2) {
    		
    			System.out.println("Agora diga o valor da moeda: ");
    			ValorEmTextoDamoeda = sc.next();
    			
    			ValorEmTextoDamoeda = ValorEmTextoDamoeda.replace("," , ".");//convertendo de "," para "." caso o usuario digite vírgula
    			double valorMoeda = Double.valueOf(ValorEmTextoDamoeda);
    			
    		    moeda = new Dollar(valorMoeda);
    			if(cofre.removerMoeda(moeda)) {
    				System.out.println("Moeda Removida com sucesso");
        		}
    			else {
        			System.out.println("Moeda Não econtrada");
        		}
    		}
    		    else if(OpcaoDeMoeda == 3) {
    			
    			System.out.println("Agora diga o valor da moeda: ");
    			ValorEmTextoDamoeda = sc.next();
    			
    			ValorEmTextoDamoeda = ValorEmTextoDamoeda.replace("," , ".");//convertendo de "," para "." caso o usuario digite vírgula
    			double valorMoeda = Double.valueOf(ValorEmTextoDamoeda);
    			
    			moeda = new Euro(valorMoeda);
    			
    			if(cofre.removerMoeda(moeda)) {
    				System.out.println("Moeda Removida com sucesso");
        		}
    			else {
        			System.out.println("Moeda Não econtrada");
        		}
        	}
    			
    		    else if (OpcaoDeMoeda == 4) {
    			System.out.println("Saindo do Menu...");
    			break;
    		}
    		    else  {
    			System.out.println("Opção inválida! Selecione novamente");
    			continue;
    		  } 
    	  }
       }   
	 
	  
	  
  }
 

