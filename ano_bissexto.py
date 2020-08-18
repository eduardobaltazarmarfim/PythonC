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

        cabecalho('Ano Bissexto')

        num=int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))

    except:

        mensagem_erro()

        retorno()

    else:

        if(num==0):

            num=datetime.date.today().year
        
        if(num%4==0 and num%100!=0 or num%400==0):

            print('Ano informado {} é Bissexto!'.format(num))

        else:

            print('Ano informado {} não é Bissexto!'.format(num))

        retorno()

    pass


verificar()