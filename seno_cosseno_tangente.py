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

        cabecalho('Calculo de seno, Cosseno e Tangente')

        val=float(input('Digite um ângulo: '))

    except:

        mensagem_erro()

        retorno()

    else:

        cos=math.cos(math.radians(val))
        sen=math.sin(math.radians(val))
        tan=math.tan(math.radians(val))

        print('O seno de {} é {:.2f}.'.format(val,sen))
        print('O Cosseno de {} é {:.2f}.'.format(val,cos))
        print('O Tangente de {} é {:.2f}.'.format(val,tan))

        retorno()

    pass

verificar()