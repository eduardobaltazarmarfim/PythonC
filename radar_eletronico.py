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

        cabecalho('Radar Eletrônico')

        num=int(input('Qual é a velocidade atual do carro: '))

    except:

        mensagem_erro()

        retorno()

    else:

        if(num>80):

            diferença=num-80

            multa=diferença*7

            print('Você foi multado o valor de sua multa é de {:.2f}!'.format(multa))

        else:

            print('Você está dentro da velocidade!')


        retorno()

    pass


verificar()