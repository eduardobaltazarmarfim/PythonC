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

        cabecalho('Extraindo Dados')

        resp='s'

        valores=list()

        while resp=='s':

            num=int(input('Digite um valor: '))

            while num in valores:

                print('Dados já consta na lista!')
                num=int(input('Digite um valor: '))

            valores.append(num)

            resp=input('Deseja inserir mais um valor na lista?[s/n]').lower()

            print('-'*30)

    except:

        mensagem_erro()

        retorno()

    else:

        dados=list()

        for cont in range(0,len(valores)):

            if cont==0 or valores[cont]>dados[-1]:

                dados.append(valores[cont])

            else:
                
                pos=0

                while pos<=len(dados):

                    if valores[cont]<=dados[pos]:

                        dados.insert(pos,valores[cont])

                        break

                    pos+=1

        print('Foi digitado {} elementos.'.format(len(dados)))
        print('Os valores da lista são: {}'.format(dados))
        
        if((dados.count(5))==1):

            print('O valor 5 se encontra na lista e está na {}º posição'.format(dados.index(5)+1))

        else:

            print('O elemento 5 não foi encontrado na lista')

        retorno()

    pass


analisar()