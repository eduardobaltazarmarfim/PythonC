def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ')

    if(resp=='S' or resp=='s'):

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass

def cabecalho(titulo):

    print('-'*30)

    print(f'{titulo:^30}')

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:

        cabecalho('Lista de Preço')

        listaPreco=('Lápis',1.75
        ,'Caderno',15.90,'Borracha',2,'Estojo',25,'Transferidor',4.20,'Compasso',9.99,
        'Mochila',120.32,'Caneta',22.30,'Livro',34.90
        )

    except:

        mensagem_erro()

        retorno()

    else:

        for i in range(0,len(listaPreco)):
            
            if(i%2==0):

                print(f'{listaPreco[i]:.<30}',end='')

            else:

                print(f'R$ {listaPreco[i]:.>.2f}')


        retorno()

    pass


verificar()