import random

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ')

    if(resp=='S' or resp=='s'):

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass

def cabecalho(titulo):

    print('-'*30)

    print(' '*9+titulo+' '*15)

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    num=(random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10),random.randint(1,10))
        
    print('Os valores sorteados foram: ',end='')

    for i in num:

        print(f'{i} ',end='')

    print('\nO maior valor é {}'.format(max(num)))
    print('O menor valor é {}'.format(min(num)))

    retorno()

    pass


verificar()