

class Dobradura:
    def __init__(self):
        self.papel = 'Teste do Papel'
        self.divisoes = 1
        self.dobradura = 2

    def get_dobrar(self,numero):
        if numero == numero *-1:
            return False
        elif numero == str(numero):
            return False
        numero = int(numero)
        for a in range (numero):
            dobradura = 2
            contador = 0
            a = 5357543035931336604742125245300009052807024058527668037218751941851755255624680612465991894078479290637973364587765734125935726428461570217992288787349287401967283887412115492710537302531185570938977091076523237491790970633699383779582771973038531457285598238843271083830214915826312193418602834034689
            while dobradura <= a:
                contador += 1
                calculo = dobradura * 2
                if contador == numero:
                    return int(dobradura)
                dobradura = int(calculo)


# if __name__ == '__main__':
papel = Dobradura()
print(papel.get_dobrar('5'))


# 1 dobradura = 2
# 2 dobradura = 4
# 3 dobradura = 8
# 4 dobradura = 16

