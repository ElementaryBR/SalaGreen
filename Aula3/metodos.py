def soma(n1,n2):
    return n1 + n2

def multiplicacao(n1,n2,n3=1):
    return n1 * n2 * n3

def concatenando(n1,n2):
     return n1 + n2

n1 = int(input('\nDigite um valor: '))
n2 = int(input('\nDigite outro valor: '))
n3 = int(input('\nDigite mais um valor: '))

print(soma(n1,n2))
print(multiplicacao(n1,n2))

frase1 = input('\nDigite uma palavra ou uma frase: ')
frase2 = input('\nDigite mais uma palavra ou frase: ')

print(concatenando(frase1,frase2))

