def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        somar()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    print('-'*30)

    print(' '*10+texto+' '*15)

    print('-'*30)

    pass

def somar():

    try:

        cabecalho('Principal')

        val01=float(input('Digite o primeiro valor: '))
        val02=float(input('Digite o segundo valor: '))
            
    except:

        print('Dados inseridos são invalidos!')

        retorno()

    else:

        res=val01+val02

        print('A soma de {} e {} é igual {}.'.format(val01,val02,res))

        retorno()

    pass

somar()
