import math
import random
import datetime
from time import sleep

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

        cabecalho('Validação de Dados')

        sexo='a'

        while sexo!='M' and sexo!='F':

            sexo=input('Informe o seu sexo [M/F]: ').upper()

        print('O seu sexo é {}'.format(sexo))

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass

verificar()