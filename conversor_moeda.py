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

        cabecalho('Conversor de Moeda')

        val=float(input('Digite um valor em R$ '))

        dolar=float(input('Digite o valor em U$ '))
                
    except:

        print('Dados inseridos são invalidos!')

        retorno()

    else:

        res=val/dolar

        print('O valor digitado: R$ {}.e o valor em U$ {:.2f}'.format(val,res))

        retorno()

    pass

verificar()