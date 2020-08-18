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

        cabecalho('Aumento Multíplos')

        valor=float(input('Qual é o seu salário atual: '))

    except:

        mensagem_erro()

        retorno()

    else:

        if(valor>1250):

            novoValor=valor*(1+0.10)

            print('O salário antigo era de R$ {:.2f} o atual com o reajuste de {:.2f} ficou R$ {:.2f}'.format(valor,10,novoValor))

        else:

            novoValor=valor*(1+0.15)

            print('O salário antigo era de R$ {:.2f} o atual com o reajuste de {:.2f} ficou R$ {:.2f}'.format(valor,15,novoValor))

        retorno()

    pass


verificar()