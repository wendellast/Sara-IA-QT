from time import sleep
import math
from random import randint
from datetime import date

# falar caracteristicas do nome 
def nome():
    nome = str(input('Digite seu nome >> ')).strip()

    print('Analizando seu Nome !!')
    sleep(2)

    print(f'Seu nome em maisculo é {nome.upper()}')
    print(f'Seu nome em minusculo é {nome.lower()}')
   # print(f'Seu Primeiro nome tem {nome.find('') letras}')
    separa = nome.split()
    print(f'Seu primeiro nome é {separa[0]} e tem {len(separa[0])} letras')
    print(f'Seu nome tem {len(nome)} Letras')


#verifica se o nome começa com santos
def santos():
    n = str(input('Digite o nome da cidade >> ')).strip()
    print(n[:5].upper() == 'SANTO')


#Dizer se tem silva no nome 
def silva():
    nome = str(input('Digite seu nome >> ')).strip() # remover spaços
    
    if 'SILVA' in nome.upper():
        print('True')
    else:
        print('False')

#Encontra a letra 'A'
def letra():
    frase = str(input('Digite sua frase >> ')).upper().strip()
    s = frase.count('A')
    v = frase.find('A')
    vv = frase.rfind('A')
    print(f'A letra A apareceu {s} vezes e na  primeira posição {v+1} , e na ultima posição {vv}')


#raiz quadrada função math
def raiz():
    n = int(input('Digite um número >> '))

    r = math.sqrt(n)
    print(r)

# jogo de adivinhar
def adivinha():
    jogador = int(input('Digite seu número >> '))
    r = randint(0, 6)
    if jogador == r:
        print('Você venceu !!')
        print(f'Eu pensei no numero {r}')
    else:
        print('Sinto muito não foi dessa vez')
        print(f'Eu pensei no numero {r}')


#multa carro
def muta():
    velocidade= int(input('Digite a velocidade do carro >> '))

    if velocidade > 80:
        muta = (velocidade -80) *7
        print(f'print você ultrapasou o limite de velocidade, irar pagar muta de {muta} ')
    else:
        print('Tudo certo pode ir')


# impar ou par
def impar():
    numero = int(input('Digite um número >> '))
    resultado = numero % 2
    if resultado == 0:
        print('Numero par')
    else:
        print('Numero impar')

#calcualr viagem preçoer
def viagem():
    viagem = float(input('Digite qual a distancia da sua viagem >> '))

    if viagem <= 200:
        via = viagem *0.50
        print(f'A sua viagem vai custar {via}')

    else:
        via2 = viagem * 0.80
        print(f'Sua viagem vai custar {via2}')

#ano bixelto
def ano():
    ano = int(input('Digite o seu ano >> '))
    
    if ano == 0:
        ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'{ano} bixesto')
    
    else:
        print(f'Esse ano de {ano} não é bixesto')

ano()        