from inspect import Traceback
from ipaddress import NetmaskValueError
from traceback import TracebackException
from vosk import Model, KaldiRecognizer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from plyer import notification
from rich import print
from rich.table import Table
from build import sistema_solar

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
import logging
import sqlite3

try:
    import pywhatkit
except:
    ...
plataforma = platform.system()

r= sr.Recognizer()

def SomIncial():
    p = vlc.MediaPlayer("music/StartSound.mp3")
    p.play()

SomIncial()

def SomCarregamento():
    p = vlc.MediaPlayer("music/AI.mp3")
    p.play()

# Validacao da pasta de modelo
# É necessario criar a pasta model-br a partir de onde estiver esta fonte
if not os.path.exists("model-br"):
    print ("Modelo em portugues nao encontrado.")
    exit (1)

# Preparando o microfone para captura
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()

# Apontando o algoritmo para ler o modelo treinado na pasta "model-br"
model = Model("model-br")
rec = KaldiRecognizer(model, 16000)

if 'Windows' in plataforma:
    # Trás a função letícia voz
    sara_voz=pyttsx3.init('sapi5')

    # Função de ajuste de voz da sara
    voz = sara_voz.getProperty('voices')
    sara_voz.setProperty('voice', voz[2].id)
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)
else:
    # Trás a função letícia voz
    sara_voz=pyttsx3.init()

    # Função de ajuste de voz da sara
    voz = sara_voz.getProperty('voices')
    sara_voz.setProperty('voice', 'brasil')
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)



# Função de fala sara (voz da letícia)   
def resposta(audio):
    # notification.notify(title = "SARA",message = audio,timeout = 3)
    stream.stop_stream ()
    print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
    sara_voz.say(audio)
    sara_voz.runAndWait()
    stream.start_stream ()

def notificar(textos):
	# notification.notify(title = "SARA",message = textos,timeout = 10)
    pass
def respostalonga(textofala):
    
    stream.stop_stream ()
    sara_voz.say(textofala)
    sara_voz.runAndWait()
    stream.start_stream ()

def horario():
	from datetime import datetime
	hora = datetime.now()
	horas= hora.strftime('%H horas e %M minutos')
	resposta(f'Agora são {horas}')
    

def datahoje():
    from datetime import date
    dataatual = date.today()
    diassemana = ('Segunda-feira','Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sábado','Domingo')
    meses = ('Zero','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro')
    resposta(f"Hoje é {diassemana[dataatual.weekday()]}")
    diatexto = f'{dataatual.day} de '
    mesatual = (meses[dataatual.month])
    datatexto = dataatual.strftime(" de %Y")
    resposta(f'Dia {diatexto} {mesatual} {datatexto}')

def bateria(): # No momento funcionameto em notebook
    try:
        bateria = psutil.sensors_battery()
        carga = bateria.percent
        bp = str(bateria.percent)
        bpint = "{:.0f}".format(float(bp))
        resposta(f"A bateria está em: {bpint}%")
        if carga <= 20:
            resposta('Ela está em nivel crítico')
            resposta('Por favor, coloque o carregador')
        elif carga == 100:
            resposta('Ela está totalmente carregada')
            resposta('Retire o carregador da tomada')
    except:
        resposta(f'Não foi possivel dizer a bateria')

def cpu ():
    usocpuinfo = str(psutil.cpu_percent())
    usodacpu  = "{:.0f}".format(float(usocpuinfo))
    resposta('Verificando carga do sistema')
    resposta(f'O uso do processador está em {usodacpu}%')

def temperaturadacpu():
    tempcpu = psutil.sensors_temperatures(fahrenheit=False)
    cputemp = tempcpu['coretemp'][0]
    temperaturacpu = cputemp.current
    cputempint = "{:.0f}".format(float(temperaturacpu))
    resposta(f'A temperatura da CPU está em {cputempint}° ')

