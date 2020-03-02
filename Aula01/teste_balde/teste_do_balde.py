from Aula01.teste_balde.balde import Balde

a = Balde()

print('#'*40,'\nVerificando se o balde inicia vazio!\n')
assert a._Balde__balde == 0, 'Erro! O Balde() não iniciou vazio'\
                           'ou a variável privada não é __balde!'
assert a._Balde__balde_atual == 0, 'Erro! O Balde() não iniciou vazio'\
                           'ou a variável privada não é __balde_atual!'
print('Balde iniciou vazio: OK\n')

a = Balde()
print('#'*40,'\nAdicionando volume (10 a 50) no Balde!\n')
lista = [x for x in range(10,51)]
for i in lista:
    assert a.set_volume_balde(i), f'Erro! set_volume_balde({i}) deve adicionar {i}!'
    assert a._Balde__balde == i, f'Erro! set_volume_balde({i}) não adicionou volume correto no balde!'
print('Volume do balde alterado: OK\n')

a = Balde()
print('#'*40,'\nVerificando filtro do volume (10 a 50) do Balde!\n')
lista = [x for x in range(10)]+[x for x in range(51,1001)]
for i in lista:
    assert not a.set_volume_balde(i) , f'Erro! set_volume_balde({i}) não pode aceitar volumes'\
                                       'abaixo de 9 e  acima de 51!'
print('Filtro do volume do balde: OK\n')

a = Balde()
print('#'*40,'\nVerificando filtro do volume para números negativos do Balde!\n')
lista = [x*-1 for x in range(1000)]
for i in lista:
    assert not a.set_volume_balde(i) , f'Erro! set_volume_balde({i}) não pode aceitar volumes'\
                                       'negativos!'
print('Filtro do volume para números negativos: OK\n')

a = Balde()
print('#'*40,'\nVerificando filtro do volume para caracteres!\n')
lista = [str(x) for x in range(1000)]+['a'*i for i in range(1000)]
for i in lista:
    assert not a.set_volume_balde(i) , f'Erro! set_volume_balde({i}) não pode aceitar string!'
print('Filtro do volume para caracteres: OK\n')

print('#'*40,'\nVerificando o volume do balde!\n')
lista = [x for x in range(10,51)]
for i in lista:
    a.set_volume_balde(i)
    assert a.get_volume_balde() == a._Balde__balde, f'Erro! get_volume_balde() não retornou {a._Balde__balde}!'
print('Verificando o volume do balde: OK\n')

a = Balde()
print('#'*40,'\nVerificando enchendo o do balde!\n')
lista = [x for x in range(10,51)]
for i in lista:
    a = Balde()
    a.set_volume_balde(i)
    contador=0
    for j in range(i):
        a.enchendo_balde(1)
        contador += 1
        assert contador == a._Balde__balde_atual, f'Erro! a.enchendo_balde() não está enchendo balde!'
print('Verificando enchendo o do balde: OK\n')

a = Balde()
print('#'*40,'\nVerificando enchendo balde resposta!\n')
lista = [x for x in range(10,51)]
for i in lista:
    a = Balde()
    a.set_volume_balde(i)
    for j in range(i+1):
        if a._Balde__balde_atual < a._Balde__balde:
            if a._Balde__balde_atual+1 == a._Balde__balde:
                assert a.enchendo_balde(1), f'Erro! enchendo_balde(), quando cheio, deve retornar True!' \
                                            f'Volume total: {a._Balde__balde}   Volume Atual: {a._Balde__balde_atual}'
            else:
                assert a.enchendo_balde(1) == 'Vazio', f'Erro! enchendo_balde(), quando enchendo, deve retornar Vazio!' \
                                                       f'Volume total: {a._Balde__balde}   Volume Atual: {a._Balde__balde_atual}'

        elif a._Balde__balde_atual == a._Balde__balde:
            assert not a.enchendo_balde(1), f'Erro! enchendo_balde(), quando tranbordando, deve retornar False!'\
                                                   f'Volume total: {a._Balde__balde}   Volume Atual: {a._Balde__balde_atual}'

print('Verificando enchendo balde resposta: OK\n')

a = Balde()
print('#'*40,'\nVerificando filtro do enchendo balde para números negativos!\n')
lista = [x*-1 for x in range(1000)]
for i in lista:
    assert a.enchendo_balde(i) == 'ValorError' , f'Erro! a.enchendo_balde({i}) não pode aceitar volumes'\
                                       'negativos!'
print('Filtro do volume para números negativos enchendo balde!: OK\n')

a = Balde()
print('#'*40,'\nVerificando filtro do enchendo balde para caracteres!\n')
lista = [str(x) for x in range(1000)]+['a'*i for i in range(1000)]
for i in lista:
    assert a.enchendo_balde(i) == 'ValorError', f'Erro! enchendo_balde({i}) não pode aceitar string!'
print('Filtro do enchendo balde para caracteres: OK\n')

a = Balde()
print('#'*40,'\nVerificando metodo sorteio!\n')

for i in range(1000):
    anterior = a._Balde__balde
    a.sorteio()
    contador = 0
    while a._Balde__balde == anterior and contador <= 3:
        contador += 1
        a.sorteio()
        if contador == 3:
            assert a._Balde__balde != anterior, 'Erro!! sorteio() não está alterando o volume do balde!'
    assert a._Balde__balde >=10 and a._Balde__balde <=50, f'Erro! sorteio() está sorteando números inválidos!'
print('Soreteio: OK\n')

print('\n'*3,'Teste Conculido com Sucesso!')

