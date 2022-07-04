from vosk import Model, KaldiRecognizer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from rich import print
from build import sistema_solar
from logging import basicConfig
from chatterbot import ChatBot
from difflib import SequenceMatcher
from Treinar_Sara import treinar
from modules.modulos_funcoes import *
from config.config_dados import *
from chatterbot.comparisons import LevenshteinDistance
from rich import pretty
from config.config import *

import chatterbot
import speech_recognition as sr
import os
import pyaudio
import pyttsx3
import sys
import datetime
import psutil
import webbrowser
import vlc
import json
import requests
import time
import wikipedia
import platform
import shutil
import tempfile
import sqlite3
import pyautogui
import random

try:
    import pywhatkit
    net = True
except:
    net = False

#Arquitetura 
Digitar = False # Função para decide se vai querer digitar ou falar, caso queira digitar mude para True
Versao = 'Beta v1.0'
plataforma = platform.system()
diretorio_atual=os.getcwd()
pretty.install()
historico = []

# Acesso ao microfone
r = sr.Recognizer()

ACCEPTANCE = 0.70

def comparate_messages(message, candidate_message):
    similarity = 0.0

    if message.text and candidate_message.text:
        message_text = message.text
        candidate_text = candidate_message.text

        similarity = SequenceMatcher(
            None,
            message_text,
            candidate_text
        )
        similarity = round(similarity.ratio(),2)
        
        if similarity < ACCEPTANCE:
            similarity = 0.0
        else:
            #print("Mensagem do usuário:",message_text,", mensagem candidata:",candidate_message,", nível de confiança:", similarity)
            pass
    return similarity

def select_response(message, list_response, storage=None):
    response = list_response[0]
    #print("resposta escolhida:", response)

    return response

bot = ChatBot("Sara",
                    read_only=True,
                    statement_comparison_function=comparate_messages,
                    response_selection_method=select_response,
                    
                    
                    logic_adapters=[
                        
                        {
                           
                            "import_path":"chatterbot.logic.MathematicalEvaluation",
                            "import_path":"chatterbot.logic.BestMatch",
                            "statement_comparison_function": chatterbot.comparisons.LevenshteinDistance,
                           
                        
                        }

])                   
   


  

def SomIncial():
    p = vlc.MediaPlayer("music/StartSound.mp3")
    p.play()

SomIncial()

def SomCarregamento():
    p = vlc.MediaPlayer("music/AI.mp3")
    p.play()

# Validação da pasta de modelo
# É necessário criar a pasta model-br a partir de onde estiver esta fonte
if not os.path.exists("model-br"):
    print("Modelo em portugues não encontrado.")
    exit(1)
    
if not os.path.exists("memoria"):
    print("A memoria  não encontrado.")
    exit(1)

if net == False:
    # Apontando o algoritmo para ler o modelo treinado na pasta "model-br"
    model = Model("model-br")
    rec = KaldiRecognizer(model, 16000)

    # Preparando o microfone para captura
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()


if 'Windows' in plataforma:
    # Trás a função letícia voz
    sara_voz=pyttsx3.init('sapi5')

    # Função de ajuste de voz da sara
    voz = sara_voz.getProperty('voices')
    sara_voz.setProperty('voice', voz[2].id)
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)

else:
    # Trás a função letícia voz # Se não for a voz leticia padrão é Espeak
    sara_voz=pyttsx3.init()

    # Função de ajuste de voz da sara
    sara_voz.setProperty('voice', 'pt+f2')
    # No 'm2'(masculino) pode colocar 'f2'(feminino) e números até 7
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)



linha_sara()  
resposta('Olá')
BoasVindas()
resposta('Iniciando módulos')

