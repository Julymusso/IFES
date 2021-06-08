#include <stdio.h>
#include "ex5lib.h"

int main (int argc, char **argv){
    
    int matriz[4][2], l, c;
    l=4;
    c=2;

    ler(matriz[0], l, c);
    troca(matriz[0], l, c);
    escrever(matriz[0], l, c);

    return 0;
}
        