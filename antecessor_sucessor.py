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

        cabecalho('Controle de Dados')

        val=int(input('Digite um valor inteiro: '))

    except:

        print('Dados inseridos são invalidos!')

        retorno()

    else:

        print('O valor digitado é {} o antecessor {} e o sucessor é {}'.format(val,val-1,val+1))
        
        retorno()

    pass

verificar()