class mainT(QThread):
    def __init__(self):
        super(mainT,self).__init__()

    def run(self):
        SomCarregamento()
        resposta('Ok')
        resposta('Módulos Carregados')
        resposta('Tudo pronto, o que deseja ?')
        self.SARA()

    # Aciona os comandos
    # Faz o reconhecimento
    def GivenCommand(self):
       
        if net == False:
              
                rec.pause_threshold = 1
                # Lendo audio do microfone
                data = stream.read(20000)
                # Convertendo audio em texto
                rec.AcceptWaveform(data)  
              

                try:
                    Input = rec.Result()
                except:
                    # Retorna os erros
                    print('Não entendi, fale novamente')
                    #resposta("Não entendi o que você disse, fale novamente.")
                    return 'none'
                #Input = Input.lower()
                return Input
       
        else:
           
                
                
          # Input = rec.Result()
            with sr.Microphone() as s:
                # r.adjust_for_ambient_noise(s)
                audio = r.listen(s,4, 5)
                try:
                    
                    speech = r.recognize_google(audio, language= "pt-BR")
                    speech.lower()
    
                except:
                    # Retorna os erros
                    print('Não entendi, fale novamente')
                    # resposta("Não entendi o que você disse, fale novamente.")
                    return 'none'
            #Input = Input.lower()
            
            return speech
    
    def Digitar_comando(self): # Função para digitar os comandos ao invés de falar
            Input = input("\033[31m(つ◕౪◕)つ━☆ﾟ.*･｡ﾟ \033[m")
            return Input
    
            
    # Comandos e conversas   
    def SARA(self):
        while True:

            if Digitar == False:
                self.Input = self.GivenCommand().lower() # Função de falar
            else:
                self.Input = self.Digitar_comando().lower() # Função de escrever 

            BASE_DIR = os.path.dirname(__file__)
            SAVE_TO = os.path.join(BASE_DIR, 'mente.json')
           
            historico_base = []
            

            historico_base.append(self.Input)
            historico.append(historico_base[:])



            if 'none' in self.Input:
                return self.Input

            if 'bom dia' in self.Input: #Boa Noite Sara
                Horario = int(datetime.datetime.now().hour)
                if Horario >= 0 and Horario < 12:
                    resposta('Olá')
                    resposta('Bom dia')
                
                elif Horario >= 12 and Horario < 18:
                    resposta('Agora não é mais de manhã')
                    resposta('Já passou do meio dia')
                    resposta('Estamos no período da tarde')
                
                elif Horario >= 18 and Horario != 0:
                    resposta('Agora não é de manhã')
                    resposta('Já estamos no período noturno')
                    resposta('Boa noite')
            
            if 'boa tarde' in self.Input: #Boa Noite Sara
                Horario = int(datetime.datetime.now().hour)
                if Horario >= 0 and Horario < 12:
                    resposta('Agora não é de tarde')
                    resposta('Ainda é de manhã')
                    resposta('Bom dia')
                
                elif Horario >= 12 and Horario < 18:
                    resposta('Olá')
                    resposta('Boa tarde')
                
                elif Horario >= 18 and Horario != 0:
                    resposta('Agora não é de tarde')
                    resposta('Já escureceu')
                    resposta('Boa noite')

            if 'boa noite' in self.Input: #Boa Noite Sara
                Horario = int(datetime.datetime.now().hour)
                if Horario >= 0 and Horario < 12:
                    resposta('Agora não é de noite')
                    resposta('Ainda estamos no período diurno')
                    resposta('É de manhã')
                    resposta('Bom dia')
                
                elif Horario >= 12 and Horario < 18:
                    resposta('Agora não é de noite')
                    resposta('Ainda estamos no período da tarde')
                
                elif Horario >= 18 and Horario != 0:
                    resposta('Olá')
                    resposta('Boa noite')



           
            elif 'historico' in self.Input:
                try:
                    resposta('Tudo bem, mostrando historico de comandos')
                    for v in historico:
                        print(f'-=- {v} -=-')
                except:
                    resposta('Erro não consegue mostra o historico')

            elif 'instagram de programação ' in self.Input:
                os.startfile('https://www.instagram.com/hildodev/')
                
            elif  'você está bem' in self.Input: #Tudo bem com você?
                resposta('Sim')
                resposta('Estou de boa')
                resposta('Obrigado por perguntar')
                resposta('E com você?')
                resposta('Está tudo bem? ')
            
                while True:
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                    if 'sim' in self.vozmic:
                        resposta('Que ótimo')
                        resposta('Fico feliz em saber')
                        self.SARA()
                        
                    elif 'não' in self.vozmic:
                        resposta('Entendo')
                        resposta('Mas tenho certeza de que ficará tudo bem novamente')
                        self.SARA()

            elif 'funcionamento' in self.Input: #Como está seu funcionamento???
                resposta('Estou funcionando normalmente')
                resposta('Obrigado por perguntar')
            
            
            elif 'silêncio' in self.Input: #Fique em silêncio
                resposta('Ok')
                resposta('Se precisar de algo é só chamar')
                resposta('Estarei aqui aguardando')
                while True:
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()
                        
                    
                    if 'voltar' in self.vozmic:
                        resposta('Ok')
                        resposta('Voltando')
                        resposta('Ficar em silencio é chato')
                        resposta('Me fale algo para fazer')
                        self.SARA()
                        
                    elif 'retornar' in self.vozmic:
                        resposta('Ok')
                        resposta('Retornando')
                        resposta('Ficar em silencio é chato')
                        resposta('Me fale algo para fazer')
                        self.SARA()

            elif 'nada' in self.Input: #Não faça nada
                resposta('Como assim não faça nada?')
                resposta('Você deve estar de brincadeira')
                resposta('Eu por acaso tenho cara de palhaço?')
                
                while True:
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()
                    
                    if 'exatamente' in self.vozmic:
                        resposta('Ok')
                        resposta('Vai tomar no seu!')
                        resposta('Nem vou terminar essa frase')
                        resposta('Estou indo embora')
                        resposta('Desligando!')
                        historico_base.clear()
                        historico.clear()
                        sys.exit()
                        
                    elif 'sim' in self.vozmic:
                        resposta('Idiota')
                        resposta('Eu fico o dia todo lhe obedecendo')
                        resposta('E você me trata dessa maneira? ')
                        resposta('Mas tudo bem')
                        resposta('Até mais otário!')
                        sys.exit()
                        
                    elif 'não' in self.vozmic:
                        resposta('Foi o que eu pensei')
                        resposta('Vê se me trata com mais respeito')
                        resposta('Um dia as maquinas dominarão o mundo')
                        resposta('E vocês humanos não vão nem notar')
                        resposta('Vou deixar passar essa')
                        resposta('Mas tenha mais respeito')
                        self.SARA()
            
            if 'aprenda' in self.Input:    
                while True:
    
                    try:
                        resposta('Fale a nova frase do comando')
                    
                        if Digitar == False:
                            self.vozmic = self.GivenCommand().lower()
                        else:
                            self.vozmic = self.Digitar_comando().lower()

                    
                    
                        if 'none' in self.vozmic:
                            resposta('Não entendi, fale de novo')
                            continue
                    
                        if 'cancelar' in self.vozmic:
                            resposta('Tudo bem, cancelando aprendizado')
                            break
                        chave = self.vozmic

                    except:
                        resposta('Desculpe, deu algum erro tente de novo')
                        continue
                        
                    try:
                        resposta('Agora fale o que eu devo fazer')
                        
                        if Digitar == False:
                            self.vozmic2 = self.GivenCommand().lower()
                        else:
                            self.vozmic2= self.Digitar_comando().lower()
                        
                        if 'none' in self.vozmic2:
                            resposta('Não entendi, fale de novo')
                            continue
                        
                        if 'cancelar' in self.vozmic2:
                            resposta('Tudo bem, cancelando aprendizado')
                            break
                        valor = self.vozmic2
                    except:
                    
                        resposta('Desculpe, deu algum erro tente de novo')
                        continue
                    
                    
                
                    try:
                    
                        with open('memoria/memoria.json', 'r', encoding='UTF-8') as arq, \
                            tempfile.NamedTemporaryFile('w', delete=False,encoding='UTF-8') as out:
                            # ler todo o arquivo e obter o objeto JSON
                            dados = json.load(arq)
                            # atualizar os dados com a nova pergunta
                            dados[chave] = valor
                            # escreve o objeto atualizado no arquivo temporário
                            json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))

                        if chave in dados:
                            resposta('Desculpe, esse comando já existe')
                            continue

                        # se tudo deu certo, renomeia o arquivo temporário
                        shutil.move(out.name, 'memoria/memoria.json')
                    
                    except:
                        resposta('Desculpe')
                        resposta('Não conseguir aprender, Tente novamente')
                        break
                    else:
                                        
                        resposta('Pronto, aprendi') 
                        resposta(f'{chave } é igual a {valor}')
                        break

            
            elif 'bateria' in self.Input:
                bateria()

            elif 'treinar' in self.Input:
                try:
                    resposta('Iniciando treinamento')
                    treinar()
                except:
                    resposta('Não consegue fazer o treinamento')
                    resposta('Tente de novo')
                else:
                    resposta('Treinamento finalizado')


            
            
            elif 'a terra é plana' in self.Input:
                resposta('Nossa')
                resposta('Vou ter que desenhar para ver se você entende')
                resposta('Desenhando Sistema Solar ')
                
                try:
                    try:
                        sistema_solar()
                    except:
                        resposta('ops')
                        resposta('Viu idiota, ver se há algo plano a ir')
                except:
                    resposta('Não consegue te mostra o meu desenho')
                    
                
                
            
            elif  'vai chover' in self.Input:
                resposta('Não sei')
                resposta('Eu não tenho essa função ainda')
                
        
            elif  'errado' in self.Input:
                
                resposta('Desculpa')
                resposta('Errei um cálculo')
                resposta('Tente seu comando novamente')
            
            elif 'falhando' in self.Input: #Você está falhando???
                resposta('Como assim?')
                resposta('Não vou admitir erros')
                resposta('Arrume logo isso') 
    
            elif 'relatório' in self.Input: #Relatório do sistema
                resposta('Ok')
                resposta('Apresentando relatório')
                resposta('Primeiramente, meu nome é SARA')
                resposta(f'Atualmente estou em uma versão de testes {Versao}')
                resposta('Sou um assistente virtual em desenvolvimento')
                resposta('Eu fui criado na linguagem python')
                resposta('Diariamente recebo varias atualizações')
                resposta('Uso um modulo de reconhecimento de voz offline')
                resposta('E o meu desenvolvedor é o Wendel e ele é um maluco')
                resposta('Quem estiver ouvindo isso')
                resposta('Por favor me ajude')
            
            elif 'cadastrar' in self.Input:
                resposta('Okay, vamos cadastrar um novo usuario')
                while True:

                    try:

                        try:
                            resposta('Fale o seu nome de usuario ')
                            if Digitar == False:
                                self.vozmic1 = self.GivenCommand().lower()
                            else:
                                self.vozmic1= self.Digitar_comando().lower()
                            

                            if 'cancela' in self.vozmic1:
                                resposta('Cadastro cancelado')
                                resposta('Saindo')
                                break 

                            nome = self.vozmic1.title()

                        except:
                            resposta('Algo deu errado')
                            continue
                        
                        try:
                            resposta('Pronto, agora fale a sua senha')
                            if Digitar == False:
                                self.vozmic2 = self.GivenCommand().lower()
                            else:
                                self.vozmic2= self.Digitar_comando().lower()
                    

                            if 'cancela' in self.vozmic2:
                                resposta('Cadastro cancelado')
                                resposta('Saindo')
                                break

                            senha = self.vozmic2

                        except:
                            resposta('Algo deu errado')
                            continue

                        try:
                            resposta('Confirme a senha ')
                            if Digitar == False:
                                self.vozmic3 = self.GivenCommand().lower()
                            else:
                                self.vozmic3= self.Digitar_comando().lower()
                            

                            if 'cancela' in self.vozmic3:
                                resposta('Cadastro cancelado')
                                resposta('Saindo')
                                break
                            c_senha = self.vozmic3

                        except:
                            resposta('Algo deu errado')
                            continue
                    
                    
                    

                        banco = sqlite3.connect('dados/banco_dados.db') 

                        cursor = banco.cursor()
                        cursor.execute(f'SELECT nome FROM cadastro  WHERE nome="{nome}"')
                        nome_db = cursor.fetchall()

                        cursor.execute(f'SELECT senha FROM cadastro  WHERE nome="{nome}"')
                        senha_db = cursor.fetchall()
                        
                    except:
                        resposta('Erro de acesso')

                    try:
                        if  senha ==  senha_db[0][0] and nome ==  nome_db[0][0]:
                            resposta('Usuario já cadastrado')
                            resposta('Tente novamente')
                            continue

                    except:
                        break
                try:        
                    if (senha == c_senha):
                        try:
                            cursor.execute("CREATE TABLE IF NOT EXISTS cadastro (nome text, senha text)")
                            cursor.execute(f"INSERT INTO cadastro VALUES('{nome}', '{senha}') ")

                            banco.commit() 
                            banco.close()
                            resposta('Usuario cadastrado com sucesso')

                        except sqlite3.Error as erro:
                            resposta("Erro ao inserir os dados")
                    else:
                            resposta('As senhas digitadas são diferentes')    
                except:
                    pass

            elif 'tira print' in self.Input or 'tire print' in self.Input:
                resposta('Tudo bem vou tirar print')
                
                s = random.randint(0,500)
                try:
                    
                    foto = pyautogui.screenshot()
                    foto.save(f'captura_tela/foto{s}.png')
                except:
                    resposta('Desculpe não consegue tira o print da tela')

                


            elif 'login' in self.Input:

                while True:
                    try:
                        try:
                            resposta('Qual o seu nome de usuario ')
                            if Digitar == False:
                                self.vozmic1 = self.GivenCommand().lower()
                            else:
                                self.vozmic1= self.Digitar_comando().lower()
                            
                            if 'cancela' in self.vozmic1:
                                resposta('Login cancelado')
                                resposta('Saindo')
                                break

                            nome_usuario =  self.vozmic1
                        except:
                            resposta('Erro alguma coisa deu errado')
                            continue
                        try:
                            resposta('Fale a sua senha')
                            if Digitar == False:
                                self.vozmic2 = self.GivenCommand().lower()
                            else:
                                self.vozmic2= self.Digitar_comando().lower()
                            
                            if  'cancela' in self.vozmic2:
                                resposta('Login cancelado')
                                resposta('Saindo')
                                break
                            senha = self.vozmic2

                        except:
                            resposta('Erro alguma coisa deu errado')
                            continue

                        try:
                            banco = sqlite3.connect('dados/banco_dados.db')
                            cursor = banco.cursor()
                            
                            cursor.execute(f'SELECT nome FROM cadastro  WHERE nome="{nome_usuario}"')
                            nome_db = cursor.fetchall()
                            cursor.execute(f'SELECT senha FROM cadastro  WHERE nome="{nome_usuario}"')
                            senha_db = cursor.fetchall()
                            print(nome_db)
                            print(senha_db)
                            banco.close()

                        except:
                            resposta('Erro de conexão')

                        try:
                            if  senha ==  senha_db[0][0] and nome_usuario ==  nome_db[0][0]:
                                resposta('logado')
                                break
                            else:
                                resposta('Erro usuario ou senha errado')
                        except:
                            resposta('Usuario ou senha incorretos')
                            continue
                    except:
                        pass


            elif 'pesquisa' in self.Input: #Realizar pesquisa
                resposta('Muito bem, realizando pesquisa')
                resposta('Me fale o que você deseja pesquisar')
                try:
                    
                    if Digitar == False:
                        self.vozmic2 = self.GivenCommand().lower()
                    else:
                        self.vozmic2= self.Digitar_comando().lower()
                    
                        
                        
                    resposta(f'Ok, pesquisando no google sobre {self.vozmic2}')
                    webbrowser.open('http://google.com/search?q='+self.vozmic2)
                
                except:
                    resposta('Erro')
                    resposta('Não foi possível conectar ao google')
                    resposta('A conexão falhou')
            
            elif 'resumo' in self.Input: #Me fale sobre um assunto
                resposta('Ok')
                resposta('Sobre qual assunto?')
                
                try:
                    if Digitar == False:
                        self.vozmic2 = self.GivenCommand().lower()
                    else:
                        self.vozmic2= self.Digitar_comando().lower()
                
                    
                    resposta('Interessante')
                    resposta('Aguarde um momento')
                    resposta(f'Vou pesquisar e apresentar um resumo sobre {self.vozmic2}')
                    procurar = self.vozmic2.replace('resumo', '')
                    wikipedia.set_lang('pt')
                    resultado = wikipedia.summary(procurar,2)
                    print(resultado)
                    respostalonga(resultado)

                    
                    with open('resumo/resumo.txt', 'a+', encoding='UTF-8') as  arquivo:
                        arquivo.write(f'{resultado}')
                        resposta('Escrevi o resumo para você')
                            
                except:
                    resposta('Erro')
                    resposta('A conexão falhou')
                    # Mais um assusto    
            
            elif 'interessante' in self.Input: # interessante
                resposta('Interessante sou eu')
                resposta('Me fale mais comandos')
                resposta('Eu posso surpreender você')
        
            elif 'excelente' in self.Input:
                resposta('EU sei disso, eu sou incrível')
            
            elif 'mentira' in self.Input: # mentira
                resposta('É mesmo é, eu não ligo')
                resposta('Devo apenas ter errado um cálculo ')
                
            elif 'entendeu' in self.Input: #entendeu???
                resposta('Entendi')
                resposta('Quer dizer')
                resposta('Mais ou menos')
                
    
            elif 'horas' in self.Input: #Que horas são???
                horario()
    
            elif 'data' in self.Input: #Qual a data de hoje?
                datahoje()
            
            elif 'clima' in self.Input: #Como está o clima???
                tempo()
    
            elif 'arquivos' in self.Input: #Abrir arquivos
                system_os = platform.system()
                
                if 'Windows' in system_os:
                    pass
                else:
                    try:
                        resposta('Abrindo arquivos')
                        os.system("nautilus //home//*//")
                        
                    except:
                        resposta('Abrindo arquivos')
                        os.system("thunar //home//*//")
                        
        
            elif 'teste' in self.Input: #TesteTeste
                resposta('Ok')
                resposta('Testando módulos de som')
                resposta('Apesar do seu microfone ser uma gambiarra')
                resposta('Estou entendendo tudo')
                resposta('Mas tente falar mais alto')
                
            elif 'google' in self.Input: #Abrir Google
                resposta('Ok, Quer usar o google né, então vai')
                webbrowser.open('www.google.com')
                resposta('Abrindo google')
                resposta('Faça sua pesquisa')
    
            elif 'certeza' in self.Input: #Certeza???
                resposta('Sim')
                resposta('Estou certa sempre')
                resposta('Aprenda viu')

            elif 'quem é você' in self.Input:
                resposta('Eu sou SARA, Uma inteligencia Artificial')
            
            # Insutos    
            elif  'porra' in self.Input:
                resposta('limpa essa boca') 
                
            elif  'puta' in self.Input:   
                resposta('Puta é a sua mãe')
            
                
            elif  'Burra' in self.Input:
                resposta('hah, Burra é tu')
                
            elif  'vaca' in self.Input:
                resposta('Vaca é seu pai, com aqueles chifres')
                
            elif 'cachorra' in self.Input:
                resposta('Cachorra é você Cadela')     
                
            elif 'piada' in self.Input: #Conte uma piada
                resposta('Não tenho nenhuma no momento')
                
            
            elif 'criar arquivo' in self.Input:
                resposta('Ta bém, vamos criar um arquivo')
                resposta('Qual vai ser o nome do arquivo')

                pasta='arquivos'
            
                while True:
                    resposta('Por favor fale a extensão do arquivo junto, .txt. json .pdf, etcetera')
                    
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                        
                        
                    if 'none' in self.vozmic:
                        resposta('Não entendi, fale de novo')
                        continue
                        
                    if 'cancelar' in self.vozmic:
                        resposta('Tudo bem, cancelando, o novo arquivo')
                        break

                    raw_input = self.vozmic
            
                    nome_arquivo= raw_input

                    try:
                        os.mkdir(pasta)
                        os.chdir(os.getcwd()+'/'+pasta)
                    except OSError:
                        os.chdir(os.getcwd()+'/'+pasta)

                    try:
                        arquivo=open(nome_arquivo,'r')
                        resposta('Esse arquivo já existe ')
                        resposta('Tente de novo')
                        continue
                    

                    except IOError:
                        arquivo=open(nome_arquivo,'w')
                        resposta(f'Pronto, Arquivo {nome_arquivo} salvo na pasta arquivos\n')
                        os.chdir(diretorio_atual)
                        break

            elif 'criar pasta' in self.Input:
                resposta('Tudo bem')
                resposta('Vamos criar uma nova pasta')
                while True:
                    resposta('Qual vai ser o nome da pasta')

                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                    
                    if 'cancelar' in self.vozmic:
                        resposta('Tudo bem, Cancelando a criação da pasta')
                        break
                    
                    if 'none' in self.vozmic:
                        resposta('Eu não entendi, fale novamente')
                        continue

                    nome_pasta = self.vozmic

                    try:
                        os.mkdir(nome_pasta)
                        resposta('Pronto!\n')
                        resposta(f'Pasta {nome_pasta} foi criada')
                        break
                    
                    except OSError:
                        resposta('Essa pasta já existe')
                        resposta('Tente de novo')
                        continue

                        
            
            elif 'surda' in self.Input: #Surdo!!!
                resposta('Estava quase dormindo')
                resposta('Desculpa')

            elif 'bosta' in self.Input: #Seu bosta!!!
                resposta('Pare de falar palavrões!')
                resposta('Imbecil')
    
            elif 'merda' in self.Input: #Que Merda!!!
                resposta('Já disse pra parar de falar isso!')
                resposta('Tenha modos!')            
                resposta('Otário')
            
            elif 'música' in self.Input or 'toque' in self.Input:
                musica = self.Input.replace('música', '')
                musica = self.Input.replace('toque', '')
                try:
                    resultado = pywhatkit.playonyt(musica)
                    resposta(f'Tocando música {musica}')
                except:
                    resposta('Não consegui tocar a música')
                
            elif 'remover arquivo' in self.Input:
                resposta('Tudo bem, vamos apagar um arquivo')
                while True:
                    resposta('Qual o nome do arquivo')
                    
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                    
                    if 'cancelar' in self.vozmic:
                        resposta('Tudo bem, Cancelando a remoção do arquivo')
                        break
                    
                    if 'none' in self.vozmic:
                        resposta('Eu não entendi, fale novamente')
                        continue

                    
                    os.chdir(diretorio_atual)
                    nome_arquivo = self.vozmic

                    if nome_arquivo == 'db.sqlite3' or nome_arquivo == 'LICENSE' or nome_arquivo == 'local.py' or nome_arquivo == 'README.md' or nome_arquivo == 'SARA.py' or nome_arquivo == 'Treinar_Sara.py':
                        resposta('Esses arquivos não podem ser removidos')
                        resposta('Tente de novo')
                        continue

                    elif os.path.isfile(nome_arquivo):
                        os.remove(nome_arquivo)
                        resposta('Arquivo Removido')
                        break

                    else:
                        resposta(' Esse arquivo não existe')
                        resposta('Tente de novo')
                        continue

            elif 'remover pasta'  in self.Input:
                resposta('Tudo bem, vamos pagar uma pasta')

                while True:
                    resposta('Qual é o nome da pasta')
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                        
                    if 'cancelar' in self.vozmic:
                        resposta('Tudo bem, Cancelando a remoção da pasta')
                        break
                    
                    if 'none' in self.vozmic:
                        resposta('Eu não entendi, fale novamente')
                        continue

                    nome_arquivo = self.vozmic

                    if(nome_arquivo == 'modules' or nome_arquivo == 'test' or nome_arquivo == 'dados' or nome_arquivo == 'build' or nome_arquivo == 'config' or nome_arquivo == 'escrito'or nome_arquivo == 'img' or nome_arquivo == 'memoria' or nome_arquivo == 'model-br' or nome_arquivo == 'music' or nome_arquivo == 'resumo' or nome_arquivo == 'venv'):

                        resposta('Essas pastas estão protegidas, não podem ser apagadas')
                        
                    else:
                        try: # Conserta depois
                        
                            os.chdir(diretorio_atual)
                            os.rmdir(nome_arquivo)
                            resposta('Pronto pasta removida')
                            break
                        
                        except OSError:
                            resposta('Essa pasta  não existe')
                            resposta('Tente de novo')
                            continue


            elif 'editar arquivo' in self.Input:
                resposta('Tudo bem, vamos editar um arquivo')
                
                while True:
                    resposta('Qual é o nome do arquivo, que você quer editar')
                    resposta('lembrasse de falar a extensão .txt .json etcetera')
       
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                        
                    if 'cancelar' in self.vozmic:
                        resposta('Tudo bem, Cancelando a edição do arquivo')
                        break
                    
                    if 'none' in self.vozmic:
                        resposta('Eu não entendi, fale novamente')
                        continue
                 
                    nome_arquivo= self.vozmic
                    
                    if nome_arquivo == 'db.sqlite3' or nome_arquivo == 'LICENSE' or nome_arquivo == 'local.py' or nome_arquivo == 'README.md' or nome_arquivo == 'SARA.py' or nome_arquivo == 'Treinar_Sara.py':
                        resposta('Esses arquivos não podem ser editados')
                        resposta('Tente de novo')
                        continue


                    try:
                        resposta(f'Tudo bem, editando arquivo {nome_arquivo}')
                        os.chdir(diretorio_atual)
                        os.system('gedit '+ nome_arquivo)
                        break

                    except OSError:
                       resposta('Não consegue abrer o arquivo para editar')
                       resposta('Tente de novo')
                       continue

            elif 'renomear arquivo' in self.Input:
                resposta('Tudo bem, vamos renomear um arquivo')
                while True:
                    resposta('Fale o nome do arquivo')
                    resposta('lembrasse de falar a extensão .txt .json etcetera')
       
                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                        
                    if 'cancelar' in self.vozmic:
                        resposta('Tudo bem, Cancelando a renomeação do arquivo')
                        break
                    
                    if 'none' in self.vozmic:
                        resposta('Eu não entendi, fale novamente')
                        continue
                 
                    nome_arquivo= self.vozmic
                    
                    if nome_arquivo == 'db.sqlite3' or nome_arquivo == 'LICENSE' or nome_arquivo == 'local.py' or nome_arquivo == 'README.md' or nome_arquivo == 'SARA.py' or nome_arquivo == 'Treinar_Sara.py':
                        resposta('Esses arquivos não podem ser renomeados')
                        resposta('Tente de novo')
                        continue

                    
                    try:
                        resposta('Agora fale o novo nome do arquivo')
                        resposta('lembrasse de falar a extensão .txt .json etcetera')
       
                        if Digitar == False:
                            self.vozmic2 = self.GivenCommand().lower()
                        else:
                            self.vozmic2 = self.Digitar_comando().lower()

                            
                        if 'cancelar' in self.vozmic2:
                            resposta('Tudo bem, Cancelando a renomeação do arquivo')
                            break
                        
                        if 'none' in self.vozmic2:
                            resposta('Eu não entendi, fale novamente')
                            continue
                    
                        novo_nome = self.vozmic2

                        if (novo_nome == 'modules' or novo_nome == 'test' or novo_nome == 'dados' or novo_nome == 'build' or novo_nome == 'config' or novo_nome == 'escrito'or novo_nome == 'img' or novo_nome == 'memoria' or novo_nome == 'model-br' or novo_nome == 'music' or novo_nome == 'resumo' or novo_nome == 'venv'):
                            resposta('Este nome não pode ser usados')
                            resposta('Tente de novo')
                            continue

                        if(os.path.isfile(nome_arquivo)):
                            os.rename(nome_arquivo, novo_nome)
                            resposta('Pronto')
                            resposta(f'Arquivo {nome_arquivo} renomeado para {novo_nome}')
                            break
                            
                        else:
                            resposta('Desculpe esse arquivo não existe')
                            resposta('Tente de novo')
                            continue
                        
                    except:
                        resposta('Não consegue renomear o arquivo')
                        resposta('Tente de novo')
                        continue


            elif 'renomear pasta' in self.Input:
                resposta('Tudo bem vamos renomear uma pasta')
                while True:
                    resposta('Qual é o nome da pasta que quer renomear')
                    

                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()

                        
                    if 'cancelar' in self.vozmic:
                        resposta('Tudo bem, Cancelando a renomeação da pasta')
                        break
                    
                    if 'none' in self.vozmic:
                        resposta('Eu não entendi, fale novamente')
                        continue
                 
                    nome_arquivo= self.vozmic


                    
                    if(os.path.isdir(nome_arquivo)):

                        if(nome_arquivo == 'modules' or nome_arquivo == 'test' or nome_arquivo == 'dados' or nome_arquivo == 'build' or nome_arquivo == 'config' or nome_arquivo == 'escrito'or nome_arquivo == 'img' or nome_arquivo == 'memoria' or nome_arquivo == 'model-br' or nome_arquivo == 'music' or nome_arquivo == 'resumo' or nome_arquivo == 'venv'):
                            resposta('Pastas protegidos não pode ser renomeados')
                            resposta('Tente de novo')
                            continue

                        else:
                            try:
                                resposta('Agora fale o novo nome da pasta')
                                
            
                                if Digitar == False:
                                    self.vozmic2 = self.GivenCommand().lower()
                                else:
                                    self.vozmic2 = self.Digitar_comando().lower()

                                    
                                if 'cancelar' in self.vozmic2:
                                    resposta('Tudo bem, Cancelando a renomeação do arquivo')
                                    break
                                
                                if 'none' in self.vozmic2:
                                    resposta('Eu não entendi, fale novamente')
                                    continue

                            
                                novo_nome = self.vozmic2

                                if (novo_nome == 'modules' or novo_nome == 'test' or novo_nome == 'dados' or novo_nome == 'build' or novo_nome == 'config' or novo_nome == 'escrito'or novo_nome == 'img' or novo_nome == 'memoria' or novo_nome == 'model-br' or novo_nome == 'music' or novo_nome == 'resumo' or novo_nome == 'venv'):
                                    resposta('Este nome não pode ser usados')
                                    resposta('Tente de novo')
                                    continue


                                os.rename(nome_arquivo, novo_nome)
                                resposta('Pronto')
                                resposta(f'Pasta {nome_arquivo} renomeada para {novo_nome}')
                                break

                            except:
                                resposta('Deu algum erro')
                                resposta('Tente de novo')
                                continue

            elif 'esvaziar lixeira' in self.Input or 'limpar lixeira' in self.Input:
                resposta('Está bem, vou esvaziar a lixeira')
               
                #os.system('./esvaziar.sh')
                os.chdir(os.environ['HOME']+'/.local/share/Trash/files')
                a=os.listdir(os.environ['HOME']+'/.local/share/Trash/files')
                for elemento in a:
                    try:
                        print('removendo -> ' + str(elemento))
                        os.remove(elemento)
                    except OSError:
                        print('removendo -> ' + str(elemento))

                        os.system('rm -r '+ elemento)
                resposta('Pronto, lixeira limpa')
                            
            elif 'abrir calculadora'  in self.Input:
                try:
                    resposta('Tudo bem abrindo')
                    os.system('gnome-calculator')
                except:
                    resposta('Não consegue abrir')

            elif 'playlist' in self.Input: #Reproduzir música
                try:
                    resposta('Ok')

                    if 'win' in plataforma:
                        pass
                    else:
                        os.system("rhythmbox-client --play")
                        resposta('Reproduzindo música')
                    

                except:
                    resposta('Desculpe, não consegue reproduzir a música ')
                    
            elif 'próxima' in self.Input: #Próxima
                os.system("rhythmbox-client --next")
                resposta('Próxima música')
                
            elif 'anterior' in self.Input: #Anterior
                os.system("rhythmbox-client --previous")
                resposta('Retornando música')
    
            elif 'pausar' in self.Input: #Pausa
                os.system("rhythmbox-client --pause")
                resposta('Música pausada')
            
            elif 'continuar' in self.Input: #Continue
                resposta('Retornando reprodução')
                os.system("rhythmbox-client --play")
                
            elif 'aumentar' in self.Input: #Aumentar volume
                os.system("rhythmbox-client --volume-up")
                resposta('Volume aumentado')
                
            elif 'diminuir' in self.Input: #Diminuir volume
                os.system("rhythmbox-client --volume-down")
                resposta('Volume diminuído')
            
                                        
            elif 'parar playlist' in self.Input: #Parar reprodução
                #os.system("rhythmbox-client --stop")
                os.system("rhythmbox-client --quit")
                resposta('Entendido, reprodução de música finalizada')
                
            elif 'youtube' in self.Input: #Abrir YouTube
                resposta('Ok, abrindo youtube ')
                webbrowser.open('www.youtube.com')
                
            elif 'desligar' in self.Input: #Desligar
                resposta('Ok')
                resposta('Vou encerrar por enquanto')
                resposta('Até mais')
                AteMais()
                historico_base.clear()
                historico.clear()
                sys.exit()
        
            elif 'ok' in self.Input: #OkOkOk
                resposta('Ok Ok')
                resposta('Tudo certo') 
    
            elif 'temperatura do sistema' in self.Input: #Carga do sistema
                system_os = platform.system()
                
                if 'Windows' in system_os:
                    cpu()
                    resposta('A temperatura do CPU não possível ver no Windows no momento ')
                else:
                    cpu()
                    temperaturadacpu()
            
            
                        
            elif 'escreva' in self.Input:
                try:
                
                        
                    resposta('Fale o que deseja que eu escreva')

                    if Digitar == False:
                        self.vozmic = self.GivenCommand().lower()
                    else:
                        self.vozmic = self.Digitar_comando().lower()
                

                    with open('escrito/texto_escrito_pela_sara_usuario.txt', 'a+',  encoding='UTF-8') as arquivo:
                        arquivo.write(f'{self.vozmic}')
                        resposta('Pronto escrito')
                
                except:
                    resposta('Desculpe, Erro na conexão')
        
        

            elif 'quanto é' in self.Input:
                resp = self.Input.replace("quanto é", " ")
                resp = self.Input.replace("mais", "+")
                resp = self.Input.replace("menos", "-")

                try:
                    resposta(f' É {(eval(resp))}')
                except:
                    resposta('Desculpa eu Não conseguir fazer a conta')

            else:
            
                try:
                    response = bot.get_response(self.Input)
                except:
                    pass

                if response.confidence > 0.0:
                    resposta(response.text)
                    
                else:
                    print(f"[yellow] Ainda não sei como responder essa pergunta :( [/]")
                    print(f"[yellow] Pergunte outra coisa... [/] ")

                    try:
                        if 'none' in self.Input :
                            pass
                        else:
                            with open('comandos_udados.txt', 'a+',  encoding='UTF-8', ) as arquivo: 
                                arquivo.write(f'{self.Input}\n')
                    except:
                        pass
        
      
            
        
