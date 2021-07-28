#include <stdio.h>

void imprime (int *v, int tam){
    
    for (int i=0; i<tam; i++ ){
        printf ("%d | ", *(v+i));
    }
}


int main (int argc, char **argv){
    
    int tam, vetor[]={1, 3, 5, 7, 9};
    tam=5;

    imprime(vetor, tam);
   
    return 0;
}