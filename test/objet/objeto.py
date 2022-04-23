from datetime import datetime

class Pessoas:
    anoatual = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, nome, idade,falar=False, comendo=False ):
        self.nome = nome
        self.idade = idade  
        self.falar = falar
        self.comendo = comendo


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'{self.nome} está comendo {alimento}')
        self.comendo = True

    def para_comer(self):
        if not self.comendo:
            print(f'{self.nome} não esta comendo')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def nascimento(self):
        return self.anoatual - self.idade