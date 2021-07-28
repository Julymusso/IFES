#include <stdio.h>

void calcula (float l, float *area, float *perimetro){
    *area = l*l;
    *perimetro = 4*l;
}


int main (int argc, char **argv){
    
    float lado, area, perimetro;
    
    printf("Insira o valor do lado do quadrado (separando por \".\" nas casas decimais): \n");
    scanf("%f", &lado);

    calcula(lado, &area, &perimetro);

    printf("Lado: %.2f\nArea: %.2f\n Perimetro: %.2f", lado, area, perimetro);
    
    return 0;
}