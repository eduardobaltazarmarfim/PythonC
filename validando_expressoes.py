def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ').lower()

    if(resp=='s'):

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

        cabecalho('Validando Expressões')

        valores=list()

        num=input('Digite a expressão: ')
    
    except:

        mensagem_erro()

        retorno()
    
    else:

        for i in num:

            if i=='(':

                valores.append(i)

            elif i==')':

                valores.append(i)


        if(valores.count('(')==valores.count(')')):

            print('Sua expressão está valida')

        else:

            print('Sua expressão está invalida!')

        retorno()

    pass


analisar()