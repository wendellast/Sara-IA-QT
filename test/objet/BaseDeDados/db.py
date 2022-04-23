
class BaseDeDados:
    def __init__(self):
        self.dados = {}

    def iserir_clientes(self, id, nome):
        if 'clientes' not in self.dados:
            self.dados['clientes'] = {id: nome}
        else:
            self.dados['clientes'].update({id: nome})


    def lista_clentes(self):
        for id, nome in self.dados['clientes'].items():
            print(id, nome)

    def delcleintes(self, id):
        del self.dados['clientes'][id]



bd = BaseDeDados()

bd.iserir_clientes(1,'wendel')
bd.iserir_clientes(2, 'carol')
bd.iserir_clientes(3, 'joão')

bd.delcleintes(2)

bd.lista_clentes()
