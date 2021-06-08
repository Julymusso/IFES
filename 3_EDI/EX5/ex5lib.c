#include <stdio.h>
    
void ler(int *matriz, int l, int c){
    int i, j;

    for (i=0; i<l; i++){
        for (j=0; j<c; j++){
            scanf("%d",&matriz[i*c+j]);
        }
    }
}

void troca(int *matriz, int l, int c){
    int i, j, vAux[c];

    for (i=0; i<l; i+=2){
        for (j=0; j<c; j++){
        vAux[j] = matriz[i*c+j];
        matriz[i*c+j] = matriz[(i+1)*c+j];
        matriz[(i+1)*c+j] = vAux[j];
        }
    }
}

void escrever(int *matriz, int l, int c){
    int i, j;

    for (i=0; i<l; i++){
        for (j=0; j<c; j++){
            printf("%d ",matriz[i*c+j]);
        }
        printf("\n");
    }
}