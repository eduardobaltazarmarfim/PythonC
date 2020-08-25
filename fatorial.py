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

        cabecalho('Calculo Fatorial')

        num=int(input('Digite um número: '))

    except:

        mensagem_erro()

        retorno()

    else:
        
        cont=1

        for i in range(num,0,-1):

            cont*=i

            if(i==1):

                print('{} = {}'.format(i,cont),end='')

                print('\n')

            else:

                print('{} x '.format(i),end='')
        
        retorno()
        
    pass


    
verificar()