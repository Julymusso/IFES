#include <stdio.h>

void ler (unsigned char *vNomeAluno, int *iQtdNotas, double *vNotas){
    
    int i;

    printf("Insira o nome do Aluno: ");
    scanf("%[^\n]", vNomeAluno);
    printf("Insira a quantidade de provas realizadas: ");
    scanf("%d", iQtdNotas);
    for (i=0; i<*iQtdNotas; i++){
        printf("Insira a nota [%d]: ", i+1);
        scanf("%lf", &vNotas[i]);
    }
}

double calcMedia (double *vNotas, int iQtdNotas){
    int i;
    double somaNotas;

    somaNotas = 0;
    for (i=0; i<iQtdNotas; i++){
        somaNotas = somaNotas + vNotas[i];
    }
    return (somaNotas/iQtdNotas);
}

void escrever (unsigned char *vNomeAluno, double fMedia){
    printf ("A nota somaNotas de %s e %.2lf.", vNomeAluno, fMedia);
}