#include <stdio.h>

void Strcopy(char *dest, char *src, int count){
    int i=0;
    while (count--){
        *(dest+i) = *(src+i);
        i++;
    }
    *(dest+i)='\0';
}

int main (int argc, char **argv){
    
    char str1[50], str2[50];
    int tamanho;

    printf("Digite uma frase: ");
    gets(str2);
    printf("Digite quantos caracteres de dessa frase deseja copiar: ");
    scanf("%d", &tamanho);

    Strcopy(str1, str2, tamanho);
    printf("\nO trecho copiado foi: %s", str1);
  
    return 0;
}