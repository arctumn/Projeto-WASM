use std::time::Instant;

use aes::Aes128;
use block_modes::{BlockMode, Cbc};
use block_modes::block_padding::Pkcs7;
use hex_literal::hex;

// create an alias for convenience
type Aes128Cbc = Cbc<Aes128, Pkcs7>;
fn run() -> bool{
    let key = hex!("000102030405060708090a0b0c0d0e0f");
    let iv = hex!("f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff");
    let plaintext = b"This is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!";
    let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();
    
    // buffer must have enough space for message+padding
    let mut buffer = [0u8; 320];
    // copy message to the buffer
    let pos = plaintext.len();
    buffer[..pos].copy_from_slice(plaintext);
    let ciphertext = cipher.encrypt(&mut buffer, pos).unwrap();
    
    //assert_eq!(ciphertext, hex!("1b7a4c403124ae2fb52bedc534d82fa8"));
    
    // re-create cipher mode instance and decrypt the message
    let cipher = Aes128Cbc::new_var(&key, &iv).unwrap();
    let mut buf = ciphertext.to_vec();
    let decrypted_ciphertext = cipher.decrypt(&mut buf).unwrap();
    decrypted_ciphertext == plaintext
}
fn test() {
    for _ in 0..10000{
        run();
    }
}
fn main(){
    let media = Instant::now();
    for _ in 0..5 {
        test();
    }
    println!("{:#?}",media.elapsed()/5)
}