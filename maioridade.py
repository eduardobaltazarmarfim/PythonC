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

        valores=list()

        maior=0

        menor=0

        for i in range (1,6):

            peso=int(input('Digite a {}º peso: '.format(i)))
            valores.append(peso)

        print(valores)
 
    except:

        mensagem_erro()

        retorno()

    else:

        p=0

        for i in range(0,5):
            
            p=valores[i]

            if(i==0):

                maior=p
                menor=p
            
            else:

                if(p>maior):

                    maior=p

                elif(p<menor):

                    menor=p
           

        print('O maior número da lista é {}'.format(maior))
        print('O menor número da lista é {}'.format(menor))

        retorno()

    pass

verificar()