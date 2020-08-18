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

        cabecalho('Classificação de Atleta')

        nascimento=int(input('Digite seu ano de nascimento: '))

    except:

        mensagem_erro()

        retorno()

    else:
 
        dataAtual=datetime.date.today().year

        idade=dataAtual-nascimento

        if(idade<=9):

            print('Classificação Mirim')

        elif(idade>9 and idade<=14):

            print('Classificação Infantil')

        elif(idade>14 and idade<=19):

            print('Classificação Junior')

        elif(idade>19 and idade<=25):

            print('Classificação Sênior')

        else:

            print('Classificação Master')

        retorno()

    pass


verificar()