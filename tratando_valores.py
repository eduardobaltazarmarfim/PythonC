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

        cabecalho('Tratando Valores')

        num=0
        cont=0
        soma=0

        while num!=999:
           
            num=int(input('Digite um número [999 para parar]: '))

            if(num!=999):

                soma+=num
                cont+=1

        print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


verificar()