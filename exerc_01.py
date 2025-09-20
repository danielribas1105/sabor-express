print("""
Python na Escola de Programação da Alura
""")

""" nome = input("Informe seu nome: ")
idade = input("Informe sua idade: ")
print(f'Meu nome é {nome} e tenho {idade} anos') """

print('''
A
L
U
R
A
''')

print('A','L','U','R','A',sep='\n')

pi = 3.14159
# Abordagem de f-string
print(f'\nO valor arredondado de pi é: {pi:.2f}')

# Abordagem de .format()
print('\nO valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
print(f'\nO valor arredondado de pi é: {round(pi, 2)}')

lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in lista_de_numeros:
    print(numero)