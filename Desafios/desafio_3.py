print('1 - Crie uma lista para cada informação a seguir:\n')

print('Lista de números de 1 a 10.')
numeros_de_1_a_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Lista com quatro nomes.')
nomes = ['João', 'Maria', 'José', 'Ana']

print('Lista com o ano que você nasceu e o ano atual.')
nascimento_e_atual = [2003, 2024]

print('\n2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.')
for numero in numeros_de_1_a_10:
    print(numero)

print('\n3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.')
soma = 0
for numero in numeros_de_1_a_10:
    if numero % 2 != 0:  # Verifica se o número é ímpar
        soma += numero
print(soma)

print('\n4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.')
for numero in numeros_de_1_a_10[::-1]: #slice para inverter a lista
    print(numero)

print('\n5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.')
numero_solicitado = int(input('Digite um número: '))
print(f'Tabuada do {numero_solicitado}: ')
for i in range(1, 11):
    print(f'{numero_solicitado} x {i} = {numero_solicitado * i}')

print('\n6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.')
numeros_aleatorios = [10, 'b', 20, 30, 40, 50]
soma2 = 0
for numero in numeros_aleatorios:
    try:
        soma2 += numero
    except TypeError as e:
        print(f"Erro ao somar {numero}: {e}")  # Lida com valores que não podem ser somados
print(f'A soma de todos os elementos é: {soma2}')

print('\n7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.')

def calcular_media(lista):
    try:
        media = sum(lista) / len(lista)
        print(f'A média dos valores é: {media}')
    except ZeroDivisionError as e:
        print(f'Erro ao calcular a média: {e}')

calcular_media([10, 20, 30, 40, 50])