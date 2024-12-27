print('1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.') 
informacoes_das_pessoas = ({'nome':'João', 'idade':21, 'cidade':'salvador'},
                           {'nome':'Vinicius', 'idade':21, 'cidade': 'Cuiaba'})

print('\n2 - Utilizando o dicionário criado no item 1:')
print('Modifique o valor de um dos itens no dicionário por exemplo, atualize a idade da pessoa.') 
informacoes_das_pessoas[0]['idade'] = 22
print('\nAdicione um campo de profissão para essa pessoa.') 
for pessoa in informacoes_das_pessoas:
    pessoa['profissao'] = 'Estudante'
print('\nRemova um item do dicionário.') 
for pessoa in informacoes_das_pessoas:
    del pessoa['cidade']

print('\n3 - Crie um dicionário utilizando para representar números e seus quadrados de 1 a 5.') 
numeros_e_quadrados = {numero: numero**2 for numero in range(1,6)} # ** calcula a potência 
print(numeros_e_quadrados)

print('\n4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.') 
nome_e_tamanho = {'nome':'João', 'tamanho': 1.75}
chave = 'tamanho'
if chave in nome_e_tamanho:
    print(f'A chave {chave} existe no dicionário')
else:
    print(f'A chave {chave} não existe no dicionário')

print('\n5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.') 

frase = 'Pedro tem um gato e João tem dois gatos, mas João queria ter um cachorro'
palavras = frase.split()
frequencias = {}

for palavra in palavras: 
    if palavra in frequencias:
        frequencias[palavra] += 1
    else:
        frequencias[palavra] = 1

for palavra, frequencia in frequencias.items():
    if frequencia == 1:
        print(f'A palavra "{palavra}" apareceu {frequencia} vez nessa frase.')
    else:
        print(f'A palavra "{palavra}" apareceu {frequencia} vezes nessa frase.')