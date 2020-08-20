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

        cabecalho('Grupo de Maioridade')

        x=0
        valores=list()

        for i in range (0,7):

            x+=1

            ano=int(input('Digite a {}º ano de nascimento: '.format(x)))
            valores.append(ano)
 
    except:

        mensagem_erro()

        retorno()

    else:

        maior=0
        menor=0
        
        dataAtual=datetime.date.today().year

        for i in range(0,7):

            idade=0

            idade=dataAtual-valores[i]

            if(idade>=18):

                maior+=1

            else:

                menor+=1

        print('Na lista informada temos {} pessoas maior de idade. E {} pessoas menor de idade!'.format(maior,menor))

        retorno()

    pass

verificar()