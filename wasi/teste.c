#include <stdio.h>
#include <stdlib.h>
#define uint64 unsigned long long
uint64 factorial_aux(uint64 numero, uint64 counter){
	if(counter == 0) return numero;
	return factorial_aux(counter*numero,counter-1);
}
void factorial(uint64 numero){

	FILE *f = fopen("output.txt","w");

	if (numero < 0) {
		fprintf(f,"Factorial de %lld nao existe\n",numero);
		fclose(f);
		return;
	}
	fprintf(f,"Factorial de %lld = %lld\n",numero,factorial_aux(1,numero));
	fclose(f);
}

int main(int argc, char **argv){
	factorial(atoi(argv[1]));
}
