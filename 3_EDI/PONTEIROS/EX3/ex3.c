#include <stdio.h>

void swap (int *a, int *b){
    
    int aux;
    aux=*a;
    *a=*b;
    *b=aux;
}


int main (int argc, char **argv){
    
    int num1, num2;

    printf ("TROCA DOIS NUMEROS INTEIROS\n");
    printf("\nInsira o primeiro numero: ");
    scanf("%d", &num1);
    printf("\nInsira o segundo numero: ");
    scanf("%d", &num2);
    
    swap(&num1, &num2);

    printf("\nOs numeros invertidos\nPrimeiro:%d \nSegundo: %d", num1, num2);
  
    return 0;
}