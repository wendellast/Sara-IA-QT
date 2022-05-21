#Interface terminal
from rich import print
from rich.table import Table

def linha(msg=''): # Linha para menu
    
    print('[bold][green]=-=[/]'*20) # linha separar
    print(f'[bold][red]{msg:^30}')
    print('[bold][green]=-=[/]'*20)
    
    
def linha_extra(): # Linha para menu
    print('[bold yellow]=-=[/]'*20) # linha separar
    

def linha_sara(): # Linha para menu
   
    
    #Tabela Sara >> 
    table = Table(title='----> SARA <----', title_justify='center', title_style='blue')
    
    table.add_column('Informação', justify='center', style='purple')
    table.add_column('Versão', justify='center', style='red')
    table.add_column('Suporte', justify='center', style='green')
    
    #Adicionar linhas nas colunas >> 
    table.add_row('Sara, assistente virtual pessoal', '--Beta v1.0--   Compativel: Windows >> Sim;   linux >> Em breve;   Mac >> Em breve  ',  'Contado: Telegram >> https://t.me/Lasstll')
    
   
  
    
    print(table)
    
