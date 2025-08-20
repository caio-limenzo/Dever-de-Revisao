numero = int(input("Fale um numero"))
def tabuada(numero):
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} * {i} = {resultado}")

tabuada(numero)