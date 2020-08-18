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

        cabecalho('Custo da Viagem')

        num=int(input('Qual a distância de sua viagem: '))

    except:

        mensagem_erro()

        retorno()

    else:


        if(num<=200):

            valor=num*0.50

            print('O valor total da passagem R$ {:.2f}!'.format(valor))

        else:

            valor=num*0.45

            print('O valor total da passagem R$ {:.2f}!'.format(valor))            

        retorno()

    pass


verificar()