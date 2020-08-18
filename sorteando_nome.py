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

    cont=medida+30

    esquerda=math.trunc((medida-5)/2)

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

        cabecalho('Sorteando Nome')

        listaNome=list()

        x=0

        for i in range(0,4):

            x+=1

            nome=str(input('Digite o {}º nome: '.format(x)))

            listaNome.append(nome)

    except:

        mensagem_erro()

        retorno()

    else:

        sorte=random.choice(listaNome)

        print('O nome escolhido é {}.'.format(sorte))

        retorno()

    pass


verificar()