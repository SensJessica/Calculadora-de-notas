# incio do sofrimento

turma = []
nomeAluno = []
mediaModulo = []
MediaMR = 0

# Código

# Quantidade de Alunos
quantidade_alunos = int(input("Por favor, nsira a quantidade de alunos da sua turma: "))
turma.append(quantidade_alunos)


# Loop para pegar as informações dos Alunos
for i in range(quantidade_alunos):
    nome = input(f'Insira o nome do Aluno {i + 1}: ')
    nomeAluno.append(nome)


    nota1 = float(input("Insira o valor da nota (de 0 à 10) da Atividade Avaliativa 1: "))
    while nota1 < 0 or nota1 > 10:
        nota1 = float(input("Erro, a nota inserida está incorreta. Por favor inserir uma nota válida: "))


    nota2 = float(input("Insira o valor da nota (de 0 à 10) da Atividade Avaliativa 2: "))
    while nota2 < 0 or nota2 > 10:
        nota2 = float(input("Erro, a nota inserida está incorreta. Por favor inserir uma nota válida: "))

    nota3 = float(input("Insira o valor da nota (de 0 à 10) da Atividade Avaliativa 3: "))
    while nota3 < 0 or nota3 > 10:
        nota3 = float(input("Erro, a nota inserida está incorreta. Por favor inserir uma nota válida: "))


    media = (nota1 + nota2 +nota3) / 3
    print(f"{media:}")
    mediaModulo.append(MediaMR)

# Cálculo da média do aluno
    media = (nota1 + nota2 + nota3) / 3
    print(f"Média do Aluno {nome}: {media:.2f}")

    # Verificação se o aluno precisa de recuperação
    if media < 7:
        print(f'{nome}, sua média não alcançou a nota requerida, favor fazer a recuperação.')
        nota4 = float(input('Insira o valor da nota (de 0 à 10) da Atividade de Recuperação: '))

        while nota4 < 0 or nota4 > 10:
            nota4 = float(input('Erro, a nota inserida está incorreta. Inserir uma nota válida: '))

        MediaMR = (media + nota4) / 2
        print(f'Nova média após recuperação de {nome}: {MediaMR:.2f}')
        mediaModulo.append(MediaMR)
    else:
        mediaModulo.append(media)

# Contagem de alunos aprovados e reprovados
quantAprovado = sum(1 for media_aluno in mediaModulo if media_aluno >= 7)
quantReprovado = quantidade_alunos - quantAprovado

# Exibição dos resultados
print(f'Alunos Aprovados: {quantAprovado}')
print(f'Alunos Reprovados: {quantReprovado}')
print(f'Percentual de Aprovados: {(quantAprovado / quantidade_alunos) * 100:.2f}%')
print(f'Percentual de Reprovados: {(quantReprovado / quantidade_alunos) * 100:.2f}%')