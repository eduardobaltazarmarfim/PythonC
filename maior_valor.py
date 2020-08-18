import math
import random
import datetime

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

        cabecalho('Maior Valor')

        cont=0

        valores=list()

        for i in range(0,3):

            cont+=1

            num=int(input('Digite o {} valor: '.format(cont)))

            valores.append(num)
            
    except:

        mensagem_erro()

        retorno()

    else:

        valores.sort()

        print('O menor valor é {}'.format(valores[0]))
        print('O maior valor é {}'.format(valores[2]))

        retorno()

    pass


verificar()