from rich import print
from config.config_dados import *
import os

#Módulos

  




           
           
def renomear(): # melhorar
            palavras = input('O que você quer renomear')
     
            if(palavras == 'arquivo'):
                nome_arquivo = input('Qual o nome do Arquivo')
                try:
                    os.chdir(os.getcwd()+'/'+'arquivos')
                except OSError:
                    print('Não tem nenhum arquivo salvo')
                   
                    raw_input = input('Insira o novo nome ')
                    novo_nome=raw_input

                if(os.path.isfile(nome_arquivo)):
                    os.rename(nome_arquivo, novo_nome)
                    print('Pronto')
                    os.system('espeak -v pt-br -g 4 -a 100 "Pronto"')
                else:
                    print('Arquivo não existe')
                    os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

            elif(palavras == 'diretorio'):
                nome_arquivo = input('Qual o nome do diretorio ')
                if(os.path.isdir(nome_arquivo)):

                    if(nome_arquivo == 'modules' or nome_arquivo == 'test' or nome_arquivo == 'dados' or nome_arquivo == 'build' or nome_arquivo == 'config' or nome_arquivo == 'escrito'or nome_arquivo == 'img' or nome_arquivo == 'memoria' or nome_arquivo == 'model-br' or nome_arquivo == 'music' or nome_arquivo == 'resumo' or nome_arquivo == 'venv'):
                        print('Arquivos protegidos não pode ser renomeados')

                    else:
                        novo_nome=raw_input('Digite novo nome do diretorio: ')
                        os.rename(nome_arquivo, novo_nome)
                        print('Pronto')
                        os.system('espeak -v pt-br -g 4 -a 100 "Pronto"')

            else:
                print('Só pode renomear um diretorio ou arquivo ')
                os.system('espeak -v pt-br -g 4 -a 100 "Só pode renomear um diretorio ou arquivo "')

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
    