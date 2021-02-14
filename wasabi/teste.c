#include <stdio.h>
#include <stdlib.h>


int fib(n){
  if(n == 0) return  0; else if (n == 1) return 1;
  else return (fib(n-1)+fib(n-2));
}
int main(void){
  printf("output = %d\n",fib(10));
  return 0;
}
