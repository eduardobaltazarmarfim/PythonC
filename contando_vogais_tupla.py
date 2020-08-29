def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ')

    if(resp=='S' or resp=='s'):

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass

def cabecalho(titulo):

    print('-'*30)

    print(f'{titulo:^30}')

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:

        cabecalho('Contando Vogais em Tupla')

        palavras=('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR','MERCADO','PROGRAMADOR','FUTURO')

    except:

        mensagem_erro()

        retorno()

    else:

        for n in palavras:

            print('\nNa palavra {} temos: '.format(n),end='')

            for letra in n:

                if letra.lower() in 'aeiou':

                    print(letra,end=' ')

        retorno()

    pass


verificar()