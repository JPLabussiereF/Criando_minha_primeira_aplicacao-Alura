import os #os é uma biblioteca usada para limpar a tela do terminal

restaurantes = [{'nome':'Podrão do Labussiere', 'categoria':'Boteco', 'ativo':False}, 
                {'nome':'Pastelaria do tio Naiser', 'categoria': 'Pastelaria', 'ativo':False},
                {'nome':'Massas do Candinho', 'categoria': 'Massas', 'ativo':True}]

def exibir_nome_do_app():
    '''Essa função exibe o nome do Aplicativo.'''
    print('''
    ██████████████████████████████████████████████████████████████████████████
    █─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
    █▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
    ▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
    ''')

def exibir_menu():
    '''Essa função exibe o menu de opções do aplicativo'''
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar ou Desativar Restaurantes')
    print('4. Sair\n')

def voltar_ao_menu():
    '''Essa função exibe uma mensagem e aguarda o usuário digitar qualquer tecla para voltar ao menu.
    
    Input: 
    - Qualquer tecla

    Output:
    - Menu do aplicativo

    '''
    input('\nDigite qualquer tecla para voltar ao menu.\n')
    main()

def exibir_subtitulo(subtitulo):
    '''Essa função exibe um subtitulo com base no texto passado.'''
    os.system('cls')
    traco = '-' * (len(subtitulo) + 2)
    print(f'{traco}')
    print(f'|{subtitulo}|')
    print(f'{traco}')
    print()

# Regra de negócio: Todo restaurante criado deve ser cadastrado como desativado.
def cadastrar_restaurante():
    '''Essa função cadastra um restaurante na lista de restaurantes.
    
    Inputs:
    - Nome do Restaurante: str
    - Categoria do Restaurante: str

    Output:
    - Restaurante colocado na Lista Dicionario de Restaurantes
    - Mensagem de Sucesso

    '''
    exibir_subtitulo('Bem Vindo ao Cadastro de Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    restaurantes.append({'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False})
    print(f'\nRestaurante {nome_do_restaurante} cadastrado com sucesso!')
    voltar_ao_menu()

def listar_restaurantes():
    '''Essa função lista todos os restaurantes cadastrados na lista de restaurantes.'''
    exibir_subtitulo('Listagem de Restaurantes')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        status_restaurante = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante}, cadastrado com a categoria {categoria_restaurante} está {status_restaurante}!')
    voltar_ao_menu()

def ativar_desativar_restaurante():
    '''Essa função ativa ou desativa um restaurante na lista de restaurantes.
    
    Input: 
    - Nome do restaurante: str

    Output:
    - Ativação ou Desativação do Restaurante na lista de restaurantes

    '''
    exibir_subtitulo('Ativação ou Desativação de Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            # Operador ternário: É uma forma compacta de usar 'if-else' em uma única linha. 
            #Estrutura: resultado = valor_se_true if condição else valor_se_false
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado!' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O restaurante {nome_do_restaurante} não foi encontrado!')
    voltar_ao_menu()


def encerrar_programa():
   '''Essa função encerra o aplicativo.'''
   exibir_subtitulo('Encerrando o Programa! Obrigado pela Preferência')

def opcao_invalida():
    '''Essa função exibe uma mensagem de opção inválida volta ao menu através da função "voltar_ao_menu".'''
    print('\nOpção Inválida!\n')
    voltar_ao_menu()

def escolher_opcao(): 
    '''Essa função aguarda o usuário escolher uma opção do menu e chama a função correspondente a opção escolhida.
    
    Input:
    - Opção Escolhida: int

    Output:
    - Função correspondente a opção escolhida

    '''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            ativar_desativar_restaurante()
        elif opcao_escolhida == 4:
            encerrar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Essa função é a função principal do aplicativo.
    
    Output:
    - Limpar a tela
    - Nome do Aplicativo
    - Menu do Aplicativo
    - Escolher Opção do Menu

    '''
    os.system('cls')
    exibir_nome_do_app()
    exibir_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()