def notasuau():
    notas = [1, 3, 6, 6, 7, 7, 7, 8, 9, 10]
    media = round(sum(notas)/len(notas), 2)
    print(f"A media da turma foi de {media} pontos")
    print(f"A menor nota foi {notas[0]}, que lixo")
    print(f"A maior nota foi {notas[-1]}, brabo")
    acima_da_media = sum(1 for nota in notas if nota > media)
    porcentage = round((acima_da_media/len(notas)) * 100)
    print(f"{porcentage}% dos alunos estao acima da media")
notasuau()