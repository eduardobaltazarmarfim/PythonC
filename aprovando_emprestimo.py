import math
import random
import datetime

def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
                
        verificar()
        
            
    else:

        print('Processo finalizado!')

    pass


def cabecalho(texto):

    medida=len(texto)

    cont=medida+20

    esquerda=math.trunc(medida/2)

    direita=math.trunc(medida/2)

    print('-'*cont)

    print(' '*esquerda+texto+' '*direita)

    print('-'*cont)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:

        cabecalho('Aprovação de Emprestimo')

        imovel=float(input('Informe o valor do imóvel R$ '))
        salario=float(input('Informe o seu salário R$ '))
        parcela=int(input('Digite a quantidade de parcelas '))

    except:

        mensagem_erro()

        retorno()

    else:

        valorParcela=imovel/(12*parcela)

        perc=valorParcela/salario

        if(perc>0.30):

            print('Para pagar o imóvel de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(imovel,parcela,valorParcela))
            print('Impréstimo negado!')

        else:

            print('Para pagar o imóvel de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(imovel,parcela,valorParcela))
            print('Impréstimo consedido!')            

        retorno()

    pass


verificar()