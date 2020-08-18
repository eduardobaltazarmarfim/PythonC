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

        cabecalho('Primeiro e Último Nome')
        
        nome=input('Digite seu nome completo: ')

    except:

        mensagem_erro()

        retorno()

    else:

        copia=nome.split()

        num=len(copia)

        print('O seu nome primeiro nome é {}'.format(copia[0]))
        print('O seu nome último nome é {}'.format(copia[num-1]))

        retorno()

    pass

verificar()