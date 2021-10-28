package abreu;

public class AppFuncionarioGerente {
    public static void main (String[] args) {
        Scanner entrada = new Scanner(System.in);
    
        Funcionario func = new Funcionario("Jose da Silva", 1000.0f);
        Gerente ger = new Gerente(45, "João Medeiros", 5000.0f);

        //calcular 10% de aumento de salário para os funcionarios
        func.aumentarSalario(10);
        ger.aumentarSalario(10);

        System.out.println("=====DADOS DO FUNCIONÁRIO=====");
        System.out.println(func.imprimir());
        System.out.println("=====DADOS DO GERENTE=====");
        System.out.println(ger.imprimir());
    }
}
