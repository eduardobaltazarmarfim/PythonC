from os import system

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]: ').lower()[0]

        if resp in 'sn':

            break

        mensagem_erro()

    if resp=='s':

        analisar()

    else:

        print('Processo finalizado!')

    pass


def cabecalho(titulo):

    tam=len(titulo)+4

    print('-'*tam)
    
    print(f'  {titulo}')

    print('-'*tam)

    pass


def analisar():

    try:

        system('cls')

        cabecalho('Validando Dados')

        leiaint=int(input('Digite um número: '))
        
    except:

        mensagem_erro()

        retorno()

    else:

        validar_dados(leiaint)

    pass


def validar_dados(num):

    print('O valor digitado é {}'.format(num))

    pass

analisar()