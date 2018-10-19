#include <stdio.h>
#include <gsl/gsl_ieee_utils.h>

//zadanie3

int main(){
    float num = 1.0;
    for(int i=0; i<100; i++){
        num /= 2;
        gsl_ieee_printf_float(&num);
        printf("\n");
    }
}