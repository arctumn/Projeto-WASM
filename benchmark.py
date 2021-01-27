import subprocess
import matplotlib.pyplot as plt

linguagens = ["C","C-WASM", "Rust", "Rust-WASM", "Javascript"]
colors     = ['blue','orange','purple','orange','yellow']
colors2    = ['orange','orange','yellow']

def create_graph(x,y,cores,nome,labelx,labely,titulo):
    plt.title(titulo)
    plt.bar(x,y,color = cores)
    plt.ylabel(labely)
    plt.xlabel(labelx)
    plt.savefig(nome+'.png')
    plt.close()

def aes_benchmark():
    tempo = []
    # C
    result = subprocess.run(['./c-only/tiny-aes/tiny'], stdout=subprocess.PIPE)
    tempo.append(float(result.stdout.decode().rstrip('\n'))*1000)
    print("Resultado de C -> "+str(float(result.stdout.decode().rstrip('\n'))*1000))
    # C -> WASM
    result = subprocess.run(['node', './c-wasm/tiny-aes-wasm/tiny.js'], stdout=subprocess.PIPE)
    tempo.append(float(result.stdout.decode().rstrip('\n'))*1000)
    print("Resultado de C-WASM -> "+str(float(result.stdout.decode().rstrip('\n'))*1000))
    # Rust
    result = subprocess.run(['cargo', 'run', '--manifest-path=rust-only/rust-aes128/Cargo.toml'], stdout=subprocess.PIPE)
    tempo.append(float(result.stdout.decode().rstrip('\n').rstrip('ms')))
    print("Resultado de Rust -> "+result.stdout.decode().rstrip('\n').rstrip('ms'))
    subprocess.run(['cargo', 'clean', '--manifest-path=rust-only/rust-aes128/Cargo.toml'], stdout=subprocess.PIPE)
    # Rust-wasm
    result = subprocess.run(['node', './rust-wasm/rust-aes128-wasm/teste.js'], stdout=subprocess.PIPE)
    tempo.append(float(result.stdout.decode().rstrip('\n').rstrip('ms')))
    print("Resultado de Rust-WASM -> "+result.stdout.decode().rstrip('\n').rstrip('ms'))
    #JS
    result = subprocess.run(['node', './javascript/aes/aes-js.js'], stdout=subprocess.PIPE)
    tempo.append(float(result.stdout.decode().rstrip('\n')))
    print("Resultado de Javascript -> "+str(float(result.stdout.decode().rstrip('\n'))))

    list1 = []
    list1.append(linguagens[1])
    list1.append(linguagens[3])
    list1.append(linguagens[4])
    list2 = []
    list2.append(tempo[1])
    list2.append(tempo[3])
    list2.append(tempo[4])
    create_graph(linguagens[:2],tempo[:2],colors[:2],"C-times-wasm",'Language',"Runtime ms(milliseconds)",'50000 encryptions and decryptions with AES-128')
    create_graph(linguagens[2:4],tempo[2:4],colors[2:4],"Rust-times-wasm",'Language',"Runtime ms(milliseconds)",'50000 encryptions and decryptions with AES-128')
    create_graph(list1,list2,colors2,"wasm-times-wasm-times-js",'Language',"Runtime ms(milliseconds)",'50000 encryptions and decryptions with AES-128')
    #print(f"diferença de {(tempo[2]/tempo[3])*100}%")
    subprocess.run(['mv', 'C-times-wasm.png', 'Rust-times-wasm.png', 'wasm-times-wasm-times-js.png', 'AESGraph'])
    tempo = []
def rsa_benchmark():
    tempo2 = []
    # C
    result = subprocess.run(['./c-only/rsa/rsa'], stdout=subprocess.PIPE)
    tempo2.append(float(result.stdout.decode().rstrip('\n')))
    print("Resultado de C -> "+str(float(result.stdout.decode().rstrip('\n'))))
    # C -> WASM
    result = subprocess.run(['node', './c-wasm/rsa/rsa.js'], stdout=subprocess.PIPE)
    tempo2.append(float(result.stdout.decode().rstrip('\n')))
    print("Resultado de C-WASM -> "+str(float(result.stdout.decode().rstrip('\n'))))
    
    # Não funciona, portanto não irá ser usado por motivos de comparação, derivado a um bug na openssl-crate
    # Rust
    #result = subprocess.run(['cargo', 'run', '--manifest-path=rust-only/rsa_lib/Cargo.toml'], stdout=subprocess.PIPE)
    #tempo2.append(float(result.stdout.decode().rstrip('\n').rstrip('s')))
    #print("Resultado de Rust -> "+result.stdout.decode().rstrip('\n').rstrip('s'))
    # Rust-wasm 
    # result = subprocess.run(['node', './rust-wasm/rust-aes128-wasm/teste.js'], stdout=subprocess.PIPE)
    #tempo2.append(float(result.stdout.decode().rstrip('\n').rstrip('ms')))
    #tempo2.append(0.0)
    #print("Resultado de Rust-WASM -> Indísponivel")
    #JS
    result = subprocess.run(['node', './javascript/rsa/rsa-js.js'], stdout=subprocess.PIPE)
    tempo2.append(float(result.stdout.decode().rstrip('\n')))
    print("Resultado de Javascript -> "+str(float(result.stdout.decode().rstrip('\n'))))
    
    colors_rsa = colors2[1:]
    create_graph(linguagens[:2],tempo2[:2],colors[:2],"C-times-wasm-RSA",'Language',"Runtime s(seconds)",'1000 encryptions and decryptions with RSA-1024')
    lan1 = [linguagens[1],linguagens[4]]
    create_graph(lan1,tempo2[1:],colors_rsa,"wasm-times-js-RSA",'Language',"Runtime s(seconds)",'1000 encryptions and decryptions with RSA-1024')
    subprocess.run(['mv', 'C-times-wasm-RSA.png', 'wasm-times-js-RSA.png', 'RSAGraph'])

aes_benchmark()

rsa_benchmark()
