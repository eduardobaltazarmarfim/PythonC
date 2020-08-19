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

        cabecalho('Tabuada V2')

        num=int(input('Digite o número inicial da contagem: '))

        print('''
        Escolha uma Opção:\n\n[1] - Tabuada Simples\n[2] - Tabuada Acumulativa
        ''')

        print('-'*30)

        opcao=int(input('Digite uma das duas opções: '))

        print('-'*30)

    except:

        mensagem_erro()

        retorno()

    else:

        if(opcao>2):

            print('Favor informar uma das opções informadas!')

        else:

            opcoes={1:tabuada,2:tabuada_acumulativa}

            opcoes.get(opcao)(num)

        retorno()

    pass


def tabuada_acumulativa(x):

    cont=0
    valores=0

    for i in range(1,11):
        
        cont+=1

        if(cont<=1):
            
            res=i*x
            
            print('{}x{}= {}'.format(i,x,res))

        else:

            valores=res
            res=valores*i

            print('{}x{}= {}'.format(i,valores,res))     

    pass


def tabuada(x):

    for i in range(0,11):

        res=i*x

        print('{}x{}= {}'.format(i,x,res))

    pass

verificar()