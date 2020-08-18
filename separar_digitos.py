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

        cabecalho('Separar Digitos')

        num=int(input('Digite um número de 0 a 9999: '))

    except:

        mensagem_erro()

        retorno()

    else:
        
        #valor=str(num)

        milhar=num//1000 % 10
        centena=num//100 % 10
        dezena=num//10 % 10
        unidade=num//1 % 10

        print('Milhar: {}'.format(milhar))
        print('Centena: {}'.format(centena))
        print('Dezena: {}'.format(dezena))
        print('Unidade: {}'.format(unidade))

        retorno()
    
    pass

verificar()