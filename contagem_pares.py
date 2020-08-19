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

        cabecalho('Contagem de Pares')

        inicial=int(input('Digite o número inicial da contagem: '))

        final=int(input('Digite um número final de contagem: '))

    except:

        mensagem_erro()

        retorno()

    else:

        valores=list()

        if(inicial>final):

            print('O número inicial é maior que o número final!')
                        
        else:

            for i in range(inicial,final+1):

                if(i%2==0):

                    valores.append(i)

            print(valores)

        retorno()

    pass


verificar()