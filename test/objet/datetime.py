from random import randint

class Pessoas:
    ano_atual = 2022

    def __init__(self, nome, idade):

        self.nome = nome
        self.idade = idade

    def Get_Nascimento(self):
        print(self.ano_atual - self.idade)



    @classmethod 
    def por_ano_nascido(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    @staticmethod
    def id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoas('Wendel', 17)

print(p1.nome, p1.idade)
print(Pessoas.id())