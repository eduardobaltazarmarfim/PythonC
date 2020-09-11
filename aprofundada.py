from  os import system
from validacao import funcoes

def cabecalho(titulo):

    tam=len(titulo)+4

    print('-'*tam)

    print(f'  {titulo}')

    print('-'*tam)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def retorno():

    while True:

        resp=str(input('Deseja executar o programa novamente?[s/n]')).lower()[0]

        if resp in 'sn':

            break

        mensagem_erro()

    if resp=='s':

        analisar()

    else:

        cabecalho('Processo finalizado com sucesso!')

    pass


def analisar():

    try:
        
        system('cls')

        cabecalho('Entrada de Dados')

        funcoes.leiaint()

        retorno()

    except:

        mensagem_erro()
        retorno()

    pass


analisar()