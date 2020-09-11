from os import system

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]: ').lower()[0]

        if resp in 'sn':

            break

        mensagem_erro()

    if resp=='s':

        analisar()

    else:

        print('Processo finalizado!')

    pass


def cabecalho(titulo):

    tam=len(titulo)+4

    print('-'*tam)
    
    print(f'  {titulo}')

    print('-'*tam)

    pass


def analisar():

    try:

        system('cls')

        cabecalho('Ficha de Jogador')

        jogador=str(input('Nome do Jogador: '))
        num=str(input('Número de Gols: '))

        if num.isnumeric():
            num=int(num)

        else:

            num=0

        if jogador.strip()=='':

            ficha(gol=num)

        else:

            ficha(jogador,num)

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


def ficha(nome='<desconhecido>',gol=0):

    print('O jogador {} fez {} gols.'.format(nome,gol))

    pass


analisar()