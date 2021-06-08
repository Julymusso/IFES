#include <stdio.h>
#include "ex3lib.h"

int main(int agrc, char **argv){
    
    int vetor[10], n;
    n=Qtd_Termos;

    ler (vetor, n);
    troca (vetor, n);
    mostrar (vetor, n);

    return 0;
}