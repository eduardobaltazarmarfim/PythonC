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

        cabecalho('Conversor de Bases Númericas')

        num=int(input('Digite um valor: '))
        
        print('-'*30)

        print('''Escolha as opções para conversão:\n[1] - Binário\n[2] - Octal\n[3] - Hexadecimal''')

        print('-'*30)

        opcao=int(input('Digite uma das 3 opções: '))

    except:

        mensagem_erro()

        retorno()

    else:

        if(opcao>0 and opcao<=3):

            opcoes={1:binario,2:octal,3:hexadecimal}

            opcoes.get(opcao)(num)

        else:

            print('A função informada não existe!')            

        retorno()

    pass

def binario(x):

    print('{} convertido em binário é igual a {}'.format(x,bin(x)[2:]))

    pass

def octal(x):

    print('{} convertido em binário é igual a {}'.format(x,oct(x)[2:]))

    pass


def hexadecimal(x):

    print('{} convertido em binário é igual a {}'.format(x,hex(x)[2:]))

    pass


verificar()