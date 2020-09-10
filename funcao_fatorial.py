from os import system
from time import sleep

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]').lower()[0]

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

        cabecalho('Função Fatorial')
    
        fatorial(5)

    except:

        mensagem_erro()

        retorno()

    pass

def fatorial(num,show=False):

    '''
    -> Calcula o fatorial de um número.
    :parâmetro num valor fatorial para calculo
    :show ele aceita valores True/False
    :e o calulo é realizado exemplo:
    :5x4x3x2x1=120

    '''

    multiplique=1

    for i in range(num,0, -1):

        if show==True:

            if i==1:

                print(f'{i} = ',end='',flush=True)

            else:

                print(f'{i} x ',end='',flush=True)

            sleep(1)
        multiplique*=i
        
    print('{}'.format(multiplique))

    pass

help(fatorial)