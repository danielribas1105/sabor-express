import os

restaurantes = ['Pizza', 'Sushi']

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
   print('3. Ativar restaurante')
   print('4. Sair')

def opcao_invalida():
   print('Opção inválida!')
   input('Digite uma tecla para voltar ao menu principal')
   main()

def cadastrar_novo_restaurante():
   os.system('cls')
   print('Cadastro de novo restaurante\n')
   nome_restaurante = input('Digite o nome do restaurante para cadastro: ')
   restaurantes.append(nome_restaurante)
   print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso')
   input('\nDigite uma tecla para voltar ao menu principal')
   main()

def listar_restaurantes():
   os.system('cls')
   print('Listando restaurantes cadastrados\n')
   for restaurante in restaurantes:
      print(f'. {restaurante}\n')
   input('\nDigite uma tecla para voltar ao menu principal')
   main()

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
            print('Ativar restaurante')
         case 4:
            finalizar_app()
         case _:
            opcao_invalida()
   except:
      opcao_invalida()

def finalizar_app():
   os.system('cls')
   print('App finalizado!\n')

def main():
   exibir_nome_app()
   exibir_opcoes()
   escolher_opcao()

if __name__ == '__main__':
   main()