from rich import print
from config.config_dados import *
import os

#Módulos

def criar_diretorio():
    escolha = input
    raw_input = escolha
    if(escolha == 'diretorio'):
                nome_diretorio=raw_input('Insira o nome do diretorio: ')
                try:
                    os.mkdir(nome_diretorio)
                    print('Pronto!\n')
                
                except OSError:
                    print('Diretorio já existe\n')
             


def remover():
    escolha = input('O que deseja')
    diretorio_atual=os.getcwd()
    


    if(escolha == 'remover'):
        raw_input = input('Quer criar arquivo ou diretório? ')
        os.chdir(diretorio_atual)

        
        if(raw_input== 'arquivo'):
            nome_arquivo = input('Qual o nome do arquivo')
            os.chdir(os.getcwd()+'/'+'arquivos')
            if(os.path.isfile(nome_arquivo)):
                os.remove(nome_arquivo)
                print('Removido')
                os.system('espeak -v pt-br -g 4 -a 100 "Removido"')
            else:
                print('arquivo não existe')
                os.system('espeak -v pt-br -g 4 -a 100 "Arquivo não existe"')

        elif(raw_input == 'diretorio'):
                nome_arquivo = input('Qual o nome do Diretorio')
                if(nome_arquivo == 'modules' or nome_arquivo == 'test' or nome_arquivo == 'dados' or nome_arquivo == 'build' or escolha == 'config' or nome_arquivo == 'escrito'or nome_arquivo == 'img' or nome_arquivo == 'memoria' or nome_arquivo == 'model-br' or nome_arquivo == 'music' or nome_arquivo == 'resumo' or nome_arquivo == 'venv'):

                    print('Pastas protegidas, não podem ser apagadas')
                    
                else:
                    try: # Conserta depois
                        local = os.getcwd()
                        os.chdir(local)
                        os.rmdir(nome_arquivo)
                        print('removido!\n')
                       
                    except OSError:
                        print('Diretorio não existe')
                       
def editar():

            palavras = input('O Que você uqer editar ')
       
        
            if(palavras == 'arquivo'):
                raw_input =input(('Insira o nome do arquivo: '))
                nome_arquivo=raw_input 
                try:
                    os.chdir(os.getcwd()+'/'+'arquivos')
                except OSError:
                    os.mkdir('arquivos')
                    os.chdir(os.getcwd()+'/'+'arquivos')
                os.system('gedit '+nome_arquivo)
            else:
                print('A penas possivel editar arquivos')
                os.system('espeak -v pt-br -g 4 -a 100 "A penas possivel editar arquivos"')
           
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
    