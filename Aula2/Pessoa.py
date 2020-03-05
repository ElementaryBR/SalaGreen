# Crie uma clase Pessoa
# a classe deve conter 3 atributos
# a classe deve conter 6 metodos

class Pessoa:
    def __init__(self,nome, idade , sexo):
        self.__nome = nome
        self.__idade = idade
        self.__sexo = sexo
        self.endereco = Endereco('','','','')

    def getter_nome(self):
        self.__nome = self.__nome
        return self.__nome

    def getter_idade(self):
        self.__idade =self.__idade
        return self.__idade

    def getter_sexo(self):
        self.__sexo = self.__sexo
        return self.__sexo

    def setter_nome(self,nome):
        self.__nome= nome

    def setter_idade(self,idade):
        self.__idade = idade

    def setter_sexo(self,sexo):
        self.__sexo = sexo

class Endereco:
    def __init__(self, rua, cep, cidade, estado):
        self.__rua = rua
        self.__cep = cep
        self.__cidade = cidade
        self.__estado = estado

    def getter_rua(self):
        self.__rua = self.__rua
        return self.__rua

    def getter_cep(self):
        self.__cep =self.__cep
        return self.__cep

    def getter_cidade(self):
        self.__cidade = self.__cidade
        return self.__cidade

    def getter_estado(self):
        self.__estado = self.__estado
        return self.__estado

    def setter_rua(self,nome):
        self.__rua= nome

    def setter_cep(self,idade):
        self.__cep = idade

    def setter_cidade(self,sexo):
        self.__cidade = sexo

    def setter_estado(self,sexo):
        self.__estado = sexo

class Engenheiro(Pessoa):
    def __init__(self,area, numero):
        super().__init__()
        self.area = area
        self.numero_registro = numero

    def getter_area(self):
        self.area = self.area
        return self.area

    def getter_numero_rgs(self):
        self.numero_registro = self.numero_registro
        return self.numero_registro

    def setter_area(self,area):
        self.area = area

    def setter_num_regs(self,numero):
        self.numero_registro = numero



if __name__ == '__main__':
    a = Pessoa('Junin',23,'Macho')
    a.endereco.setter_rua('Alfredo Bauer')
    a.endereco.setter_cep('89068-220')
    a.endereco.setter_cidade('Blumenau')
    a.endereco.setter_estado('SC')
    a.endereco.getter_cidade()
    a.endereco.getter_rua()
    a.endereco.getter_cep()
    a.endereco.getter_estado()
    a.setter_nome('Juninhooo')
    a.getter_nome()

# 'Alfredo Bauer','89068-220','Blumenau','SC'