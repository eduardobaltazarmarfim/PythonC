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

        cabecalho('Tabuada V3')

        num=0

        while num>=0:
            
            num=int(input('Quer ver a tabuada de qual valor: '))
            
            for i in range(0,11):

                res=i*num

                print('{} x {} = {}'.format(i,num,res))
        
            print('-'*30)


        print('Programa encerrado volte sempre!')

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


verificar()