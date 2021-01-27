const NodeRSA = require('node-rsa');

const performance = require('perf_hooks').performance;

function run(){
    const key = new NodeRSA({b: 1024});
    
    const text = 'THIS IS A VERY LONG LONG LONG LONG LONG STRING THAT IM TRYING';
    const encrypted = key.encrypt(text, 'base64');

    key.decrypt(encrypted, 'utf8');
}

var t_start = performance.now()
for(i = 0;i<1000;i++) run()
var t_end = performance.now()

console.log(((t_end - t_start)/1000).toFixed(4))