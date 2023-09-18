'''Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
'''


letra = str(input('Digite uma Letra: ')).upper()
while letra != 'F' and letra != 'M':
    print('Letra inválida. Por favor, digite M ou F.')
    letra = str(input('Digite uma Letra: ')).upper()

if letra == 'M':
     print(f' Letra {letra} - FEMININO ')
if letra == 'F':
    print(f'letra {letra} - MASCULINO')



