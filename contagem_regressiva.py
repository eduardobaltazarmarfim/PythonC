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

        cabecalho('Contagem Regressiva')

        resp=input('Iniciar a contagem?[s/n] ')

    except:

        mensagem_erro()

        retorno()

    else:
        
        cont=10

        while resp=='s' or resp=='S':

            if(cont>=0):

                print(cont)
                sleep(1)

                cont-=1

            else:

                print('BOM! POW! POW!')
                break
                    
        retorno()

    pass


verificar()