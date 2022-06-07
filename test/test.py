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
    primeira_tela.label_4.setText("")
    nome_usuario = primeira_tela.lineEdit.text()
    senha = primeira_tela.lineEdit_2.text()
    
    if nome_usuario == "wendellast" and senha == "1234" :
        primeira_tela.close()
        segunda_tela.show()
    else :
        primeira_tela.label_4.setText("Dados de login incorretos!")