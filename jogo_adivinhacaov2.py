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

        cabecalho('Jogo de Adivinhação V2')
        
        computador=random.randint(0,10)

        novoNumero=0

        cont=0

        while computador==novoNumero:

            computador=random.randint(0,10)
    
        novoNumero=computador

        usuario=11

        while usuario!=novoNumero:

            usuario=int(input('Qual o seu palpite? '))
            print('-'*30)

            if(usuario<novoNumero):

                print('Mais ...Tente novamente!')
                cont+=1

            elif(usuario>novoNumero):

                print('Menos ... Tente novamente!')
                cont+=1

        print('Parabéns você conseguiu acertar com {} tentativas.'.format(cont))
        
    except:

        mensagem_erro()

        retorno()
        
    pass

verificar()