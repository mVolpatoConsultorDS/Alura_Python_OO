# standard and best practices: Snake Case
import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

# Para contar a frequência de cada palavra em uma frase, você pode utilizar o seguinte código:
#frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
#contagem_palavras = {}
#palavras = frase.split()
#for palavra in palavras:
#    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
#print(contagem_palavras)


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
    print('3. Alternar Estado dos Restaurantes')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para retornar ao menu principal ')
    main()

def finalizar_app():
    exibir_subtitulo('Encerrando o Programa')

def opcao_invalida():
    print('Opcao Invalida\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto) + 4) 
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa funcao e responsavel por cadastrar um novo Restaurante

    Inputs:
    - Nome do Restaurante
    - Categoria

    Outputs
    - Adiciona um novo restaurante a lista de restaurantes
    
    '''
    exibir_subtitulo('Cadastro de Nuevos Restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que desejascadastrar: ')
    categoria = input(f'Digite  o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando Restaurantes')

    print(f'{'Nome do Restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f' - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    #numero_tabuada = int(input("Digite um número para a tabuada: "))
    #for i in range(1, 11):
    #resultado = numero_tabuada * i
    #print(f"{numero_tabuada} x {i} = {resultado}"
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando Estado do Restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_econtrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_econtrado = True
            restaurante['ativo'] = not restaurante['ativo']
            # Estrutura ternaria
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_econtrado:
        print('O restaurante nao foi encontrado')
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
            alternar_estado_restaurante()
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