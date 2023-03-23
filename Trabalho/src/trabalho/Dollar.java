package trabalho;
/*
 * Esse código define 
 * uma classe chamada "Dolar", 
 * que herda da classe abstrata "Moeda". 
 */

public class Dollar extends Moeda {
	
	public Dollar(double valor) {//Este é o construtor da classe "Dollar"
		this.valor = valor;
	}

	@Override
	public void infoMoeda() {//metodo informação da moeda
		System.out.println("US$"+valor + " Dolares");
		
	}
	@Override
	public double converterMoeda() {//metodo converter moeda
		//  Auto-generated method stub
		return this.valor * 5.20;
	}
	@Override
	public boolean equals(Object objeto) {
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		//Cast de valor
		Dollar obejtoEuro = (Dollar)objeto;
		if(this.valor != obejtoEuro.valor) {
			return false;
		}
		return true;
	}

}
