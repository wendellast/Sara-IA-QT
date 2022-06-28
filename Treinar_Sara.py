# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from rich import print
from rich.table import Table

import json
import rich
import sqlite3

#Iniciar O treinamento
def iniciar(): 

    table = Table(title='----> SARA  Treinamento <----', title_justify='center', title_style='blue')
    
    table.add_column('IA', justify='center', style='red')
    table.add_column('Suporte', justify='center', style='red')
    
    #Adicionar linhas nas colunas >> 
    table.add_row('Sara, assistente virtual pessoal',  'Contado: Telegram >> https://t.me/Lasstll')

    print(table)
    global bot
    global trainer

    bot = ChatBot("Sara")
    trainer = ListTrainer(bot)

    
def test(arg): # Carregar conversas para treinar
    try:
        banco = sqlite3.connect('db.sqlite3')
        cursor = banco.cursor()

        cursor.execute(f'SELECT text FROM statement')
        nome_db = cursor.fetchall()

    except:
        print('[blue] Não consegue ter acesso ao banco de dados [/]')

    comandos = []
    for i in nome_db:
        comandos.append(i[0])

    banco.close()
   

    
    conversas = []
    
    for k, v in arg.items():
        
        if k in comandos:
            print('[red] Comando já existente [/]')
        
        else:
            conversas.append(k)
            conversas.append(v)

            print(f'[blue]Treinando a Sara para responder:[/] [red] {k} [/] [blue] Com a resposta [/] [red] {v} [/]')
    return conversas



def train_bot(meme): # inciar treinamento 
    global trainer
    
    trainer.train(meme)


def treinar(): # começar treinamento
    iniciar()

    try:
        with open('memoria/memoria.json', 'r', encoding='UTF-8') as file:
                memoria = json.load(file)
    except:
        print(f'[bold red]Erro, memoria das conversas não foi carregado [/] ')
    
    meme = test(memoria)

    if meme:
        try:
            train_bot(meme)
        except:
            print(f'[red] Erro no treinamento [/] ')
        else:
            print(f'[cyan] Treinamento finalizado com sucesso [/] ')



