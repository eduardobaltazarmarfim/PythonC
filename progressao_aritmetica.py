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

        cabecalho('10 Termos de uma PA')

        inicial=int(input('Primeiro Termo: '))

        final=int(input('Razão: '))

    except:

        mensagem_erro()

        retorno()

    else:

        valores=list()

        if(inicial>final):

            print('Dados inseridos não são validos!')

        else:

            cont=10*final

            for i in range(inicial,cont,final):

                valores.append(i)

            print(valores)
 
        retorno()

    pass


verificar()