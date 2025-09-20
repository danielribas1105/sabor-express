import os

restaurantes = [{'nome':'Pizza da Nona', 'categoria':'Pizzas', 'ativo': False}, 
                {'nome':'Shushi da Praça', 'categoria':'Japa', 'ativo': True},
                {'nome':'Kilograma', 'categoria':'Kilo', 'ativo': True},
]


def exibir_nome_app():
    print("""

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar estado restaurante')
    print('4. Sair')

def opcao_invalida():
    print('Opção inválida!')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)

def cadastrar_novo_restaurante():
    '''Função para realizar o cadastro de novos restaurantes
    Inputs:
    - Nome do restaurante
    - Categoria do restaurante
    
    Output:
    - Acrescenta um restaurante a lista de restaurantes
    '''
    exibir_subtitulo('Cadastro de novo restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante para cadastro: ')
    categoria = input('\nDigite o nome da categoria: ')
    dados_restaurante = {'nome': nome_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso')
    voltar_menu_principal()

def listar_restaurantes():
    '''Essa função lista os restaurantes cadastrados'''
    exibir_subtitulo('Listando restaurantes cadastrados')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'. {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}\n')
    voltar_menu_principal()

def alterar_estado_restaurante():
    '''Função para alternar o estado de um restaurante'''
    exibir_subtitulo('Alterando estado do restaurante\n')
    nome_restaurante = input('Digite o nome do restaurante para alterar o estado: ')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado.')
    voltar_menu_principal()

def escolher_opcao():
    try:
        opcao_selecionada = int(input('\nEscolha uma opção: '))
        print(f'Você escolheu a opção {opcao_selecionada}')
        match opcao_selecionada:
            case 1:
                cadastrar_novo_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alterar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    exibir_subtitulo('App finalizado!\n')

def voltar_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def main():
    exibir_nome_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
