use openssl::rsa::{Rsa, Padding};
use std::time::Instant;

fn run(){
    for _ in 1..10000{
        let rsa = Rsa::generate(1024).unwrap();
        let data: Vec<u8> = String::from("THIS IS A VERY LONG LONG LONG LONG LONG STRING THAT IM TRYING").into_bytes();
        let mut encrypted_data: Vec<u8>  = vec![0; 512];
        let padding = Padding::PKCS1;
        let _ = rsa.public_encrypt(&data, encrypted_data.as_mut_slice(), padding).unwrap();
        let mut y: Vec<u8> = vec![0; 512];
        let _  = rsa.public_decrypt(&encrypted_data, y.as_mut_slice(), padding);
    }
}

fn main() {
    let media = Instant::now();
    for _ in  0..5{
        run()
    }
    println!("Media dos Tempos: {:#?}",media.elapsed()/5)
}