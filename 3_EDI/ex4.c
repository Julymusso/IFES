#include <stdio.h>

int main (int argc, char **argv){

    int i, j, maior;
    float m1[3][3];

    for (i=0;i<3;i++){
        for (j=0;j<3;j++){
            scanf("%f",&m1[i][j]);
            if (i==0 && j==0) {
                maior = m1[i][j];
            }
            else if (m1[i][j]>maior) {
                maior = m1[i][j];
            }
        }
    }
    for (i=0;i<3;i++){
        for (j=0;j<3;j++){
            m1[i][j] = m1[i][j]/maior;
            printf("%.2f | ",m1[i][j]);
        }
        printf("\n");
    }

    return 0;
}