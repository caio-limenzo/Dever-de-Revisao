n1 = int(input("Fale um numero: "))
n2 = int(input("Fale outro numero: "))

def maiornumero(n1, n2):
    if n1 > n2:
        return n1
    elif n1 < n2:
        return n2
    else:
        return None
resultado = maiornumero(n1, n2)
if resultado == None:
    print("Os numeros sao iguais")
else:
    print(resultado)