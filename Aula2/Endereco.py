

class Endereco:
    def __init__(self, rua:str, cep:str, cidade:str) -> None:
        self.__rua = ''
        self.__cep = ''
        self.__cidade = ''

        if type(rua) == str:
            self.__rua = rua
        if type(cep) == str:
            self.__cep = cep
        if type(cidade) == str:
            self.__cidade = cidade

    def getter_rua(self):
        return self.__rua

    def getter_cep(self):
        return self.__cep

    def getter_cidade(self):
        return self.__cidade

    def setter_rua(self,rua):
        if type(rua) == str:
            self.__rua= rua

    def setter_cep(self,cep):
        if type(cep) == str:
            self.__cep = cep

    def setter_cidade(self,cidade):
        if type(cidade) == str:
            self.__cidade = cidade

endereco = Endereco('Alfredo Bauer', '89068220', 'Blumenau')