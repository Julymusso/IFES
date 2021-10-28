package abreu;

public class Funcionario {
    //Atributos - Variáveis de Instância
    private String nome;
    private float salario;

    //Construtor
    public Funcionario() {}//default
    //sobrecarregado
    public Funcionario(String nome, float salario){
        this.nome = nome;
        this.salario = salario;
    }

    //getters/setters

    //Métodos da classe
    public void aumentarSalario(float perc){
        this.salario += this.salario * perc/100.0;
    }

    public String imprimir(){
        return "Funcionario:" + nome +
            "\nSalário: R$ " +String.format("%2f\n",salario);
    }
}
