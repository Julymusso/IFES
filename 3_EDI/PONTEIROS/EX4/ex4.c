#include <stdio.h>

int main (int argc, char **argv){
    
    int matriz[5][4], i, *pmt;
    pmt = matriz[0];
    for (i=0; i<20; i++){
        *(pmt+i) = i;
    }
    
    for (i=0; i<20; i++){
        printf(" %d |",*(pmt+i));
        if (!((i+1)%4)) printf("\n");
    }
  
    return 0;
}