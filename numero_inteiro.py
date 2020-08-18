import math

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

    esquerda=35-medida

    direita=medida

    print('-'*cont)

    print(' '*esquerda+texto+' '*direita)

    print('-'*cont)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:

        cabecalho('Conveter Real para Inteiro')

        valor=float(input('Digite um valo real '))

    except:

        mensagem_erro()

        retorno()

    else:

        inteiro=math.trunc(valor)

        print('O número digitado é {} e sua porção inteira é {}'.format(valor,inteiro))

        retorno()

    pass

verificar()