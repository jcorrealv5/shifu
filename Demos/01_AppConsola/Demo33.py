import base64

#Demo 33: Conversion de ASCII a Otras Bases: Base32, Base64

print("#Demo 33: Conversion de ASCII a Otras Bases: Base32, Base64")
textoASCII = input("Ingresa un Texto a convertir en otra Base: ")
textoBytes = textoASCII.encode("utf-8")

textoBase32 = base64.b32encode(textoBytes)
print("Texto Base 32: ", textoBase32)

textoBase64 = base64.b64encode(textoBytes)
print("Texto Base 64: ", textoBase64)