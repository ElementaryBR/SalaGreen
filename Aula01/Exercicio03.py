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
import random

class Circulo:
    def __init__(self):
        self.__cor = ''
        self.__raio = 0.0
        self.__material = ''

    def getter_raio(self):
        return self.__raio

    def getter_cor(self):
        return self.__cor

    def lista_de_cores(self):
        return ['Rosa','Amarelo','Preto','Vermelho','Azul','Verde','Cinza','Roxo','Prata','Branco','Prata','Dourado','Caramelo','Marfim','Marrom','Laranja']

    def setter_raio(self,raio):
        self.__raio = self.area(raio)

    def trocaCor(self):
        self.cor_aleatoria = random.choice(self.lista_de_cores())
        self.__cor = self.cor_aleatoria

    def mostraCor(self):
        return self.__cor

    def area(self,raio):
        result = (math.pi*raio**2)
        return result

class Quadrado:
    def __init__(self):
        self.__tamanho_do_lado = 0

    def getter(self):
        return self.__tamanho_do_lado

    def mudar_tamanho(self,valor):
         self.__tamanho_do_lado = valor

    def calcular(self):
        self.resultado = self.__tamanho_do_lado * self.__tamanho_do_lado
        return self.mudar_tamanho(self.resultado)

class Retangulo:
    def __init__(self):
        self.__base = 0
        self.__altura = 0

    def setter_lados(self,base,altura):
        self.__altura = altura
        self.__base = base

    def getter(self):
        base = self.__base
        altura = self.__altura
        return f'A base tem valor de {base} e a altura tem valor de {altura}'

    def calculo_area(self):
        self.result = self.__base * self.__altura
        return self.result

circulo = Circulo()
quadrado = Quadrado()
retangulo = Retangulo()



circulo.trocaCor()
print(circulo.getter_cor())
circulo.setter_raio(5)
print(f'{circulo.getter_raio():.2f}')


quadrado.mudar_tamanho(5)
print(quadrado.getter())
quadrado.calcular()
print(quadrado.getter())


print(retangulo.getter())
retangulo.setter_lados(10,2)
print(retangulo.getter())
print(retangulo.calculo_area())