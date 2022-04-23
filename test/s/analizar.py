
somaidade = 0
mediaidade = 0

for p in range(1,5):
    print(f'=-=-=-{p}=-=-=-')
    nome = str(input('Qual é o seu nome ? ')).strip().upper()
    idade = int(input('Qual é a sua idade ? '))
    sexo = str(input('Qual o seu Sexo [M/F]')).strip().upper()
    somaidade += idade

mediaidade = somaidade / 4
print(f'a media de idade do grupo é de {mediaidade}.')

