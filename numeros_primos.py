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

        cabecalho('Números Primos')

        num=int(input('Digite um número inteiro: '))

    except:

        mensagem_erro()

        retorno()

    else:

        tot=0

        for i in range(1,num+1):

            if(num%i==0):
                print('\033[33m',end='')
                tot+=1

            else:

                print('\033[31m',end='')

            print('{} '.format(i),end='')
        
        if(tot==2):

            res='é número primo'

        else:

            res='não é número primo'

        print('\nO número foi divisível {} tantas vezes, mas ele {}!'.format(tot,res))
            
        retorno()

    pass

verificar()