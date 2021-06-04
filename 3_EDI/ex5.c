#include <stdio.h>

int main (int argc, char **argv){
    
    int m1[4][2], vAux[2], i, j;

    for (i=0; i<4; i++){
        for (j=0; j<2; j++){
            scanf("%d",&m1[i][j]);
        }
    }

    for (i=0; i<4; i+=2){
        for (j=0; j<2; j++){
        vAux[j] = m1[i][j];
        m1[i][j] = m1[i+1][j];
        m1[i+1][j] = vAux[j];
        }
    }

    for (i=0; i<4; i++){
        for (j=0; j<2; j++){
            printf("%d ",m1[i][j]);
        }
        printf("\n");
    }
    return 0;
}
        