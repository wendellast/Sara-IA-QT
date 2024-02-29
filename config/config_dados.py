from plyer import notification
from rich.table import Table
from rich import print
from datetime import time
from config.config import *
from requests import get

import json
import os
import rich
import psutil
import platform
import pyaudio
import pyttsx3
import datetime
import requests
import random
import requests

try:
    from pyfirmata import Arduino, util, STRING_DATA

    board = Arduino('/dev/ttyUSB0') # Informe a porta do arduino
    arduino = True
except:
    arduino = False



#Configurações de dados
plataforma = platform.system()



if 'Windows' in plataforma:
    # Trás a função letícia voz
    sara_voz=pyttsx3.init('sapi5')

    # Função de ajuste de voz da sara
    voz = sara_voz.getProperty('voices')
    sara_voz.setProperty('voice', voz[0].id)
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)

else:
    # Trás a função letícia voz # Se não for a voz leticia padrão é Espeak
    sara_voz=pyttsx3.init()

    # Função de ajuste de voz da sara
    sara_voz.setProperty('voice', 'en')
    # No 'm2'(masculino) pode colocar 'f2'(feminino) e números até 7
    rate = sara_voz.getProperty('rate')
    sara_voz.setProperty('rate', rate-50)

# Preparando o microfone para captura
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)



def resposta(audio):
    notification.notify(title = "SARA",message = audio,timeout = 3)
    
    stream.stop_stream()
    print(f'[bold purple]SARA:[/] [cyan]{audio}[/]')
    sara_voz.say(audio)

    if arduino == True:
        try:
            board.send_sysex(STRING_DATA, util.str_to_two_byte_iter(audio) )
        except:
            pass
    sara_voz.runAndWait()
    stream.start_stream ()

def respostalonga(textofala): 
    stream.stop_stream ()
    print(f'[bold purple]SARA:[/] [cyan]{textofala}[/]')
    sara_voz.say(textofala)
    if arduino == True:
        try:
            board.send_sysex( STRING_DATA, util.str_to_two_byte_iter(textofala) )
        except:
            pass
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
        resposta("A bateria está em:" +bpint +'%')
        if carga <= 20:
            resposta('Ela está em nivel crítico')
            resposta('Por favor, coloque o carregador')
        elif carga == 100:
            resposta('Ela está totalmente carregada')
            resposta('Retire o carregador da tomada')
    except:
        resposta('Desculpa')
        resposta('Seu dispositivo atual não está usando bateria')
        resposta('Por isso é impossivel informar a quantidade de carga')

def cpu ():
    usocpuinfo = str(psutil.cpu_percent())
    usodacpu  = "{:.0f}".format(float(usocpuinfo))
    resposta('O uso do processador está em ' +usodacpu +'%')
    
def temperaturadacpu():
    tempcpu = psutil.sensors_temperatures()
    cputemp = tempcpu['coretemp'][0]
    temperaturacpu = cputemp.current
    cputempint = "{:.0f}".format(float(temperaturacpu))
    if temperaturacpu >= 20 and temperaturacpu < 40:
        resposta('Estamos trabalhado em um nível agradavel')
        resposta('A temperatura está em ' +cputempint +'°')

    elif temperaturacpu >= 40 and temperaturacpu < 58:
        resposta('Estamos operando em nivel rasoável')
        resposta('A temperatura é de ' +cputempint +'°')

    elif temperaturacpu >= 58 and temperaturacpu < 70:
        resposta('A temperatura da CPU está meio alta')
        resposta('Algum processo do sistema está causando aquecimento')
        resposta('Fique de olho')
        resposta('A temperatura está em ' +cputempint +'°')

    elif temperaturacpu >= 70 and temperaturacpu != 80:
        resposta('Atenção')
        resposta('Temperatura de ' +cputempint +'°')
        resposta('Estamos em nivel crítico')
        resposta('Desligue o sistema imediatamente')

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
        resposta('Não foi possível realizar essa tarefa')
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
    table = Table(title=f"»»»»»»»»»»»»»»»»»»»»»»»»»»»»»> {baner} <««««««««««««««««««««««««««««««", title_justify='center', title_style='bold blue')
    
    table.add_column('Informação', justify='center', style=' purple')
    table.add_column('Versão', justify='center', style='bold red')
    table.add_column('Suporte', justify='center', style='bold green')
    
    #Adicionar linhas nas colunas >> 
    table.add_row('Sara, assistente virtual pessoal', '--Beta v1.0--   Compatível: Windows >> Sim;   linux >> Sim;   ',  'Contado: Telegram >> https://t.me/Lasstll')
    
    print(table)

    return 0
   
def localizacao():
	try:
		EndereçoIP = get('https://api.ipify.org').text
		url = 'https://get.geojs.io/v1/ip/geo/'+EndereçoIP+'.json'
		geo_reqeust = get(url)
		geo_data = geo_reqeust.json()
		city = geo_data['city']
		resposta('Sua localização é '+str(city))
	except:
		resposta('Falha ao verificar a localização')
  
def primeira_vez():
    ler = open('build/cache.txt', 'r')
    leitura = json.loads(ler.read())
    if leitura == 0:
        resposta('Oie, Meu nome é Sara')
        resposta('A parte de agora sou sua nova assistente pessoal')
        resposta('Estou pronta para atender o seus comandos')
        resposta('Vai ser um prazer trabalha com você')
        resposta('Vamos lá me diga um comando :)')
        resposta('Se você não souber basta digitar ou falar')
        resposta('"help comandos" para ver os meus comandos')
        dicionario = 1
        f = open('build/cache.txt', 'w+')
        f.write(json.dumps(dicionario))

    elif leitura == 1:
        None