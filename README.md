# Cadastro de Restaurantes

Este é um aplicativo simples desenvolvido em Python, com o objetivo de gerenciar restaurantes. Ele permite cadastrar, listar, e ativar ou desativar restaurantes. O aplicativo foi criado durante um curso da Alura sobre programação em Python.

---
## Funcionalidades

- **Cadastrar Restaurante**: Adiciona um novo restaurante à lista.
- **Listar Restaurantes**: Exibe todos os restaurantes cadastrados, incluindo suas categorias e status (ativo ou desativado).
- **Ativar ou Desativar Restaurante**: Permite ativar ou desativar um restaurante já cadastrado.
- **Sair**: Encerra o aplicativo.
---
## Requisitos

- Python 3.x
- Biblioteca `os` (integrada no Python, utilizada para limpar a tela do terminal)
---
## Como Usar

1. Execute o script em seu terminal.
2. O nome do aplicativo será exibido na tela.
3. O menu com as opções será apresentado.
4. Escolha uma das opções digitando o número correspondente.
---
## Estrutura do Código
Funções do Aplicativo: 
- **exibir_nome_do_app()**: Exibe o nome do aplicativo na tela com uma arte ASCII.
- **exibir_menu()**: Exibe o menu de opções disponíveis para o usuário.
- **cadastrar_restaurante()**: Permite ao usuário cadastrar um novo restaurante, adicionando-o à lista.
- **listar_restaurantes()**: Exibe todos os restaurantes cadastrados, com informações sobre sua categoria e status (ativo ou desativado).
- **ativar_desativar_restaurante()**: Permite ao usuário ativar ou desativar um restaurante a partir de seu nome.
- **voltar_ao_menu()**: Aguarda a interação do usuário para retornar ao menu principal.
- **opcao_invalida()**: Exibe uma mensagem de erro quando o usuário escolhe uma opção inválida.
- **escolher_opcao()**: Gerencia a escolha da opção do menu e executa a função correspondente.
- **main()**: Função principal que gerencia o fluxo do aplicativo.
---
### Créditos

- **Desenvolvido como parte do curso da Alura sobre Python.**

