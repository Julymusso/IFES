#include <stdio.h>

    /*Pede para o usuário preencher o vetor*/
    void ler (int *vNum, int n){
        int i;
        printf("Insira %d numeros para preencher o vetor:\n",n);
        for (i=0;i<n;i++){
            scanf("%d",&vNum[i]);
        }
    }

    /*Função para passar para outro vetor apenas valores diferentes de 0
    */
    void troca(int *vNum, int n){
        int i, j, vNumAux[10];
        j=0;
        for (i=0;i<n;i++){
            if (vNum[i]!=0){
                vNumAux[j]=vNum[i];
                j++;
            }
        }
        for (i=0;i<j;i++){
            vNum[i]=vNumAux[i];
        }
        for (i=j+1;i<n;i++){
            vNum[i]=0;
        } 
    }

    void mostrar(int *vNum, int n){
        int i;
        printf("\n\nNovo vetor:\n");
        for (i=0;i<n;i++){
            printf("%d | ",vNum[i]);
        }
    }