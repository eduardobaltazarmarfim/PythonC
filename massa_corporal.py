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

        cabecalho('Índice Massa de Corporal')

        peso=float(input('Digite seu peso: '))
        altura=float(input('Digite sua altura: '))
        
    except:

        mensagem_erro()

        retorno()

    else:
        
        imc=peso/(altura**2)

        if(imc<=18.5):

            print('Abaixo do peso!')

        elif(imc>18.5 and imc<=25):

            print('Peso ideal!')

        elif(imc>25 and imc<=30):

            print('Sobrepeso')

        elif(imc>30 and imc<=40):

            print('Obesidade')

        else:

            print('Obesidade mórbida')

        retorno()

    pass


verificar()