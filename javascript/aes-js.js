var aesjs = require('aes-js');

const performance = require('perf_hooks').performance;

function run(){
    // An example 128-bit key
    var key = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 ];

    // The initialization vector (must be 16 bytes)
    var iv = [ 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34,35, 36 ];

    // Convert text to bytes (text must be a multiple of 16 bytes)
    var text = 'This is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\n';
    
    var extra = text.length % 16
    if(extra > 0)
        var padding = 16 - extra
        for(let i = 0; i< padding; i++){
            text = text + " "
        }

    var textBytes = aesjs.utils.utf8.toBytes(text);

    var aesCbc = new aesjs.ModeOfOperation.cbc(key, iv);
    var encryptedBytes = aesCbc.encrypt(textBytes);

    // To print or store the binary data, you may convert it to hex
    var encryptedHex = aesjs.utils.hex.fromBytes(encryptedBytes);

    // When ready to decrypt the hex string, convert it back to bytes
    var encryptedBytes = aesjs.utils.hex.toBytes(encryptedHex);

    // The cipher-block chaining mode of operation maintains internal
    // state, so to decrypt a new instance must be instantiated.
    var aesCbc = new aesjs.ModeOfOperation.cbc(key, iv);
    var decryptedBytes = aesCbc.decrypt(encryptedBytes);

    // Convert our bytes back into text
    aesjs.utils.utf8.fromBytes(decryptedBytes);

}
var t_start = performance.now()
for(i = 0;i<50000;i++) run()
var t_end = performance.now()

console.log("Time taken is: "+ ((t_end - t_start)/1000).toFixed(4) + " seconds")
