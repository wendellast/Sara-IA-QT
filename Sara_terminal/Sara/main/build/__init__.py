#Importação de Bibliotecas e Módulos
from build import interface
from build import uteis
from flask import Flask, request
from rich import print
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os



audio = sr.Recognizer() #Reconhecedor de Audio

sara = pyttsx3.init('sapi5') # escolha sua sintese de voz (caso não tenha deixe sem nada, que irar ser automaticamente Sapi5)

# Usado Original sintese de voz Letícia
voz = sara.getProperty('voices')
sara.setProperty('voice', voz[2].id)
velocidade = sara.getProperty('rate')
sara.setProperty('rate', velocidade-50)


# Abre o microfone para falar
def executar(): # Executar comando 
    
    try:
        while True:
            
            with sr.Microphone() as source:
            
                
                print('[blue]Ouvindo...[/]')
                reconhecedor = audio.listen(source) # Definir o microfone 
                comando = audio.recognize_google(reconhecedor, language='pt-BR')
                comando = comando.lower()
                
            #Identificar comando    
            if 'sara' in comando:
                comando = comando.replace('sara', '')
                
            elif 'sair' in comando:
                break
            

    except:
        
        #Erro de microfone 
        print('[red]Infelizmente o seu microfone não está funcionando, verifique e tente novamente !!![/]')
        
        sara.say(f'Infelizmente o seu microfone não está funcionando, verifique e tente novamente')
        sara.runAndWait()

    return comando

#Comandos do Usuário >>>
def usuario_comandos():
    
    try:
        while True:
        
            comando = executar() # Executar comando de voz 
            
            
            if 'procure' in comando: # Comando para procurar algo na Wikipedia
                
                procurar = comando.replace('procure', '')
                wikipedia.set_lang('pt')
                resultado = wikipedia.summary(procurar,2)
                interface.linha('Wikipedia')
                print(resultado)
                sara.say(resultado)
                sara.runAndWait()
                
            elif 'horas' in comando: # Peguntar Horas
                hora = datetime.datetime.now().strftime('%H:%M')
                
                print(f'Agora são {hora} horas / minutos')
                sara.say(f'Agora são {hora}')
                sara.runAndWait()
              
                
            elif 'oi' in comando: # Comando cumprimento
                print(f'Olá, eu sou Sara, Tudo bem ?')
                sara.say('Olá, eu sou Sara, Tudo bem ?')
                sara.runAndWait()
                
            elif 'toque' in comando: # Tocar musica no youtube 
                musica = comando.replace('toque', '')
                resultado = pywhatkit.playonyt(musica)
                print(f'Tocando música {musica}')
                sara.say(f' Tocando música {musica}')
                sara.runAndWait()
                
            elif 'abrir chrome' in comando:
                abrir = comando.replace('abrir chrome', '')
                sara.say(f'Abrindo {abrir}')
                sara.runAndWait()
                abrir = os.startfile('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
                
                
            elif 'escreva' in comando:
                uteis.text()
                
            elif 'sair' in comando:
                print('[cyan]saindo...[/]')
                sara.say('Saindo')
                sara.runAndWait()
                break
                
            
            elif 'ei sara ' in comando:
                return comando
            
    
    except:
        print('Erro, algo deu errado !!')
        sara.say('Erro, algo deu errado')
        sara.runAndWait()


    
    
        