# função de boas vindas, fases do dia
def BoasVindas():
    Horario = int(datetime.datetime.now().hour)
    if Horario >= 0 and Horario < 12:
        resposta('Bom dia')

    elif Horario >= 12 and Horario < 18:
        resposta('Boa tarde')

    elif Horario >= 18 and Horario != 0:
        resposta('Boa noite')
	
def tempo(): 
    try:
        #Procure no google maps as cordenadas da sua cidade e coloque no "lat" e no "lon"(Latitude,Longitude)
        api_url = "https://fcc-weather-api.glitch.me/api/current?lat=14º 13 30&lon=42º 46 53"
        data = requests.get(api_url)
        data_json = data.json()
        if data_json['cod'] == 200:
            main = data_json['main']
            wind = data_json['wind']
            weather_desc = data_json['weather'][0]
            temperatura =  str(main['temp'])
            tempint = "{:.0f}".format(float(temperatura))
            vento = str(wind['speed'])
            ventoint = "{:.0f}".format(float(vento))
            dicionario = {
                'Rain' : 'chuvoso',
                'Clouds' : 'nublado',
                'Thunderstorm' : 'com trovoadas',
                'Drizzle' : 'com garoa',
                'Snow' : 'com possibilidade de neve',
                'Mist' : 'com névoa',
                'Smoke' : 'com muita fumaça',
                'Haze' : 'com neblina',
                'Dust' : 'com muita poeira',
                'Fog' : 'com névoa',
                'Sand' : 'com areia',
                'Ash' : 'com cinza vulcanica no ar',
                'Squall' : 'com rajadas de vento',
                'Tornado' : 'com possibilidade de tornado',
                'Clear' : 'com céu limpo'
                }
            tipoclima =  weather_desc['main']
            if data_json['name'] == "Shuzenji":
                resposta('Erro')
                resposta('Não foi possivel verificar o clima')
                resposta('Tente novamente o comando')
            else:
                resposta(f'Verificando clima para a cidade de {data_json["name"]}')
                resposta(f'O clima hoje está {dicionario[tipoclima]}')
                resposta(f'A temperatura é de {tempint}°')
                resposta(f'O vento está em {ventoint} kilometros por hora')
                resposta(f'E a umidade é de {str(main["humidity"])}%')
    
    except: 
        resposta('Não foi possivel realizar essa tarefa')
        resposta('Erro na conexão')

def AteMais():
    Horario = int(datetime.datetime.now().hour)
    if Horario >= 0 and Horario < 12:
        resposta('Tenha um ótimo dia')

    elif Horario >= 12 and Horario < 18:
        resposta('Tenha uma ótima tarde')

    elif Horario >= 18 and Horario != 0:
        resposta('Boa noite')

