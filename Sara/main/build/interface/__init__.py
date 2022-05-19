#Interface terminal
import colorama #Cores Terminal


def linha(msg=''): # Linha para menu
    
    print('~~~~~~'*len(msg))
    print(f'{msg:^30}')
    print('~~~~~~'*len(msg))