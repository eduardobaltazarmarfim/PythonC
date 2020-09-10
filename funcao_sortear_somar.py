from os import system
from time import sleep
from random import randint

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]').lower()[0]

        if resp in 'sn':

            break

        mensagem_erro()

    if resp=='s':

        analisar()

    else:

        print('Processo finalizado!')

    pass


def cabecalho(titulo):

    tam=len(titulo)+4

    print('-'*tam)
    
    print(f'  {titulo}')

    print('-'*tam)

    pass


def analisar():

    try:

        system('cls')

        cabecalho('Sortear Valores')

        dados=list()

        for i in range(0,2):

            num=int(input('Digite o {}º valor: '.format(i+1)))
            dados.append(num)

        sortear_numero(dados[0],dados[1])
        
        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


def sortear_numero(*valores):

    cont=0
    
    dados=list()

    while cont<5:
        
        num=randint(valores[0],valores[1])

        while num in dados:
        
            num=randint(valores[0],valores[1])
        
        dados.append(num)
            
        print(f'{num} -> ',end='',flush=True)
        sleep(1)

        cont+=1

    print('FIM')

    pares(dados[:])

    pass

def pares(*valores):

    soma=0

    cont=0

    print('Somando os valores pares de [',end='')

    for c in valores:

        for k in c:

            print('{} '.format(k),end='')

            if k%2==0:

                soma+=k
            
            cont+=1
 
    print('], temos {}'.format(soma))
    
    pass


analisar()