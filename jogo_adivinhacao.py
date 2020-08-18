import math
import random

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

    cabecalho('Jogo de Adivinhação')
        
    resp='s'

    acertou=0
    errou=0

    while resp=='s' or resp=='S':

        cont=0
        falta=3
        computador=random.randint(0,5)
                
        while cont<3:

            try:

                numero=int(input('Digite um número de 0 até 5: '))

            except:
                
                mensagem_erro()

                retorno()

                break

            else:
            
                if(numero==computador):

                    print('Parabéns você acertou o número!')
                    acertou+=1

                    break

                else:

                    cont+=1
                    falta-=1

                    if(falta>0):
                            
                        print('Você só tem {} tentativa(s).'.format(falta))
                        print('-'*30)

                    else:

                        errou+=1                        
                        print('-'*30)
                        print('Você perdeu!')

            
        resp=input('Deseja jogar novamente?[s/n]: ')

        print('-'*30)


    print('Você acertou {} e errou {} vezes.'.format(acertou,errou))                                  

    retorno()
    
    pass

verificar()