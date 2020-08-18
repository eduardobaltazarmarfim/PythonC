def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        verificar()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    print('-'*30)

    print(' '*10+texto+' '*15)

    print('-'*30)

    pass


def verificar():

    try:

        cabecalho('Tabuada')

        val=int(input('Digite um valor inteiro: '))

    except:

        print('Dados inseridos são invalidos!')

        retorno()

    else:

        for i in range(0,11):

            res=i*val

            print('{} x {} = {}'.format(i,val,res))

        retorno()

    pass

verificar()