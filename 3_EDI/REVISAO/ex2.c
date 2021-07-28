/*Sabendo que os números perfeitos conhecidos são definidos pela fórmula 2^(n-1)*(2^(n-1)), sendo n um número primero
e que os 4 primeiros números perfeitos veem da fórmula cujo n representa os 4 primeiros primos temos:*/ 
#include <stdio.h>

int main (int argc, char **argv){
    int primos[4], perfeitos[4], i, a, numero, termo1, termo2; /* i e a : contadores*/
    
    /* Calcula os 4 primeiros primos e armazena em um vetor*/
    a=0;
    numero=2;
    while (a<4){
        for (i=1;i<=(numero/2);i++){
            if (i!=1 && numero%i==0){
                numero++;
                i=1;
            }
        }
        primos[a]=numero;
        a++;
        numero++;
        i=1;
    }
    
/*aplica a fórmulo utilizandos os primos armazenados no vetor "primos" e exibe os perfeitos*/
    for (i=0;i<4;i++){
        termo1=1;
        termo2=2;
        a=0;
        
        while (a < (primos[i]-1)){
            termo1=termo1*2;
            termo2=termo2*2;
            a++;
        }
        
        perfeitos[i]=termo1*(termo2-1);
        printf("%d ",perfeitos[i]);
    }
    return 0;
}
