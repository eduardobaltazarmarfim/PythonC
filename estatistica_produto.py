import random

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ')

    if(resp=='S' or resp=='s'):

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass

def cabecalho(titulo):

    print('-'*30)

    print(' '*9+titulo+' '*15)

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def verificar():

    try:

        cabecalho('Estatística de Produtos')

        resp='s'
        cont=0
        produto=None
        soma=0
        maior=0
        
        while resp=='s':

            produto=input('Informe um produto: ')
            preco=float(input('Qual o preço do produto R$ '))

            if(cont==0):

                menor=preco
                produtoNovo=produto

            else:

                if(preco<=menor):

                    produtoNovo=produto
                    menor=preco

            if(preco>1000):

                maior+=1

            soma+=preco

            cont+=1

            resp=input('Deseja continuar a compra?[s/n] ').lower()

        print('O total da compra R$ {:.2f}'.format(soma))
        print('Na lista temos {} produto(s) acima de R$ 1000.00'.format(maior))
        print('O produto mais barato na lista é {} que custa R$ {:.2f}'.format(produtoNovo,menor))

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


verificar()