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

        cabecalho('Lista Ordenada')

        valores=list()
        
        for i in range(0,5):

            num=int(input('Digite um valor: '))

            while num in valores:

                print('Dados já consta cadastrado na lista.')
                num=int(input('Digite um valor: '))                

            if(i==0 or num>valores[-1]):

                valores.append(num)

            else:
                
                cont=0

                while cont<=len(valores):

                    if(num<=valores[cont]):

                        valores.insert(cont,num)

                        break

                    cont+=1

        print('Os valores da lista foram: {}'.format(valores))

        retorno()          

    except:

        mensagem_erro()

        retorno()


    pass


analisar()