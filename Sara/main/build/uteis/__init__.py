#Sara escrever texto que você está falando
import speech_recognition as sr
import pyttsx3
import pygame
import os
from rich import print

#Reconhecedor de Audio
audio = sr.Recognizer()
sara = pyttsx3.init('sapi5')

voz = sara.getProperty('voices')
sara.setProperty('voice', voz[2].id)
velocidade = sara.getProperty('rate')
sara.setProperty('rate', velocidade-50)

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
        
        
def musica_playlist(): # Tocar música da sua playlist
    
    caminho = r'C:\Users\Wendel\Documents\GitHub\Sara_Python\Sara\playlist'
    
       
    for diretorio,  arquivos in os.walk(caminho):
        for arquivos in arquivos:
           print(os.path.join(diretorio, arquivos))
           
           ''' pygame.init()
            pygame.mixer.music.load(arquivo)
            pygame.mixer.music.play()
            pygame.event.wait()

            while True:
              ...'''
        
    
musica_playlist()
    

