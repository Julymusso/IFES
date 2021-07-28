#include <stdio.h>
#include "ex1lib.h"

void ler(float *l){
    
    printf("Digite o valor do lado do quadrado para obter sua area e perimetro: ");
    scanf("%f", l);
}

void calcula(float l, float *area, float *perimetro){
    *area = l*l;
    *perimetro = 4*l;
}

void escrever(float l, float area, float perimetro){
    printf ("Para o quadrado de lado %.2f: \nArea: %.2f \nPerimetro: %.2f\n", l, area, perimetro);
}