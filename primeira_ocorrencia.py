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

        cabecalho('Ocorrencia de Texto')
        
        frase=input('Digite uma frase: ')

    except:

        mensagem_erro()

        retorno()

    else:

        letras=frase.strip().lower().count('a')

        print('A letra (A) aparece {} vezes.'.format(letras))
        print('A letra (A) aparece na {}º posição.'.format(frase.find('a')+1))
        print('A última posição de (A) aparece na {}º posição.'.format(frase.rfind('a')+1))

        retorno()

    pass

verificar()