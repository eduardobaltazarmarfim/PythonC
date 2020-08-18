def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        verificar()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    print('-'*30)

    print(' '*10+texto+' '*15)

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    try:

        cabecalho('Pintando Parede')

        largura=float(input('Digite a largura: '))
        altura=float(input('Digite a altura: '))

    except:

        mensagem_erro()

        retorno()


    else:

        medida=largura*altura

        tinta=medida/2

        print('A parede tem {}m² e precisa de {}L de tinta para ser pintada.'.format(medida,tinta))

        retorno()

    pass

verificar()