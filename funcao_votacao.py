from os import system
from datetime import datetime

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]').lower()[0]

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

        cabecalho('Controle de Votação')

        num=int(input('Ano de nascimento: '))

        votacao(num)

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass

def votacao(nascimento=0):

    anoAtual=datetime.today().year
    nasc=nascimento
    idade=anoAtual-nasc

    if((idade>=16 and idade<18) or idade>70):
        
        print('Você tem {} anos e seu voto é opcional'.format(idade))

    elif(idade>=18 and idade<=70):

        print('Você tem {} anos e seu voto é obrigatório!'.format(idade))

    else:

        print('Você tem {} anos e seu voto está negado!'.format(idade))

    pass

analisar()