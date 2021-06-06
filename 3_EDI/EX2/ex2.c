/*Sabendo que os números perfeitos conhecidos são definidos pela fórmula 2^(n-1)*(2^(n-1)), sendo n um número primero
e que os 4 primeiros números perfeitos veem da fórmula cujo n representa os 4 primeiros primos temos:*/ 
#include <stdio.h>
#include "ex2lib.h"

int main (int argc, char **argv){

    long int vNumPrimos[4], vNumPerfeitos[4];
    int numTermos;
    numTermos=Qtd_Termo;
    
    calculaPrimos (vNumPrimos, numTermos);
    calculaPerfeitos (vNumPrimos, vNumPerfeitos, numTermos);
    escrever (vNumPerfeitos, numTermos);
   
    return 0;
}