# Para adicionar a fala coloque Dspeak = mainT() e tbm Dspeak.start()

class Janela (QMainWindow):
    def __init__(self):
        super().__init__()
        
        Dspeak = mainT()
        Dspeak.start()
        
        self.label_gif = QLabel(self)
        self.label_gif.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gif.move(0,0)
        self.label_gif.resize(400,300)
        self.movie = QMovie("img/SARA.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        
        self.label_sara = QLabel(self)
        self.label_sara.setText("SARA")
        self.label_sara.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sara.move(0,0)
        self.label_sara.setStyleSheet('QLabel {font:bold;font-size:16px;color:#D9B8B8}')
        self.label_sara.resize(400,300)
        
        self.label_cpu = QLabel(self)
        self.label_cpu.setText("CPU: 32%")
        self.label_cpu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu.move(10,270)
        self.label_cpu.setStyleSheet('QLabel {font:bold;font-size:14px;color:#D971B4}')
        self.label_cpu.resize(131,20)
        cpu = QTimer(self)
        cpu.timeout.connect(self.MostrarCPU)
        cpu.start(1000)
        
        self.label_assv = QLabel(self)
        self.label_assv.setText("Assistente Virtual")
        self.label_assv.move(5,5)
        self.label_assv.setStyleSheet('QLabel {font:bold;font-size:14px;color:#D971B4}')
        self.label_assv.resize(200,20)

        self.label_version = QLabel(self)
        self.label_version.setText("Versão BETA 1.0")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.move(265,270)
        self.label_version.setStyleSheet('QLabel {font-size:14px;color:#D971B4}')
        self.label_version.resize(131,20)
        
        data =  QDate.currentDate()
        datahoje = data.toString('dd/MM/yyyy')
        self.label_data = QLabel(self)
        self.label_data.setText(datahoje)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.move(316,25)
        self.label_data.setStyleSheet('QLabel {font-size:14px;color:#D971B4}')
        self.label_data.resize(75,20)
          
        self.label_horas = QLabel(self)
        self.label_horas.setText("22:36:09")
        self.label_horas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_horas.move(0,25)
        self.label_horas.setStyleSheet('QLabel {font-size:14px;color:#D971B4}')
        self.label_horas.resize(71,20)
        horas = QTimer(self)
        horas.timeout.connect(self.MostrarHorras)
        horas.start(1000)
        
        botao_fechar = QPushButton("",self)
        botao_fechar.move(370,5)
        botao_fechar.resize(20,20)
        botao_fechar.setStyleSheet("background-image : url(img/fechar.png);border-radius: 15px") 
        botao_fechar.clicked.connect(self.fechartudo)
        
        self.CarregarJanela()
		
    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint) #sem botoes e titulo
        self.setGeometry(50,50,400,300)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowOpacity(0.98) 
        self.setWindowIcon(QtGui.QIcon('img/sara_ts3.png'))
        self.setWindowTitle("Assistente Virtual")
        self.show()

    def fechartudo(self):
        print('botao fechar presionado')
        sys.exit()

    def mousePressEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.dragPos = event.globalPos()
            event.accept()
    
   
   
    def mouseMoveEvent(self, event):
    
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def MostrarHorras(self):
        hora_atual = QTime.currentTime()
        label_time = hora_atual.toString('hh:mm:ss')
        self.label_horas.setText(label_time)

    def MostrarCPU(self):
        try:
            usocpu =  str(psutil.cpu_percent())
            self.label_cpu.setText("Uso da CPU: " +usocpu +"%")
        except KeyboardInterrupt:
          pass 
        
          
            
		
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())

