use openssl::rsa::{Padding, Rsa};
use rayon::prelude::*;
use std::{ops::RangeInclusive, time::Instant};

fn run() {
        RangeInclusive::new(0, 1000).into_par_iter().for_each(|_| {
        let rsa = Rsa::generate(1024).unwrap(); // blow up #1
        let data = "THIS IS A VERY LONG LONG LONG LONG LONG STRING THAT IM TRYING".as_bytes(); // why bother allocating a string?
        let padding = Padding::PKCS1;
        let mut encrypted_data = vec![0u8; 512];
        let _ = rsa.public_encrypt(data, &mut encrypted_data, padding);
        let mut decoded_data = vec![0u8; 512];
        // Porque é que este result aqui não é usado?
        let _ = rsa.public_decrypt(&encrypted_data, decoded_data.as_mut_slice(), padding);
    });
}

fn main() {
    // Eu não sei se estás a fazer as contas direito...
    // for _ in 0..5 isto não é 5, isto é 6.
    // Logo são 6 * 9999, não 5*10000
    let media = Instant::now();
    RangeInclusive::new(0, 1)
        .into_par_iter()
        .for_each(|_| run());
    println!("Média de tempos: {:#?}", media.elapsed() )
}
