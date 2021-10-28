package groner;

public class Aluno extends Pessoa {
    
    private String curso;
    private double[] notas;
    }
    
    public String getCurso(){
        this.curso = curso;
    }
    public void setCurso(String curso){
        return curso;
    }
    public double[] getNotas(){
        this.notas = notas;
    }
    public void setNotas(double[] notas){
        this.notas = notas;
    }

    public double calcularMedia(){
        return 0;
    }

    public boolean verificarAprovado(){
        return true;
    }
}
