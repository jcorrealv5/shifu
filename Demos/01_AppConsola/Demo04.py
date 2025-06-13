import random

#Demo 04: Bucles con Numeros al Azar
titulo = "Demo 04: Bucles con Numeros al Azar"
print(titulo)
print("_" * len(titulo))
num1To6 = random.randint(1,6)
print("Digito de 1 al 6 =", num1To6)
caracterAZ = chr(random.randint(65,90))
print("Caracter de A al Z =", caracterAZ)
#Generar un Captcha de 6 caracteres y/o digitos
captcha = ""
for i in range(6):
    captcha += (str(random.randint(0,9)) if random.randint(1,2)==1 else chr(random.randint(65,90)))
    '''
    tipo = random.randint(1,2)
    if(tipo==1):
        captcha += str(random.randint(0,9))
    else:
        captcha += chr(random.randint(65,90))
    '''
print("Catpcha = ", captcha)