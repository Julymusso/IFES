#include <stdio.h>

int main(int agrc, char **argv){
    
    int v1[10], v2[10], i, a;

    for (i=0;i<10;i++){
        scanf("%d",&v1[i]);
    }

    for (a=0, i=0; i<10; i++){
        if (v1[i] != 0) {
            v2[a] = v1[i];
            a++;
        }
    }
    
    a=i-a; /*Quantidade de "espacos vagos" no novo vetor a serem preenchidos com zeros.*/
    if (a != 0) {
        for (i=10-a;i<10;i++){
            v2[i]=0;
        }
    } 

    for (i=0; i<10; i++){
        printf("%d ",v2[i]);
    }
    return 0;
}