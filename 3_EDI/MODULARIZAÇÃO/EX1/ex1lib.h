#ifndef _ex1lib_h_
#define _ex1lib_h_

#define Qtd_Notas 3

void ler (unsigned char *vNomeAluno, unsigned int iQtdNotas, double *vNotas);
int calcMedia (double vNotas, unsigned int iQtdNotas);
void escrever (unsigned char *vNomeAluno, double fMedia);

#endif