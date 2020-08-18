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

    esquerda=medida-5

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

        cabecalho('Calcular Desconto (%)')

        preco=float(input('Digite o preço do produto R$ '))
        desconto=float(input('Digite o desconto do item '))

    except:

        mensagem_erro()

        retorno()

    else:

        novoValor=preco*(1-(5/100))

        print('O valor do item é de R$ {:.2f} e foi aplicado um desconto de {:.2f}% ficando no valor novo de R$ {:.2f}'.format(preco,desconto,novoValor))

        retorno()

    pass

verificar()