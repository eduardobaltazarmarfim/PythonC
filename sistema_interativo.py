from os import system

def cabecalho(titulo,cor=0):

    tam=len(titulo)+4

    print('~'*tam)

    print(f'  {titulo}')

    print('~'*tam)

    pass

def analisar():

    system('cls')
    
    comando=''

    while True:

        cabecalho('Sistema de Ajuda PyHelp')

        comando=str(input('Função Biblioteca: '))

        if comando.upper()=='FIM':

            break

        else:

            ajuda(comando)

        cabecalho('Até Logo')

    pass


def ajuda(funcoes):

    help(funcoes)

    pass

analisar()