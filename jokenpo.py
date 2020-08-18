import math
import random
import datetime

def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
                
        verificar()
        
            
    else:

        print('Processo finalizado!')

    pass


def cabecalho(texto):

    medida=len(texto)

    cont=medida+20

    esquerda=math.trunc(medida/2)

    direita=math.trunc(medida/2)

    print('-'*cont)

    print(' '*esquerda+texto+' '*direita)

    print('-'*cont)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():

    resp='s'
           
    perdeu=0
    ganhou=0
    empate=0

    while resp=='s' or resp=='S':
        
        try:

            cabecalho('JOKENPO')

            itens=('Pedra','Papel','Tesoura')

            computador=random.randint(0,2)
        
            print('Escolha um opção!\n[0] - Pedra\n[1] - Papel\n[2] - Tesoura\n')

            print('-'*30)

            jogador=int(input('Qual é a sua jogada? '))

        except:

            mensagem_erro()

            retorno()

        else:

            if(jogador>2):

                print('O valor não tem na opção!')
                retorno()

            print('O computador jogou {} e você {}'.format(itens[computador],itens[jogador]))

            if(computador==0):
                
                if(jogador==computador):
                    
                    print('Empate')
                    empate+=1

                elif(jogador==0 and computador==1):

                    print('O computador ganhou!')
                    perdeu+=1

                else:

                    print('Você ganhou!')
                    ganhou+=1

            elif(computador==1):

                if(jogador==computador):

                    print('Empate')
                    empate+=1

                elif(jogador==1 and computador==2):

                    print('O computador ganhou!')
                    perdeu+=1

                else:

                    print('Você ganhou!')
                    ganhou+=1            

            elif(computador==2):

                if(jogador==computador):

                    print('Empate')
                    empate+=1

                elif(jogador==2 and computador==0):

                    print('O computador ganhou!')
                    perdeu+=1

                else:

                    print('Você ganhou!')
                    ganhou+=1

        resp=input('Deseja jogar novamente?[s/n] ')

    print('Você ganhou {} e empatou {} e perdeu {}!'.format(ganhou,empate,perdeu))

    retorno()

    pass

verificar()