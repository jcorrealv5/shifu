#Demo 29: Cifrado Por Bit XOR
print("Demo 29: Cifrado Por Bit XOR")
texto = input("Ingresa el Texto a Cifrar: ")
nTexto = len(texto)
clave = int(input("Clave a cifrar (Entrei entre 0-30): "))
cifrado = ""
for i in range(nTexto):
    n = ord(texto[i])
    c = n ^ clave
    cifrado += chr(c)
print("El Texto Cifrado es: ", cifrado)
