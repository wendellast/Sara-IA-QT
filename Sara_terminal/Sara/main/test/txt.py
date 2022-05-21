#Importação de Bibliotecas e Módulos
from rich import print
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pywhatkit
import os

#Reconhecedor de Audio
audio = sr.Recognizer()
sara = pyttsx3.init()


# Abre o microfone para falar
def executar(): # Executar comando 
    
    try:
        with sr.Microphone() as source:
        
            
            print('[blue]Ouvindo...[/]')
            reconhecedor = audio.listen(source) # Definir o microfone 
            comando = audio.recognize_google(reconhecedor, language='pt-BR')
            comando = comando.lower()
            
        #Identificar comando    
        if 'sara' in comando:
            comando = comando.replace('sara', '')
            

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
                
            elif 'sair' in comando:
                print('saindo...')
                break
            
            elif 'ei sara ' in comando:
                return comando
            
            elif 'escrever' in comando:
                text()
    except:
        print('Erro, algo deu errado !!')
        sara.say('Erro, algo deu errado')
        sara.runAndWait()
        
 





def text():
    
    with sr.Microphone() as source:
        
            
            print('[blue]Ouvindo...[/]')
            reconhecedor = audio.listen(source) # Definir o microfone 
            comando_escrever = audio.recognize_google(reconhecedor, language='pt-BR')
            comando_escrever = comando_escrever.lower()
    
    with open('usuario_texto.txt', 'w') as arquivo:
        print(comando_escrever)
        arquivo.write(f'{comando_escrever}')
        
text()