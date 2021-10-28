package abreu;
public class Gerente extends Funcionario{
    private int nFuncionarios; //Atributos-Variáveis de instância

    //construtores
    public Gerente(){ //default
        super();
    }
    public Gerente(int nFuncionarios, String nome, float salario){
        super(nome, salario);
        this.nFuncionarios = nFuncionarios;
    }
    //getters/setters

    //Reescrita do método aumentarSalario
    @Override
    public void aumentarSalario(float perc){
        super.aumentarSalario(perc + 20);
    }

    //Reescrita do método imprimir
    @Override
    public String imprimir(){
        return super.imprimir() + "Numero de funcionário que gerencia: " +nFuncionarios+ "\n";
    }
}
