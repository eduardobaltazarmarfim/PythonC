def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        verificar()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    print('-'*40)

    print(' '*10+texto+' '*15)

    print('-'*40)

    pass


def verificar():

    try:

        cabecalho('Validação de Dados')
        
        val=int(input('Digite um valor inteiro: '))

    except:

        print('Dados inseridos são invalidos!')

        retorno()

    else:

        dobro(val)
        triplo(val)
        raiz(val)

        retorno()

    pass


def dobro(x):

    res=x*2

    print('O dobro de {} é igual {}'.format(x,res))


def triplo(x):

    res=x*3

    print('O triplo de {} é igual {}'.format(x,res))


def raiz(x):

    res=x**(1/2)

    print('A raiz quadrada de {} é igual {:.2f}'.format(x,res))

verificar()