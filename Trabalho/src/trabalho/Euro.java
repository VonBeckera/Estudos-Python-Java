package trabalho;
/*
 * Esse código define 
 * uma classe chamada "Euro", 
 * que herda da classe abstrata "Moeda". 
 */
public class Euro extends Moeda {
	
	public Euro(double valor) {//Este é o construtor da classe "Euro"
		this.valor = valor;
	}


	@Override
	public void infoMoeda() {//metodo informação da moeda
		System.out.println("€"+valor + " Euros");
		
	}

	@Override
	public double converterMoeda() {//metodo converter moeda
		return this.valor * 5.52;
	}
	
	@Override
	public boolean equals(Object objeto) {
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		//Cast de valor
		Euro obejtoEuro = (Euro)objeto;
		if(this.valor != obejtoEuro.valor) {
			return false;
		}
		return true;
	}
	

}
