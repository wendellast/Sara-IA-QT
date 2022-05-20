#Sara escrever texto que você está falando
import speech_recognition as sr
import pyttsx3
from rich import print

#Reconhecedor de Audio
audio = sr.Recognizer()
sara = pyttsx3.init()

def text():
    
    with sr.Microphone() as source:
        
            
            print('[blue]Ouvindo...[/]')
            print('[purple]Fale o que deseja que eu escreva !![/]')
            reconhecedor = audio.listen(source) # Definir o microfone 
            comando_escrever = audio.recognize_google(reconhecedor, language='pt-BR')
            comando_escrever = comando_escrever.lower()
    
    with open('usuario_texto.txt', 'w') as arquivo:
        print(comando_escrever)
        arquivo.write(f'{comando_escrever}')
        print('Pronto escrito')
        sara.say('Pronto, escrito')
        sara.runAndWait()