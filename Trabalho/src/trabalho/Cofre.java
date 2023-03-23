package trabalho;
import java.util.ArrayList;


public class Cofre {
	private ArrayList<Moeda> listaMoedas;
	public Cofre() {// construtor da lista de moedas iniciando vazia
		this.listaMoedas = new ArrayList<>();
		
	}
	
	public void inserirMoeda(Moeda moeda) {//Construtor: Inicializa um objeto com as propriedades passadas
		this.listaMoedas.add(moeda);
		
	}
	
	public boolean removerMoeda(Moeda moeda) {//Construtor: Inicializa um objeto com as propriedades passadas
		return this.listaMoedas.remove(moeda);
	}
	
	public void listarMoedas() {//Construtor: Inicializa um objeto com as propriedades passadas
		
		if(this.listaMoedas.isEmpty()) {
			System.out.println("A lista de Moedas está Vazia");
			return;
		}
		
		for(Moeda moeda : this.listaMoedas){// percorre toda a lista de moedas e retorna as informações
			moeda.infoMoeda();
			
		}
	}

	public double totalConvertido() {
		
		if(this.listaMoedas.isEmpty()) {
			System.out.println("A lista de Moedas está Vazia");
			return 0;
		}
		 double valorMoedaAcumulada = 0;
		 
		 for(Moeda moeda : this.listaMoedas){// percorre toda a lista de moedas e retorna as informações
				moeda.infoMoeda();
				valorMoedaAcumulada = valorMoedaAcumulada + moeda.converterMoeda();
			}
		// TODO Auto-generated method stub
		return valorMoedaAcumulada;
	}
	

}
