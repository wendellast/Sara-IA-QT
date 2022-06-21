from rich import print
from config.config_dados import *
import os

#Módulos

  




           

           

def esvaziar_lixeira():
    frase = input('O deseja')
    if(frase == 'esvaziar lixeira' or frase == 'esvaziar'):
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
        print('Pronto!\n')
        os.system('espeak -v pt-br -g 4 -a 100 "Pronto!"')

def calculadora():
        os.system('gnome-calculator')
    
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
    