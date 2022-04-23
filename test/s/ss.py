class Pessoas:
    def __init__ (self, nome, idade, sxo):

        self.nome = nome
        self.idade = idade
        self.sxo = sxo

    def info(self):
        print(f' Nome: {self.nome}, Idade: {self.idade}, Sexo: {self.sxo}')
