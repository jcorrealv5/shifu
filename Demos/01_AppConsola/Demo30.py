#Demo 29: Cifrado Por Bit XOR
print("Demo 30: Cifrado ROT")
texto = input("Ingresa el Texto a Cifrar: ")
nTexto = len(texto)
clave = int(input("Cantidad a Rotar (Entre entre 1-25): "))
cifrado = ""
for i in range(nTexto):
    n = ord(texto[i])
    c = n + clave
    cifrado += chr(c)
print("El Texto Cifrado es: ", cifrado)

descifrado = ""
nCifrado = len(cifrado)
for i in range(nCifrado):
    n = ord(cifrado[i])
    c = n - clave
    descifrado += chr(c)
print("El Texto Descifrado es: ", descifrado)