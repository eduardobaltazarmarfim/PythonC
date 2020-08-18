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

        cabecalho('Verificar Letras')

        cidade=input('Digite o nome de uma cidade: ').lstrip()
        
        resposta='santo'

    except:

        mensagem_erro()

        retorno()

    else:

        if cidade.lower() in resposta:

            print('True')

        else:

            print('False')

        retorno()

    pass

verificar()