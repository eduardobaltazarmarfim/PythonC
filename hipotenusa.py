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

        cabecalho('Calculo da Hipotenusa')

        val1=float(input('Digite a medida do cateto oposto: '))
        val2=float(input('Digite a medida do cateto adjacente: '))

    except:

        mensagem_erro()

        retorno()

    else:

        hip=math.hypot(val1,val2)

        print('O valor da hipotenusa dos valor {:.2f}x{:.2f} é {:.2f}'.format(val1,val2,hip))

        retorno()

    pass

verificar()