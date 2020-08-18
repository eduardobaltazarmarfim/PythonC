def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        verificar()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    medida=len(texto)

    cont=medida+30

    esquerda=35-medida

    direita=medida

    print('-'*cont)

    print(' '*esquerda+texto+' '*direita)

    print('-'*cont)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:

        cabecalho('Reajuste Salárial (R$)')

        nome=input('Digite o nome do funcionário: ')
        salario=float(input('Digite seu salário atual R$ '))
        reajuste=float(input('Digite o percentual de aumento '))

    except:

        mensagem_erro()

        retorno()

    else:

        salarioNovo=salario*(1+(reajuste/100))

        print('O funcionário {} teve reajuste no salário de {:.2f}%, ficando no valor de R$ {:.2f}.'.format(nome,reajuste,salarioNovo))

        retorno()

    pass


verificar()