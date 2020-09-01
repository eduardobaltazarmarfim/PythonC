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

        cabecalho('Dividindo Valores de uma Lista')

        resp='s'

        valores=list()

        while resp=='s':

            num=int(input('Digite um valor:'))
            
            while num in valores:

                print('Valor digitado já consta na lista')
                num=int(input('Digite um valor:'))

            valores.append(num)

            resp=input('Deseja inserir um novo valor?[s/n]').lower()

    except:

        mensagem_erro()

        retorno()

    else:

        ordenar(valores)

        pares(valores)

        impares(valores)        

        retorno()

    pass

def ordenar(listagem):

    dados=list()

    for i in range(0,len(listagem)):

        if i==0 or listagem[i]>dados[-1]:

            dados.append(listagem[i])

        else:

            cont=0

            while cont<=len(listagem):

                if listagem[i]<=dados[cont]:

                    dados.insert(cont,listagem[i])

                    break

                cont+=1

    
    print('Os dados da lista são: {}'.format(dados))

    pass

def pares(par):

    dados=list()
    dadosOrdem=list()

    for i in par:

        if i%2==0:

            dados.append(i)

    for cont in range(0,len(dados)):

        if cont==0 or dados[cont]>dadosOrdem[-1]:

            dadosOrdem.append(dados[cont])

        else:

            pos=0

            while pos<=len(dadosOrdem):

                if dados[cont]<=dadosOrdem[pos]:

                    dadosOrdem.insert(pos,dados[cont])

                    break

                pos+=1
    
    print('A lista de números pares são: {}'.format(dadosOrdem))

    pass

def impares(impar):

    dados=list()
    dadosOrdem=list()

    for i in impar:

        if i%2==1:

            dados.append(i)

    for i in range(0,len(dados)):

        if i==0 or dados[i]>dadosOrdem[-1]:

            dadosOrdem.append(dados[i])

        else:

            linha=0

            while linha<=len(dados):

                if dados[i]<=dadosOrdem[linha]:

                    dadosOrdem.insert(linha,dados[i])

                    break

                linha+=1

    
    print('A lista de números ímpares são: {}'.format(dadosOrdem))

    pass


analisar()