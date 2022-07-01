from plyer import notification
from rich.table import Table
from rich import print
from datetime import time

import os
import rich
import psutil
import platform
import pyaudio
import pyttsx3
import datetime
import requests



#Configurações de dados


plataforma = platform.system()



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
    sara_voz.runAndWait()
    stream.start_stream ()

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
            resposta('Ela está em nível crítico')
            resposta('Por favor, coloque o carregador')
        elif carga == 100:
            resposta('Ela está totalmente carregada')
            resposta('Retire o carregador da tomada')
    except:
        resposta(f'Não foi possível dizer a bateria')

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
    table = Table(title='----> SARA <----', title_justify='center', title_style='blue')
    
    table.add_column('Informação', justify='center', style='purple')
    table.add_column('Versão', justify='center', style='red')
    table.add_column('Suporte', justify='center', style='green')
    
    #Adicionar linhas nas colunas >> 
    table.add_row('Sara, assistente virtual pessoal', '--Beta v1.0--   Compatível: Windows >> Sim;   linux >> Sim(Beta);   Mac >> Em breve  ',  'Contado: Telegram >> https://t.me/Lasstll')
    
    print(table)

    return 0
    
