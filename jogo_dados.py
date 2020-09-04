from random import randint
from os import system
from time import sleep
from operator import itemgetter

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ').lower()

    if(resp=='s'):

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass


def cabecalho(titulo):

    print('-'*30)

    print('{:^30}'.format(titulo))

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def verificar():

    try:

        system('cls')

        cabecalho('Jogo de Dados')

        jogo={'Jogador1':randint(1,6),'Jogador2':randint(1,6),'Jogador3':randint(1,6),'Jogador4':randint(1,6)}

        print(f'{"Valores Soteados":^30}')
        print('-'*30)

        for k,v in jogo.items():

            print('{} tirou {} no dados.'.format(k,v))
            sleep(1)

        cabecalho('Rank dos Ganhadores')

        rank=list()

        rank=sorted(jogo.items(),key=itemgetter(1),reverse=True)

        for i,v in enumerate(rank):

            print('{}º o {} tirou {} no dado'.format(i+1,v[0],v[1]))
            sleep(1)

        print('-'*30)

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass

verificar()