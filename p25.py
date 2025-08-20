def cpfverificadormonstruosocatastroficobizarro():
    cpf = input("Digite um CPF valido: ")
    tamanho = len(str(cpf))
    if not cpf.isdigit():
        print("CPF INVALIDO")
    elif tamanho != 11:
        print("CPF INVALIDO")
    else:
        print("cpf valido :)")



cpfverificadormonstruosocatastroficobizarro()