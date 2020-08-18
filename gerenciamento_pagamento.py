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

        cabecalho('Gerenciador de Pagamento')
        
        valor=float(input('Digite um valor R$ '))

        print('-'*30)

        print('Condição de Pagamento\n[1] - Dinheiro/Cheque\n[2] - Cartão de Débito\n[3] - Cartão de Crédito')

        print('-'*30)

        num=int(input('Digite um opção: '))
        
    except:

        mensagem_erro()

        retorno()

    else:
        
        opcoes={1:avista,2:cartaoavista,3:parcelado}

        opcoes.get(num)(valor)

        retorno()

    pass

def avista(x):

    preco=x*(1-(10/100))

    print('O valor do produto R$ {:.2f} é você vai pagar R$ {:.2f}!'.format(x,preco))

    pass

def cartaoavista(x):

    preco=x*(1-(5/100))

    print('O valor do produto R$ {:.2f} é você vai pagar R$ {:.2f}!'.format(x,preco))

    pass

def parcelado(x):

    try:

        parcelas=int(input('Digite a quantidade de parcelas: '))
    
    except:

        mensagem_erro()

        retorno()

    else:

        if(parcelas<=2):

            preco=x/parcelas

            print('O valor do produto R$ {:.2f} e você vai pagar em até {} vezes sem juros no valor de R$ {:.2f}!'.format(x,parcelas,preco))

        else:

            valorJuros=x*(1+(20/100))
            preco=valorJuros/parcelas

            print('O valor do produto R$ {:.2f} e você vai pagar em até {} vezes com juros no valor de R$ {:.2f} ficando no final da parcela R$ {:.2f}'.format(x,parcelas,preco,valorJuros))            

    pass

verificar()