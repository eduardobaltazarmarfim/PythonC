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

    try:

        cabecalho('Analise de Tupla')

        num=(int(input(f'Digite o 1º valor: ')),int(input(f'Digite o 2º valor: ')),int(input(f'Digite o 3º valor: ')),int(input(f'Digite o 4º valor: ')))

    except:

        mensagem_erro()

        retorno()

    else:

        cont=0
        
        print('Os valores digitados foram: {}'.format(num))
        print('O número 9 apareceu: {} veze(s)'.format(num.count(9)))
        if 3 in num:
            print('O número 3 está na: {}º posição'.format(num.index(3)+1))
        else:
            print('Valor não encontrado!')
        print('O(s) valor(es) par(es) digitado(s): ',end='')

        for n in num:

            cont+=1

            if(n%2==0):

                    print(f'{n} ',end='')


        print('\n')
        retorno()

    pass


verificar()