import random, secrets
#Demo32: Generando datos al azar usando secrets

def token_AZ(n):
    rpta = ""
    for i in range(n):
        n =  random.randint(65, 90)
        rpta += chr(n)
    return rpta

def token_09(n):
    rpta = ""
    for i in range(n):
        rpta += str(random.randint(0, 9))        
    return rpta

def token_AlfaNumerico(n):
    rpta = ""
    for i in range(n):
        n = random.randint(0,2)
        if(n==0):
            rpta += str(random.randint(0, 9))
        else:
            rpta += chr(random.randint(65, 90))
    return rpta

print("Demo32: Generando datos al azar (tokens usando secrets")
tokenBytes = secrets.token_bytes(4)
tokenString = tokenBytes.decode('latin-1')
print("Token en Bytes: ", tokenBytes)
print("Token en String: ", tokenString)

tokenHexa = secrets.token_hex(32)
print("Token en Hexadecimal: ", tokenHexa)

tokenUrl = secrets.token_urlsafe(6)
print("Token URL Segura: ", tokenUrl)

tokenAZ = token_AZ(6)
print("Token A-Z: ", tokenAZ)

token09 = token_09(6)
print("Token 0-9: ", token09)

tokenAlfaNumerico = token_AlfaNumerico(6)
print("Token AlfaNumerico: ", tokenAlfaNumerico)
