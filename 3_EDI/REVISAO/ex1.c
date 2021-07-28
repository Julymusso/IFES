#include <stdio.h>
int main (int argc, char **argv){
    
    int nProvas, i;
    char nome[20];
    float nota, media;

    printf("Insira o nome do Aluno:");
    scanf("%s",nome);
    printf("Insira a quantidade de provas realizadas:");
    scanf("%d",&nProvas);
    for (i=0; i<nProvas; i++){
        printf("Insira a nota:");
        scanf("%f",&nota);
        media = media + nota;
    }
    media = media/nProvas;
    printf ("O(a) aluno(a) %s obteve %.2f de media.",nome,media);
    return 0;
}