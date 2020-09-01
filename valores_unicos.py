def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ').lower()

    if(resp=='s'):

        print('-'*30)

        analisar()

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


def analisar():

    try:

        cabecalho('Valores Únicos em Lista')

        valores=list()

        resp='s'

        while resp=='s':

            num=int(input('Digite um valor: '))

            if(num in valores):

                print('Dados já consta cadastrado na lista!')

            else:

                valores.append(num)

            
            resp=input('Deseja inserir mais um valor? [s/n] ').lower()

        print('O valores digitados foram: {}'.format(sorted(valores)))

        retorno()                        

    except:

        mensagem_erro()

        retorno()


    pass


analisar()