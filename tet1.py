import tempfile
import json
import psutil
chave = 'morango'
valor = 'blabla'

with open('memoria/memoria.json', 'r', encoding='UTF-8') as arq, \
    tempfile.NamedTemporaryFile('w', delete=False,encoding='UTF-8') as out:
    # ler todo o arquivo e obter o objeto JSON
    dados = json.load(arq)
    # atualizar os dados com a nova pergunta
    dados[chave] = valor
    # escreve o objeto atualizado no arquivo temporário
    json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))

    if chave in dados:
  
        print(dados)