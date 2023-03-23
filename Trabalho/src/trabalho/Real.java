package trabalho;
/*
 * Esse código define 
 * uma classe chamada "Real", 
 * que herda da classe abstrata "Moeda". 
 */
public class Real extends Moeda {
	
	public Real(double valor) {//Este é o construtor da classe "Real"
		this.valor = valor;
	}

	@Override
	public void infoMoeda() {//metodo informação da moeda
		System.out.println("R$"+valor + " Reais");
		
	}

	@Override
	public double converterMoeda() {//metodo converter moeda
    return this.valor;
		
	}
	
	@Override
	public boolean equals(Object objeto) {
		if(this.getClass() != objeto.getClass()) {
			return false;
		}
		//Cast de valor
		Real obejtoReal = (Real)objeto;
		if(this.valor != obejtoReal.valor) {
			return false;
		}
		return true;
	}
	

}