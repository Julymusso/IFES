#include <stdio.h>
#include "ex4lib.h"

int main (int argc, char **argv){
    int nTermos;
    float m1[3][3], maior;

    nTermos=Qtd_Termos;

    ler (m1[0], nTermos);
    maior = verificaMaior (m1[0], nTermos);
    escrever (m1[0], maior, nTermos);
   
    return 0;
}