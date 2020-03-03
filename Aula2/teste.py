class Cliente:
    def __init__(self, nome='Junior'):
        self.nome = nome
        print('Junior')
    def compra(self):
        print('Quero comprar')

class ClienteVip(Cliente):
    def __init__(self,nome,num_vip):
        super(ClienteVip, self).__init__('')
        self.nome = nome
        self.num_vip = num_vip
        print(self.num_vip)

    def comprar(self):
        print('Quero comprar esse item especial')

cliente = Cliente()
clientevip =ClienteVip('',1)



lista1 = ['coisa1']
lista2 = ['coisa2']
result = lista1 + lista2
print(result)