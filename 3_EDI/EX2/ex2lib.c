/*Sabendo que os números perfeitos conhecidos são definidos pela fórmula 2^(n-1)*(2^(n)-1), sendo n um número primero
e que os 4 primeiros números perfeitos veem da fórmula cujo n representa os 4 primeiros primos temos:*/ 
#include <stdio.h>
    
long int calculaPrimos (long int *vNumPrimos, int n){
    int i, j;
    long int numero;
    /*Se um número possui um divisor antes ou até sua metade, 
    ele terá necessariamente um correspontende após sua metade.
    Portanto basta fazer a verificação em apenas uma metade do numero
    para saber se ele possuir divisor além do 1.*/
    j=0;/*posição do vetor vNumPrimos*/
    numero=2;/*Os números serão testados a partir do 2, pois sabemos que 1 é divisível apenas por ele mesmo.*/
    while (j<n){ /*repete até preencher o vetor com os "n" primeiros primos*/
        for (i=1;i<=(numero/2);i++){ /*faz divisões sucessivas até chegar a metade dele*/
            if (i!=1 && numero%i==0){ /*Se o resto da divisão for 0, o número possui divisor, portanto nã e primo*/
                numero++;/*vai para o proximo numero a ser testado*/
                i=1;/*reinicia o contador a partir do um*/
            }
        }
        vNumPrimos[j]=numero;/*caso o numero saia do laço, ele e primo então entra no vetor*/
        j++; /*vetor "pula" para a proxima posicao*/
        numero++; /*vai para o proximo numero a ser testado*/
        i=1;/*reinicia o contador a partir do um*/
    }
    return *vNumPrimos;
}

/*aplica a potencia de um numero de base "a" e expoente "b"*/
long int pot(long int a, long int b){
    long int potencia;
    int i;
    potencia=a;

    if (b==0){
        potencia=1;
    }
    else{
        for (i=1; i<b; i++){
            potencia = potencia*a;
        }
    }
    return potencia;
}

/*aplica a fórmula utilizandos os primos armazenados no vetor "primos" e exibe os perfeitos*/
long int calculaPerfeitos (long int *vNumPrimos, long int *vNumPerfeitos, int n){
    int i;

    for (i=0;i<n;i++){ /*repete até preencher o vetor com os 4 primeiros perfeitos*/
        vNumPerfeitos[i] = pot(2,vNumPrimos[i]-1)*(pot(2,vNumPrimos[i])-1); /*aplica a conjecutra para numeros perfeitos*/
    }
    return *vNumPerfeitos;
}

void escrever (long int *vNumPerfeitos, int n){
    int i=0;

    printf("A Sequencia dos %d primeiros numeros perfeitos e: ", n);
    for (i=0; i<n; i++){
        printf("%li ", vNumPerfeitos[i]);
    }
}