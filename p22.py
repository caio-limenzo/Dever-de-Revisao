def checarsenha():
    senhacorreta = "senha123"
    tentativas = 0

    while tentativas < 3:
        senha = input(f"Digite a senha({3 - tentativas} tentativas restantes): ")

        if senha == senhacorreta:
            print("Bem-vindo!")
            return
        else:
            print("Senha incorreta.")
            tentativas += 1

    print("Acesso bloqueado.")
checarsenha()
