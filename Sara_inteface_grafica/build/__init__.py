import os
from rich import print
import platform

comandos_adicionar = []
comandos_novos = []

def abrir_arquivos(): # Conserta depois
    try:
         os.startfile(r'C:\Users\Wendel\AppData\Roaming\Microsoft\Internet Explorer\Quick Launch\User Pinned\TaskBar')
         
    except:
        print('Erro não consegue abrir')
    
def comando_novo(*args):
    comandos_novos.append(*args)
    comandos_adicionar.append(comandos_novos[:])
    comandos_novos.clear()
    




 
    
def text():
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(s)
            audio = r.listen(s)
            resposta('Fale o que deseja que eu escreva')
            self.Input
                
            
            
            
        
        with open('usuario_texto.txt', 'w') as arquivo:
            arquivo.write(f'{self.Input}')
            resposta('Pronto escrito')
    
    except:
        resposta('Desculpe, Erro na conexão')
        