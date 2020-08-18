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

        cabecalho('Analisando Triângulo')

        cont=0

        dados=list()

        for i in range(0,3):

            cont+=1

            valor=float(input('Digite o {}º valor: '.format(cont)))
            
            dados.append(valor)
        
    except:

        mensagem_erro()

        retorno()

    else:
        
        r1=dados[0]
        r2=dados[1]
        r3=dados[2]

        if(r1<r2+r3 and r2<r1+r3 and r3<r2+r1):

            print('A três medidas formam um triângulo ',end='')

            if(r1==r2==r3):

                print('Equilátero')

            elif(r1!=r2!=r3!=r1):

                print('Escaleno')

            else:

                print('Isósceles')

        else:

            print('A três medidas não formam um triângulo')

        retorno()

    pass


verificar()