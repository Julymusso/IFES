#include <stdio.h>
#include "ex1lib.h"

int main (int argc, char **argv){

    int qtdNotas;
    unsigned char nome[50];
    double notas[10];

    ler (nome, &qtdNotas, notas);
    escrever (nome, calcMedia (notas, qtdNotas));
  
    return 0;
}