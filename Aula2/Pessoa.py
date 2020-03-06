class Pessoa:
    def __init__(self,nome:str,idade:str,sobrenome:str)->None:
        self.__nome = ''
        self.__idade = 0
        self.__sobrenome = ''

        if type(nome) == str:
            self.__nome = nome
        if self.verificar_idade(idade):
            self.__idade = idade
        if type(sobrenome) == str:
            self.__sobrenome = sobrenome

    def verificar_idade(self,idade):
        if type(idade)  == int and idade > 0:
            self.__idade = idade

    def getter_nome(self):
        return self.__nome

    def getter_idade(self):
        return self.__idade

    def getter_sexo(self):
        self.__sexo = self.__sexo
        return self.__sexo

    def setter_nome(self,nome):
        if type(nome) == str:
            self.__nome= nome

    def setter_idade(self,idade):
        if self.verificar_idade(idade):
            self.__idade = idade

    def setter_sexo(self,sobrenome):
        if type(sobrenome) == str:
            self.__sobrenome = sobrenome