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

        cabecalho('Matriz V2')

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

        soma=0
        pares=0
        maior=0
        
        for l in range(0,3):

            for c in range(0,3):

                print('[{}]'.format(dados[l][c]),end='')

                num=dados[l][c]

                if(num%2==0):

                    pares+=num

                if(c==2):

                    soma+=num

                if(l==0 and c==2):

                    maior=num

                elif(l>0 and c==2):

                    if(num>maior):

                        maior=num    

            print()

        print('-'*30)
        
        print('A soma dos números pares são: {}'.format(pares))
        print('A soma da terceira coluna é: {}'.format(soma))
        print('O maior da segunda linha é: {}'.format(maior))

        retorno()

    pass

verificar()