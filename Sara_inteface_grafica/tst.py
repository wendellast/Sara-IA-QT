import json
import os
import shelve
import shutil
import tempfile

with open('mente.json', 'r', encoding='utf-8') as arq, \
     tempfile.NamedTemporaryFile('w', delete=False) as out:
    # ler todo o arquivo e obter o objeto JSON
    dados = json.load(arq)
    # atualizar os dados com a nova pergunta
    dados["PERGUNTA 4"] = "RESPOSTA"
    # escreve o objeto atualizado no arquivo temporário
    json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))

# se tudo deu certo, renomeia o arquivo temporário
shutil.move(out.name, 'mente.json')




'''
with open('mente.json', 'r', encoding='utf-8') as arq, \
    shelve.open('mente_shelve.json') as novos_dados:
    dados = json.load(arq)
    novos_dados.update(dados)
                    
with shelve.open('mente_shelve.json') as dados:
    # a linha abaixo já atualiza o arquivo
    comando[chave] = valor'''