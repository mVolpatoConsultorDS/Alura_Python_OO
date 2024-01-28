# standard and best practices: Snake Case
import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
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
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurantes')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Encerrando o Programa')

def voltar_ao_menu_principal():
    input('Digite uma tecla para retornar ao menu principal ')
    main()

def opcao_invalida():
    print('Opcao Invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de Nuevos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que desejascadastrar: ')
    restaurantes.append(nome_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')

    for restaurante in restaurantes:
        print(f'.{restaurante}')

    #numero_tabuada = int(input("Digite um número para a tabuada: "))
    #for i in range(1, 11):
    #resultado = numero_tabuada * i
    #print(f"{numero_tabuada} x {i} = {resultado}")


    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opcao: '))
        # print(opcao_escolhida == 2)
        # print(type(opcao_escolhida))
        # print(type(1))
        # print(f'Voce escolheu a opcao {opcao_escolhida}')
        ##if opcao_escolhida > 0 and opcao_escolhida <=1:
        ##    print('true')
        ##else: print('false')
        #if 0 < opcao_escolhida <= 1:
        #    print('true')
        #else: print('false')
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print('Ativar Restaurantes')
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

# case structure
#opcao_escolhida = int(input('Escolha uma opção: '))
#match opcao_escolhida:
#    case 1:
#        print('Adicionar restaurante')
#    case 2:
#        print('Listar restaurantes')
#    case 3:
#        print('Ativar restaurante')
#    case 4:
#        print('Finalizar app')
#    case _:
#        print('Opção inválida!')

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()