def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ')

    if(resp=='S' or resp=='s'):

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

        cabecalho('Vários Números com Flag')

        num=0
        soma=0
        cont=0

        while num!=999:

            num=int(input('Digite um número: '))

            if(num!=999):

                cont+=1
                soma+=num
                
        print('Você digitou {} números e a soma é {}.'.format(cont,soma))
        
        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


verificar()