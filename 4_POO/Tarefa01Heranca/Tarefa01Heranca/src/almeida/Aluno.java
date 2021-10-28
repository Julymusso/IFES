package almeida;

public class Aluno extends Pessoa {
    int matricula;

    Aluno (String nome, int idade, int matricula){
        super(nome, idade);
        this.matricula = matricula;
    }

    String dizerMatricula(){
        return "Minha matrícula é" + this.matricula;
    }

    String dizerNome(){
        return super.dizerNome() + this.dizerMatricula();
    }
}
