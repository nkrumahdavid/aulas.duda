print('Exemplo 07')
n = float(input('Digite um número: '))
print(n)

print('Exemplo 08')
n = bool(input('Digite alguma coisa: '))
print('Digitei algo. Certo?')
print(n)

print('Exemplo 09')
n = input('Digite outro número.')
print('Digitei um número. Certo?')
print(n.isnumeric())

print('Exemplo 10')
n = input('Digite uma palavra: ')
print('Digitei uma palavra. Certo?')
n = input(n.isalpha())

print('Exemplo 11')
n = input('Digite qualquer coisa. ')
print('Digitei. Certo?')
n = input(n.isalnum())

print('Exemplo 12')
n = input('Digite seu nome com letras maiúsculas ')
print('Fiz o que pediu. Certo?')
n = input(n.isupper())