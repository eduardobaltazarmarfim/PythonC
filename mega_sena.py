from random import randint
from os import system
from time import sleep

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

        cabecalho('Mega Sena')

        num=int(input('Quantos jogos deseja sortiar: '))

        cabecalho(f'Sorteando {num} Jogos')

        cont=1

        sorteio=list()

        while cont<=num:

            for i in range(0,6):

                if(i==0):

                    computador=randint(1,60)
                    
                    
                else:

                    while computador in sorteio:

                        computador=randint(1,60)
                      

                sorteio.append(computador)
               
            print('Jogo {}: {}'.format(cont,sorted(sorteio)))
            cont+=1
            sleep(1)
            sorteio.clear()

        cabecalho('Boa Sorte')

        retorno()
            
    except:

        mensagem_erro()

        retorno()

    pass

verificar()