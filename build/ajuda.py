#Ajuda sobre comandos
#Aqui vamos informa o que cada comando faz
from config.config_dados import *
from rich.table import Table
from rich import print

def ajuda(comando):
    

    if 'comandos' in comando:

        resposta('Tudo bem, Mostrando lista de comandos ')
        
        list_comando1 = ['sara','historico','silencio','horas','aprenda','bateria','easter egg','relatório','cadastro','tira print','login','pesquisa','resumo',
        'data','abrir arquivos', 'criar arquivo', 'criar pasta','música','remover arquivo','remover pasta','editar arquivo','renomear arquivo','renomear pasta', 'esvaziar lixeira', 'abrir calculadora','playlist','desligar','temperatura do sistema','escreva','quanto é']


        table = Table(title='----> Comandos <----', title_justify='center', title_style='blue')

        table.add_column('Comandos 1', justify='center', style='purple')
  
        for i in list_comando1:
                table.add_row(f'{i}')
  
        print(table)
        return table


    elif 'sara' in comando:
        resposta('Sara é uma assistente virtual pessoal, ela foi criada para ser uma companheira no seu dia dia, onde possa ter alguém para conversar e desabafar, também focada em ajuda os necessitados como deficientes visuais, usando a Sara para poder usar o seu dispositivo sem a necessidade das mãos')
    
    elif 'historico' in comando:
        resposta('O comando historico mostra todos os comandos que você usou enquanto a Sara estava aberta. obs quando você desliga a sara o historico é limpado automaticamente ! ')

    elif 'silencio' in comando:
        resposta('O comando silencio serve para deixa a sara em modo silencio, elá não responde nada enquanto você não libera ela. para tira desse modo basta dizer voltar, volte ou retornar')

    elif 'horas' in comando:
        resposta('Comando horas serve para mostra as horas né !')

    elif 'aprenda' in comando:
        resposta('O comando resposta serve para ensinar a sara algo, bastar dizer "aprenda" falar a frase e o que ela deve fazer ao ouvir essa frase, depois use o comando treinar para que a sara aprenda o novo comando.')

    elif 'bateria' in comando:
        resposta('O comando bateria serve para a sara dizer qual o nível de bateria do dispositivo')

    elif 'easter egg' in comando:
        resposta('Easter egg são comandos divertidos que a Sara tem, para usar basta dizer um desses, "a terra é plana", "desenha sistema solar" ') #fazer depois

    elif 'relatório' in comando:
        resposta('O comando relatório serve para mostra informações sobre a sara')
    
    elif 'cadastro' in comando:
        resposta('O comando cadastro serve para cadastrar novos usuários')
    
    elif 'tira print' in comando:
        resposta('O comando de "tira print" faz com que a sara tire uma foto da tela do dispositivo')
    
    elif 'login' in comando:
        resposta('O comando login serve para carregar um novo usuário')

    elif 'pesquisa' in comando:
        resposta('Esse comando serve para você dizer a Sara o que ela deve pesquisa no google')

    elif 'resumo' in comando:
        resposta('O comando resumo serve para você dizer um assunto a sara e ela ira fazer um resumo sobre o assunto e escrever um arquivo txt com o assunto')
    
    elif 'data' in comando:
        resposta('Comando data serve para que a Sara diga a data, basta falar "data", "que dia é hoje" para ativar o comando')
        
    elif 'abrir arquivos' in comando:
        resposta('Serve para que a Sara abra o gerenciador de arquivos do dispositivo')

    elif 'abrir google' in comando:
        resposta('Serve para que a Sara abra o google no seu navegador')

    elif 'criar arquivo' in comando:
        resposta('Serve para que sara crie arquivos do tipo que o usuário basta que no final diga a extensão por exemplo, "criar arquivo jogo.txt" ')

    elif 'criar pasta' in comando:
        resposta('Serve para que a sara possa criar pastas, basta dizer o comando e o nome da pasta a ser criada, observação não pode criar pastas já existentes')

    elif 'música' in comando:
        resposta('Comando música serve para pede a sara que toque uma música no youtube, basta dizer "música" e o nome da música')

    elif 'remover arquivo' in comando:
        resposta('O comando de remover arquivo, serve para dizer a Sara para apagar um arquivo, basta dizer "remover arquivo" e o nome do arquivo junto com a extensão no final, observação não é possível apagar arquivos necessários para o funcionamento da Sara, então esses arquivos estão bloqueados. ')

    elif 'remover pasta' in comando:
        resposta('O comando de remover pastas serve para dizer a Sara para apagar uma pasta, basta dizer "remover pasta" e falar o nome da pasta a qual você quer apagar porem se a pasta estiver protegida ou seja for necessária para o funcionamento da sara não sera possível apagar')

    elif 'editar arquivo' in comando:
        resposta('O comando de editar arquivos serve para poder editar arquivos que o usuário deseja, lembrando de informa a extensão no final do arquivo')

    elif 'renomear arquivo' in comando:
        resposta('Serve para a Sara poder editar o nome do arquivo desejado')

    elif 'renomear pasta' in comando:
        resposta('O comando serve para que a Sara possa editar o nome de pasta que o usuário deseja, porem não pode ser pastas protegidas')

    elif 'esvaziar lixeira' in comando:
        resposta('Serve para mandar a Sara limpar a lixeira do dispositivo')
    
    elif 'abrir calculadora' in comando:
        resposta('O comando pede a Sara para abrir a calculadora do sistema')

    elif 'playlist' in comando:
        resposta('O comando manda a Sara tocar as músicas que estão no dispositivo, podendo usar comandos como "proximo, para, pausar, diminuir, aumenta " enquanto o comando estiver ativo, para desativar basta dizer "parar playlist"')
    
    elif 'desligar' in comando:
        resposta('O como serve para desligar a Sara fazer ela sair.')
    
    elif 'temperatura do sistema' in comando:
        resposta('Esse comando faz a Sara dizer como está a temperatura do sistema')
    
    elif 'escreva' in comando:
        resposta('O comando "escreva" serve para você manda a sara escrever o que você vai dizer')
    
    elif 'quanto é' in comando:
        resposta('O comando "quanto é" é usado para fazer a Sara fazer contas, basta dizer "quanto é" mais o calculo por exemplo 5+5  ')

    else:
        resposta('Desculpe comando não encontrado !!')


