import sqlite3


def cadastrar(): # Pronto // Precisa melhorar
  
    while True:

        try:
            nome = str(input('Digite o seu nome: '))
            senha = str(input('Digite a sua senha: '))
            c_senha = str(input('confirme a sua senha'))

            banco = sqlite3.connect('banco_cadastro.db') 

            cursor = banco.cursor()
            cursor.execute(f'SELECT nome FROM cadastro  WHERE nome="{nome}"')
            nome_db = cursor.fetchall()

            cursor.execute(f'SELECT senha FROM cadastro  WHERE nome="{nome}"')
            senha_db = cursor.fetchall()
            
        except:
            print('Erro de acesso')

        try:
            if  senha ==  senha_db[0][0] and nome ==  nome_db[0][0]:
                print('Usuario já cadastrado')
                print('Tente novamente')
                continue

        except:
            break

    if (senha == c_senha):
        try:
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
        print('Erro de conexão')

    try:
        if  senha ==  senha_db[0][0] and nome_usuario ==  nome_db[0][0]:
            print('logado')

    except:
        print('Usuario e senha incorretos')



login()