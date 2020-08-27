def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ')

    if(resp=='S' or resp=='s'):

        print('-'*30)

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

        cabecalho('Progressão PA')

        num=int(input('Digite o primeiro termo: '))

        numPA=int(input('Digite sua razão PA: '))

    except:

        mensagem_erro()

        retorno()

    else:

        cont=1

        while cont<=10:
            
            
            if(cont>=10):

                print('{} = FIM\n'.format(num),end='')

            else:

                print('{} -> '.format(num),end='')

            cont+=1
            num+=numPA
            

        retorno()

    pass


verificar()