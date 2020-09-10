from os import system

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]: ').lower()[0]

        if(resp in 'sn'):

            break
        
        print('Digite uma resposta valida S ou N')

    if(resp=='s'):

        verificar()

    else:

        print('Processo finalizado')

    pass


def cabecalho(titulo):

    print('-'*30)

    print('{:^30}'.format(titulo))

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    texto=input('Digite um texto: ')

    escreva(texto)

    retorno()

    pass


def escreva(titulo):

    qtde=len(titulo)+4

    print('~'*qtde)

    print(f'  {titulo}')

    print('~'*qtde)

    pass

verificar()