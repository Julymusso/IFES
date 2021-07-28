#include <stdio.h>
    void ler (float *matriz, int n){
        int i, j;
        for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                scanf("%f",&matriz[i*n + j]);
            }
        }
    }

    float verificaMaior (float *matriz, int n){
        int i, j;
        float maior;

        for (i=0; i<n; i++){
            for (j=0; j<n; j++){
                if (i!=0 && j!=0) {
                    maior = matriz[i*n + j];
                }
                else if (matriz[i*n + j]>maior){
                        maior = matriz[i*n + j];
                }
            }
        }
        return maior;
    }

    float normalizar (float num, float divisor){
        return num/divisor;
    }   

    void escrever (float *matriz, float maior, int n){
        int i, j;
        for (i=0;i<n;i++){
            for (j=0;j<n;j++){
                matriz[i*n + j] = normalizar(matriz[i*n + j],maior);
                printf("%.2f | ",matriz[i*n + j]);
            }
            printf("\n");
        }
    }
