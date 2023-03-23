package trabalho;
/*
*
* "public abstract class Moeda" é uma declaração de classe que define uma classe 
*  abstrata pública chamada "Moeda" que pode ser estendida por outras classes para
*  implementar a funcionalidade específica da moeda.
*/

public abstract class Moeda {
	
	/* "protected double moeda" é uma declaração de variável que armazena um 
	    valor numérico de ponto flutuante de precisão dupla (por exemplo, um valor 
	    monetário) que só pode ser acessado por outras classes que estendam 
	    a classe atual ou dentro da própria classe.
	*/
	protected double valor;
	/*"public abstract void nome();" é uma declaração de um método abstrato público 
	 * que não retorna nenhum valor e não tem implementação na classe atual. Qualquer classe que estenda essa classe deve
	 * implementar o método "info()" para fornecer sua própria implementação.
	 */
	public abstract void infoMoeda();
	
	public abstract double converterMoeda();


}
