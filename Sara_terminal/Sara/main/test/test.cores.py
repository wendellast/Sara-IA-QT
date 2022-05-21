from time import sleep
from rich.progress import track
from rich.console import Console
from rich.table import Table
from rich.layout import Layout

#for tarefa in track(range(18), 'Processando...'):
 #   sleep(5)
 
console = Console() 
def criar_arquivo():
     for i in range(18):
         with open(f'Arquivo{i}.txt', 'w') as file:
            file.write('Criando um arquivo')             
            sleep(2)
            console.log(f'Tarefa {i} Finalizada !!')
            
            
#with console.status('[green] Realizando a tarefa >> [/]') as arquivo:
 #   criar_arquivo()
 

table = Table(title='Filmes Favoritos')            
table.add_column('Nome', justify="left", style='red')
table.add_column('Data de  lançamento')
table.add_column('Faturamento')

table.add_row('Peiratas de caribe', '2005', '1298498598')
console.print(table)    
              




#layout = Layout()

#layout.split_column(
 #   Layout(name='top'),
#    Layout(name='baixo')
    


#print(layout)

