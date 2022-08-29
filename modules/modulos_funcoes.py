from rich import print
from config.config_dados import *
from datetime import date

import json
import shutil
import psutil
import tempfile
import os
import pandas as pd

#Módulos
try:
    Versao = 'Versão Beta v1.0'
    ano_criacao = 2022
    ano_atual = date.today().year
except:
    resposta('Deu algum erro nos dados')

def relatorio():
    resposta('Ok')
    resposta('Apresentando relatório')
    resposta('Primeiramente, meu nome é SARA muito prazer')
    resposta(f'Atualmente estou em uma versão de testes {Versao}')
    resposta('Sou um assistente virtual em desenvolvimento estou sempre aprendendo coisas novas')
    resposta('Eu fui criado na linguagem python')
    resposta(f'Eu nasce no ano {ano_criacao} então eu tenho {(ano_criacao-ano_atual)+1} ano de idade')
    resposta('Diariamente recebo varias atualizações')
    resposta('Uso um modulo de reconhecimento de voz offline e oline')

def ler_frase():
    try:
        comandos = pd.read_csv('command/comandos.csv')  
        
        if not os.path.isfile('command/comandos.csv'):
            pass
            
        try:
            frase = comandos.loc[0, 'comandos']
            
            resposta(frase)
        
            
        except:
            pass
    except:
        pass
    
    
def perguntas(usuario=str): # Faz a sara fazer perguntas
    comandos = pd.read_csv('command/comandos.csv')  
    
    if not os.path.isfile('command/comandos.csv'):
        pass
        
    try:
        frase = comandos.loc[0, 'comandos']
        
        aprender(frase, usuario)
       
        
        
        save = comandos.drop(0, axis=0)
        save.to_csv('command/comandos.csv', index=False)
        
    except:
        pass

def aprender(chaves=str, valores=str): # Ensia a Sara aprender coisas novas
    
    
    chave = chaves
    valor = valores
  
    try:
                
        with open('memoria/memoria.json', 'r', encoding='UTF-8') as arq, \
            tempfile.NamedTemporaryFile('w', delete=False,encoding='UTF-8') as out:
            # ler todo o arquivo e obter o objeto JSON
            dados = json.load(arq)
            # atualizar os dados com a nova pergunta
            dados[chave] = valor
            # escreve o objeto atualizado no arquivo temporário
            json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))

        
        resposta('Há entende !!')
        # se tudo deu certo, renomeia o arquivo temporário
        shutil.move(out.name, 'memoria/memoria.json')
    
    except:
       pass

    
def historico():
    try:
        print('Histórico: \n')
        lista = [2,1]
        for comandos in lista:
                print(str(comandos))
    except:
        pass
    
#Localização adicionar depois
#Clima adicionar depois
#Moeda

#def email(): fazer depis
#Agenda
#Marca tempo ex: Sara marca 10 minutos.. depois de 10 minutos ela chama você de volta
#tirar print da tela
    