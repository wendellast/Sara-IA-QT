import sqlite3


def cadastrar(): # Pronto // Precisa melhorar
    nome = str(input('Digite o seu nome: '))
    senha = str(input('Digite a sua senha: '))
    c_senha = str(input('confirme a sua senha'))

    if (senha == c_senha):
        try:
            banco = sqlite3.connect('banco_cadastro.db') 
            cursor = banco.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, senha text)")
            cursor.execute(f"INSERT INTO cadastro VALUES('{nome}', '{senha}') ")

            banco.commit() 
            banco.close()
            print('Usuario cadastrado com sucesso')

        except sqlite3.Error as erro:
            print("Erro ao inserir os dados: ",erro)
    else:
            print('As senhas digitadas são diferentes')

def login():
    nome_usuario = str(input('Digite o seu nome: '))
    senha = str(input('Digite a sua senha: '))
    banco = sqlite3.connect('banco_cadastro.db')
    cursor = banco.cursor()

    try:
        
        cursor.execute(f'SELECT nome FROM cadastro  WHERE nome="{nome_usuario}"')
        nome_db = cursor.fetchall()
        cursor.execute(f'SELECT senha FROM cadastro  WHERE nome="{nome_usuario}"')
        senha_db = cursor.fetchall()
        print(nome_db)
        print(senha_db)
        banco.close()

    except:
        print('Usuario não cadastrado')

    try:
        if  senha ==  senha_db[0][0] and nome_usuario ==  nome_db[0][0]:
            print('logado')
        else:
            print('Erro senha incorreta')
    except:
        print('Erro usuario não encontrado')
login()