import matplotlib.pyplot as plt

linguagens = ["C", "C-WASM", "Rust", "Rust-WASM", "Javascript"]
tempo = [5,6,4,6,6]
fig = plt.figure(figsize=(7,5))


plt.title('Time for 50000 encryption and decrytion')

plt.bar(linguagens,tempo)
plt.ylabel('Runtime')
plt.xlabel('Language')
plt.show()