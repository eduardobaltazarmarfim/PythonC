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

        cabecalho('Aluguel de Carro')

        km=float(input('Digite a quantidade percorrida por Km '))
        dia=int(input('Digite a quantidade de dias que foi alugado '))

    except:

        mensagem_erro()

        retorno()

    else:

        taxaKm=0.15
        taxaDia=60

        total=(km*taxaKm)+(dia*taxaDia)

        print('O total a ser pago pelo aluguel de {} dias é de R$ {:.2f}'.format(dia,total))

        retorno()

    pass


verificar()