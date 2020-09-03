from os import system

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ').lower()

    if(resp=='s'):

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass


def cabecalho(titulo):

    print('-'*30)

    print('{:^30}'.format(titulo))

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:
        
        system('cls')

        cabecalho('Matriz')

        valores=list()
        dados=list()

        for l in range(0,3):

            for c in range(0,3):

                num=int(input('Digite um valor para [{}][{}]: '.format(l,c)))

                while num in valores:

                    num=int(input('Digite um valor para [{}][{}] novamente: '.format(l,c)))

                valores.append(num)
                
            dados.append(valores[:])
            valores.clear()
            
    except:

        mensagem_erro()

        retorno()

    else:

        print('-'*30)

        for l in range(0,len(dados)):

            for c in range(0,len(dados)):

                print('[{}]'.format(dados[l][c]),end='')

            print()

        retorno()

    pass


verificar()