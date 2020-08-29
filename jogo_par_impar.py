import random

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

        cabecalho('Jogo do Par ou Ímpar')

        cont=0
  
        par=1
        impar=0
        
        while True:

            jogador=int(input('Diga um valor: '))
            tipo=input('Par ou Ímpar?[P/I]').upper()

            par=1
            impar=0

            if(tipo=='P'):
                
                while par%2!=0:

                    par=random.randint(0,11)
                    computador=par+jogador
                    
                   

            else:

                while impar%2==0:
                                        
                    impar=random.randint(0,11)
                    computador=impar+jogador
                                        


            if(computador%2==0):

                print('Você ganhou!')
                cont+=1

            else:

                break

        
        print('Game Over Você ganhou {} vez.'.format(cont))

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


verificar()