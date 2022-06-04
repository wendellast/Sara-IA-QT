#Banco de dados
import sqlite3

nome = 'joão'
idade = 32
email = 'joão23@gmail.com'


banco = sqlite3.connect('teste_banco.db')

curso = banco.cursor()

#curso.execute(f'INSERT INTO pessoas VALUES ("{nome}", {idade}, "{email}")')

curso.execute('UPDATE pessoas SET nome = "caio" WHERE idade = 32')

banco.commit()


