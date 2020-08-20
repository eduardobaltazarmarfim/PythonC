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

        cabecalho('Detector de Palíndromo')

        frase=input('Digite uma frase: ').strip().upper()

        separar=frase.split()

        juntar= ''.join(separar)
 
    except:

        mensagem_erro()

        retorno()

    else:
        
        inverso=''

        for i in range(len(juntar)-1,-1,-1):

            inverso+=juntar[i]

        print(inverso)

        retorno()

    pass

verificar()