#include <stdio.h>
#include "rsa.h"
#include <string.h>
#include <stdlib.h>
#include <time.h>
void run(){
  struct public_key_class pub[1];
  struct private_key_class priv[1];
  rsa_gen_keys(pub, priv, PRIME_SOURCE_FILE);
  
  char message[] = "THIS IS A VERY LONG LONG LONG LONG LONG STRING THAT IM TRYING";

  
  long long *encrypted = rsa_encrypt(message, sizeof(message), pub);
  if (!encrypted){
    fprintf(stderr, "Error in encryption!\n");
    return;
  } 
  
  char *decrypted = rsa_decrypt(encrypted, 8*sizeof(message), priv);
  if (!decrypted){
    fprintf(stderr, "Error in decryption!\n");
    return;
  }
  //printf("message = %s\n",decrypted);
  free(encrypted);
  free(decrypted);
}

int main(){
  clock_t start, stop;
  start = clock();
  for(int i = 0;i<50000;i++){ run();}
  stop = clock();
  printf("ELAPSED TIME %f SECONDS.\n",(double)(stop-start)/CLOCKS_PER_SEC);
  return 0;
}
