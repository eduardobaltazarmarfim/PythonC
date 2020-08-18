import math
import random

def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
                
        verificar()
        
            
    else:

        print('Processo finalizado!')

    pass


def cabecalho(texto):

    medida=len(texto)

    cont=medida+20

    esquerda=math.trunc(medida/2)

    direita=math.trunc(medida/2)

    print('-'*cont)

    print(' '*esquerda+texto+' '*direita)

    print('-'*cont)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:

        cabecalho('Par e Ímpar')

        num=int(input('Digite um número inteiro: '))

    except:

        mensagem_erro()

        retorno()

    else:

        if(num%2==0):

            print('Número {} é par.'.format(num))

        else:

            print('Número {} é ímpar.'.format(num))

        retorno()

    pass


verificar()