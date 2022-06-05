import json
import shutil
import tempfile

chave = 'oi'
valor = '9'

with open(r'C:\Users\Wendel\Documents\GitHub\Sara_Python\Sara_inteface_grafica\test\test.json', 'r', encoding='UTF-8') as arq, \
    tempfile.NamedTemporaryFile('w', delete=False,encoding='UTF-8') as out:
    # ler todo o arquivo e obter o objeto JSON
    dados = json.load(arq)
    # atualizar os dados com a nova pergunta
    dados[chave] = valor
    # escreve o objeto atualizado no arquivo temporário
    json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))

# se tudo deu certo, renomeia o arquivo temporário
shutil.move(out.name, r'C:\Users\Wendel\Documents\GitHub\Sara_Python\Sara_inteface_grafica\test\test.json')
    
