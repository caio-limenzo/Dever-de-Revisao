n = int(input("Fala um numero"))
def operacao(n):
    soma = 0
    operacoes = 0 
    for i in range(1, n + 1):
        soma += i
        operacoes += 1
    formula = n * (n + 1) // 2

    print(f"Soma: {soma}")
    print(f"Operações: {operacoes}")
    print(f"Formula: {formula}")
    if soma is formula:
        print("A formula é igual a soma dos numeros consecutivos")
operacao(n)
