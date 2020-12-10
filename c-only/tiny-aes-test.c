#include "aes.h"
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void run(){
    
    struct AES_ctx ctx;
    uint8_t key[] = "aaaaaaaaaaaaaaaa";
    uint8_t iv[]  = "bbbbbbbbbbbbbbbb";
    uint8_t str[] = {"This is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\n"};
    for(int g = 0; g < 10000; g++){
        //encriptar
        AES_init_ctx_iv(&ctx, key, iv);
        AES_CBC_encrypt_buffer(&ctx, str, sizeof(str));
        //desencriptar
        AES_init_ctx_iv(&ctx, key, iv);
        AES_CBC_decrypt_buffer(&ctx, str, sizeof(str));
    
    }
}

int main(){

    clock_t start, stop;
    start = clock();
    for(int i = 0; i < 5; i++){
        run();
    }
    stop = clock();
    printf("ELAPSED TIME %f SECONDS.\n",(double)(stop-start)/CLOCKS_PER_SEC);
}