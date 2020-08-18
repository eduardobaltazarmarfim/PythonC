def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):

        mensagem()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    print('-'*30)

    print(' '*10+texto+' '*15)

    print('-'*30)

    pass


def mensagem():

    cabecalho('Principal')

    nome=input('Digite seu nome: ')

    print('Seja bem vindo {}.'.format(nome))

    retorno()

    pass

mensagem()