def linha_sara(): # Linha para menu
   
    
    #Tabela Sara >> 
    table = Table(title='----> SARA <----', title_justify='center', title_style='blue')
    
    table.add_column('Informação', justify='center', style='purple')
    table.add_column('Versão', justify='center', style='red')
    table.add_column('Suporte', justify='center', style='green')
    
    #Adicionar linhas nas colunas >> 
    table.add_row('Sara, assistente virtual pessoal', '--Beta v1.0--   Compativel: Windows >> Sim;   linux >> Sim(Beta);   Mac >> Em breve  ',  'Contado: Telegram >> https://t.me/Lasstll')
    
    print(table)
    
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
        try:
            try:
                import pywhatkit
            except:
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
                    # resposta("Não entendi o que você disse, fale novamente.")
                    return 'none'
                #Input = Input.lower()
                return Input
            
        #   Input = rec.Result()
            with sr.Microphone() as s:
                r.adjust_for_ambient_noise(s)
                audio = r.listen(s)
                speech = r.recognize_google(audio, language= "pt-BR")
            '''try:
                with sr.Microphone() as s:
                    audio = vozes.listen(s)
                    speech2 = vozes.recognize_google(audio, language= "pt-BR")
                
                
                    speech = speech2.lower()
                    
                    try:
                    with sr.Microphone() as s:
                        r.adjust_for_ambient_noise(s)
                        audio = r.listen(s)
                        speech = r.recognize_google(audio, language= "pt-BR")
                    
                    '''
    
        except:
            # Retorna os erros
            print('Não entendi, fale novamente33')
            # resposta("Não entendi o que você disse, fale novamente.")
            return 'none'
        #Input = Input.lower()
        return speech
    

            
    # Comandos e conversas   
    def SARA(self):
        while True:
            self.Input = self.GivenCommand().lower()
            
            BASE_DIR = os.path.dirname(__file__)
            SAVE_TO = os.path.join(BASE_DIR, 'mente.json')

            with open('memoria/memoria.json', 'r',) as file:
                self.comandos = json.load(file)
                

            
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

            elif 'olá' in self.Input: #Olá Sara
                resposta('Olá')
                resposta('Estou aqui')
                resposta('Precisa de algo?')
	         
            elif 'ideia' in self.Input: #Alguma ideia???
                resposta('No momento nenhuma')
                resposta('Mas tenho certeza de que voçê vai pensar em algo')

            elif 'instagram de programação ' in self.Input:
                os.startfile('https://www.instagram.com/hildodev/')
                
            elif  'tudo bem' in self.Input: #Tudo bem com voçê?
                resposta('Sim')
                resposta('Estou de boa')
                resposta('Obrigado por perguntar')
                resposta('E com voçê?')
                resposta('Está tudo bem? ')
                while True:
                    self.vozmic = self.GivenCommand()
 
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
                     self.vozmic = self.GivenCommand()
                    
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
                resposta('Voçê deve estar de brincadeira')
                resposta('Eu por acaso tenho cara de palhaço?')
                while True:
                    self.vozmic = self.GivenCommand()
                    
                    if 'exatamente' in self.vozmic:
                        resposta('Ok')
                        resposta('Vai tomar no seu!')
                        resposta('Nem vou terminar essa frase')
                        resposta('Estou indo embora')
                        resposta('Desligando!')
                        sys.exit()
                        
                    elif 'sim' in self.vozmic:
                        resposta('Idiota')
                        resposta('Eu fico o dia todo lhe obedeçendo')
                        resposta('E voçê me trata dessa maneira? ')
                        resposta('Mas tudo bem')
                        resposta('Até mais otário!')
                        sys.exit()
                         
                    elif 'não' in self.vozmic:
                        resposta('Foi o que eu pensei')
                        resposta('Vê se me trata com mais respeito')
                        resposta('Um dia as maquinas dominarão o mundo')
                        resposta('E voçês humanos não vão nem notar')
                        resposta('Vou deixar passar essa')
                        resposta('Mas tenha mais respeito')
                        self.SARA()
            
            if 'aprenda' in self.Input:    
                while True:
    
                    try:
                        resposta('Fale a nova frase do comando')
                        
                        self.vozmic = self.GivenCommand()
                        
                        chave = self.vozmic

                    except:
                        resposta('Desculpe, deu algum erro tente de novo')
                        continue
                        
                    try:
                        resposta('Agora fale o que eu devo fazer')
                        self.vozmic2 = self.GivenCommand()
                        
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
                   
            elif self.Input in self.comandos:
                resposta(self.comandos[self.Input])
                 
                 
            elif 'exelente' in self.comandos:
                resposta('Eu sei, Eu sou a melhor')
            
            elif 'bateria' in self.Input:
                bateria()
            
            elif 'perfeito' in self.Input:
                resposta('Eu sei, eu sou a melhor')
            
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
                    
                
                
            
            elif 'vai chover' in self.Input:
	            resposta('Não sei')
	            resposta('Eu não tenho essa função ainda')
                
	       
            elif 'errado' in self.Input:
                
                resposta('Desculpa')
                resposta('Errei um cálculo')
                resposta('Tente seu comando novamente')
	        
            elif 'falhando' in self.Input: #Voçê está falhando???
                resposta('Como assim?')
                resposta('Não vou admitir erros')
                resposta('Arrume logo isso') 
	
            elif 'relatório' in self.Input: #Relatório do sistema
                resposta('Ok')
                resposta('Apresentando relatório')
                resposta('Primeiramente, meu nome é SARA')
                resposta('Atualmente estou em uma versão de testes BETA v1.0')
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
                            self.vozmic1 = self.GivenCommand()
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
                            self.vozmic2 = self.GivenCommand()
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
                            self.vozmic3 = self.GivenCommand()

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

            
            elif 'login' in self.Input:

                while True:
                    try:
                        try:
                            resposta('Qual o seu nome de usuario ')
                            self.vozmic1 = self.GivenCommand()
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
                            self.vozmic2 = self.GivenCommand()
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
                resposta('Me fale o que voçê deseja pesquisar')
                try:
                    self.vozmic2 = self.GivenCommand()
                        
                        
                    resposta(f'Ok, pesquisando no google sobre {self.vozmic2}')
                    webbrowser.open('http://google.com/search?q='+self.vozmic2)
                
                except:
                    resposta('Erro')
                    resposta('Não foi possivel conectar ao google')
                    resposta('A conexão falhou')
            
            elif 'resumo' in self.Input: #Me fale sobre um assunto
                resposta('Ok')
                resposta('Sobre qual assunto?')
                
                try:
                    self.vozmic2 = self.GivenCommand()
                    
                    resposta('Interessante')
                    resposta('Aguarde um momento')
                    resposta(f'Vou pesquisar e apresentar um resumo sobre {self.vozmic2}')
                    procurar = self.vozmic2.replace('resumo', '')
                    wikipedia.set_lang('pt')
                    resultado = wikipedia.summary(procurar,2)
                    print(resultado)
                    respostalonga(resultado)
                   
                        
                        
                        
                    
                    system_os = platform.system()
                
                    if 'Windows' in system_os:
                        with open(r'C:\Users\Wendel\Documents\GitHub\Sara_Python\Sara_inteface_grafica\resumo\resumo_texto.txt', 'a+', encoding='UTF-8') as arquivo:
                            arquivo.write(f'{resultado}')
                            resposta('Escrevir o resumo para você')
                        
                        
                       
                except:
                    resposta('Erro')
                    resposta('A conexão falhou')
                    # Mais um assusto    
	        
            elif 'interessante' in self.Input: # interessante
                resposta('Interessante sou eu')
                resposta('Me fale mais comandos')
                resposta('Eu posso surpreender voçê')
           
            elif 'exêlente' in self.Input:
                resposta('EU sei disso, eu sou incrível')
	        
            elif 'mentira' in self.Input: # mentira
                resposta('É mesmo é, eu não ligo')
                resposta('Devo apenas ter errado um cálculo ')
	            
            elif 'entendeu' in self.Input: #entendeu???
                resposta('Entendi')
                resposta('Quer dizer')
                resposta('Mais ou menos')
                print(self.Input)
	
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
                    resposta('Abrindo arquivos')
                    os.system("thunar //home//*//")
         
            elif 'teste' in self.Input: #TesteTeste
                resposta('Ok')
                resposta('Testando modulos de som')
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
                resposta('haha, Burra é tu')
                
            elif  'vaca' in self.Input:
                resposta('Vaca é seu pai, com aqueles chifres')
                  
            elif 'cachorra' in self.Input:
                resposta('Cachorra é você Cadela')     
                
            elif 'piada' in self.Input: #Conte uma piada
                resposta('Não sei contar piadas')
                resposta('Diferente dos outros assistentes virtuais')
                resposta('Eu não fui criado com emoções')
                resposta('Então, não posso produzir nada engraçado')
                resposta('Sugiro pesquisar na web')
            
            
                
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
	        
            elif 'música' in self.Input:
                musica = self.Input.replace('música', '')
                try:
                    resultado = pywhatkit.playonyt(musica)
                    resposta(f'Tocando música {musica}')
                except:
                    resposta('Não consegue tocar a música')
                
         
            elif 'playlist' in self.Input: #Reproduzir música
                try:
                    resposta('Ok')
                    resposta('Reproduzindo música')
                    os.startfile('"%ProgramFiles(x86)%\Windows Media Player\wmplayer.exe"')

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
                resposta('Volume diminuido')
	        
                                         
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
                sys.exit()
	     
            elif 'ok' in self.Input: #OkOkOk
                resposta('Ok Ok')
                resposta('Tudo certo') 
	
            elif 'sistema' in self.Input: #Carga do sistema
                system_os = platform.system()
                
                if 'Windows' in system_os:
                    cpu()
                    resposta('A temperatura do CPU não possivel ver no Windows ')
                else:
                    cpu()
                    temperaturadacpu()
            
            
                        
            elif 'escreva' in self.Input:
                try:
                   
                        
                    resposta('Fale o que deseja que eu escreva')
                    self.vozmic = self.GivenCommand()

                    with open('escrito/texto_escrito_pela_sara_usuario.txt', 'a+',  encoding='UTF-8') as arquivo:
                        arquivo.write(f'{self.vozmic}')
                        resposta('Pronto escrito')
                
                except:
                    resposta('Desculpe, Erro na conexão')
        
            try: # Responder Perguntas de matematica >> ( + e  -) 
                resposta(eval(self.Input))
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
        self.movie = QMovie("SARA.gif")
        self.label_gif.setMovie(self.movie)
        self.movie.start()
        
        self.label_sara = QLabel(self)
        self.label_sara.setText("SARA")
        self.label_sara.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sara.move(0,0)
        self.label_sara.setStyleSheet('QLabel {font:bold;font-size:16px;color:#2F00FF}')
        self.label_sara.resize(400,300)
        
        self.label_cpu = QLabel(self)
        self.label_cpu.setText("Uso da CPU: 32%")
        self.label_cpu.setAlignment(QtCore.Qt.AlignCenter)
        self.label_cpu.move(10,270)
        self.label_cpu.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_cpu.resize(131,20)
        cpu = QTimer(self)
        cpu.timeout.connect(self.MostrarCPU)
        cpu.start(1000)
        
        self.label_assv = QLabel(self)
        self.label_assv.setText("Assistente Virtual")
        self.label_assv.move(5,5)
        self.label_assv.setStyleSheet('QLabel {font:bold;font-size:14px;color:#000079}')
        self.label_assv.resize(200,20)

        self.label_version = QLabel(self)
        self.label_version.setText("Versão BETA 1.0")
        self.label_version.setAlignment(QtCore.Qt.AlignCenter)
        self.label_version.move(265,270)
        self.label_version.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_version.resize(131,20)
        
        data =  QDate.currentDate()
        datahoje = data.toString('dd/MM/yyyy')
        self.label_data = QLabel(self)
        self.label_data.setText(datahoje)
        self.label_data.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data.move(316,25)
        self.label_data.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_data.resize(75,20)
          
        self.label_horas = QLabel(self)
        self.label_horas.setText("22:36:09")
        self.label_horas.setAlignment(QtCore.Qt.AlignCenter)
        self.label_horas.move(0,25)
        self.label_horas.setStyleSheet('QLabel {font-size:14px;color:#000079}')
        self.label_horas.resize(71,20)
        horas = QTimer(self)
        horas.timeout.connect(self.MostrarHorras)
        horas.start(1000)
        
        botao_fechar = QPushButton("",self)
        botao_fechar.move(370,5)
        botao_fechar.resize(20,20)
        botao_fechar.setStyleSheet("background-image : url(fechar.png);border-radius: 15px") 
        botao_fechar.clicked.connect(self.fechartudo)
        
        self.CarregarJanela()
		
    def CarregarJanela(self):
        self.setWindowFlag(Qt.FramelessWindowHint) #sem botoes e titulo
        self.setGeometry(50,50,400,300)
        self.setMinimumSize(400, 300)
        self.setMaximumSize(400, 300)
        self.setWindowOpacity(0.98) 
        self.setWindowIcon(QtGui.QIcon('icone.png'))
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
        usocpu =  str(psutil.cpu_percent())
        self.label_cpu.setText("Uso da CPU: " +usocpu +"%")
		
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec_())

