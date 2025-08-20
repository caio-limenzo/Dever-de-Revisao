def pesquisa():
    listanomes = ["Adalberto", "Benifacio", "Cicero", "Dmitri", "Eureco", "Filemon", "Godot", "Hector", "Indigo", "J"]
    nome = input("Digite um nome para fazer a busca: ").capitalize()
    for i in range(len(listanomes)):
        if nome == listanomes[i]:
            print(f"Nome encontrado na posição {i + 1}")
            return
    print("Nome não encontrado")
    
pesquisa()