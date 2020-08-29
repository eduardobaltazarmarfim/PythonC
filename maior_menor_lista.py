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

        cabecalho('Maior e Menor Valores Lista')

        valores=list()

        cont=0

        for i in range(0,5):

            cont+=1

            num=int(input('Digite o {}º valor: '.format(cont)))
            
            valores.append(num)

    except:

        mensagem_erro()

        retorno()

    else:
        
        cont=0
        maior=max(valores)
        menor=min(valores)

        print('Os valores da lista: {}'.format(valores))
        
        print('O maior valor é {} ele está nas posições: '.format(maior),end='')

        for i,v in enumerate(valores):

                if(v==maior):

                    print('{} '.format(i),end='')

        print('\nO menor valor é {} ele está nas posições: '.format(menor),end='')

        for i,v in enumerate(valores):

                if(v==menor):

                    print('{} '.format(i),end='')


        print('\n')              

        retorno()

    pass


verificar()