from rich import print
from config.config_dados import *
from datetime import date

import os

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



           

           


    
def historico():
    print('Histórico: \n')
    lista = [2,1]
    for comandos in lista:
            print(str(comandos))

#Localização adicionar depois
#Clima adicionar depois
#Moeda

#def email(): fazer depis
#Agenda
#Marca tempo ex: Sara marca 10 minutos.. depois de 10 minutos ela chama você de volta
#tirar print da tela
    