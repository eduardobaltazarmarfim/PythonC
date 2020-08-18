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

        cabecalho('Alistamento Militar')

        nascimento=int(input('Digite seu ano de nascimento: '))

    except:

        mensagem_erro()

        retorno()

    else:
 
        anoAtual=datetime.date.today().year

        idade=anoAtual-nascimento

        anoListamento=nascimento+18

        anoRestantte=18-idade

        if(idade<18):

            print('Você tem {} anos e você vai se alistar em {} falta ainda {} anos!'.format(idade,anoListamento,anoRestantte))

        elif(idade>18):

            print('Você tem {} anos e você já passou do periódo de alistamento {}'.format(idade,anoListamento))

        else:

            print('Você tem {} anos e já está na hora de se alistar.'.format(idade))

        retorno()

    pass


verificar()