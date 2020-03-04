# Classe Circulo: Crie uma classe que modele uma bola:
#
# Atributos: Cor, raio, material
# Métodos: trocaCor, mostraCor, area (math.pi*raio**2)
# para acessar o pi:
# import math
# math.pi

# Classe Quadrado: Crie uma classe que modele um quadrado:
#
# Atributos: Tamanho do lado
# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
# area = lateral*lateral


# Classe Retangulo: Crie uma classe que modele um retangulo:
#
# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área;
# area comprimento*largura


# crite testes para validar cada uma destas classes!

import math

class Circulo:
    def __init__(self):
        self.cor = ''
        self.raio = ''
        self.material = ''

    def trocaCor(self):
        pass
    def mostraCor(self):
        pass
    def area(self,raio):
        result = (math.pi*raio**2)
        return result
class Quadrado:

