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

        cabecalho('Analisando Nome')

        nome=str(input('Digite o seu nome completo: '))

    except:

        mensagem_erro()

        retorno()
    
    else:

        print('Analisando o seu nome...')

        separar=nome.split()

        print('O seu nome em maíusculo é {}.'.format(nome.upper()))
        print('O seu nome em mínusculo é {}.'.format(nome.lower()))
        print('Seu nome completo tem {} letras.'.format(len(nome)-nome.count(' ')))
        print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
        print('O seu primeiro nome é {}.'.format(separar[0]))

        retorno()
                        
    pass


verificar()