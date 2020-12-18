const NodeRSA = require('node-rsa');

const performance = require('perf_hooks').performance;

function run(){
    const key = new NodeRSA({b: 1024});
    
    const text = 'This is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\nThis is a very long text message to test heavy compression and decompression!\n';
    const encrypted = key.encrypt(text, 'base64');

    key.decrypt(encrypted, 'utf8');
}

var t_start = performance.now()
for(i = 0;i<50000;i++) run()
var t_end = performance.now()

console.log("Time taken is: "+ ((t_end - t_start)/1000).toFixed(4) + " seconds")