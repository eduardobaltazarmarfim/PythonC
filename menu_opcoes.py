import math
import random
import datetime
from time import sleep

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

    try:

        cabecalho('Criando Menu de Opções')

        valores=list()
        
        for i in range(1,3):

            num=int(input('Digite o {}º número inteiro: '.format(i)))

            valores.append(num)


    except:

        mensagem_erro()

        retorno()

    else:
        
        valor=1
        
        while valor!=5:

            print('-'*30)

            print('Opções')

            print('[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa')
            
            cont=0

            escolha=6
            
            while escolha>5 or escolha<0:
                
                cont+=1

                if(cont==1):

                    escolha=int(input('Qual é sua opção? '))

                else:

                    escolha=int(input('Opção invalida digite novamente: '))

            funcoes={1:somar,2:multiplicar,3:maior,4:novos_numeros,5:sair_sistema}

            a=0

            b=0

            if(escolha<=3):

                for i in range(0,2):

                    x=valores[i]

                    if(i==0):

                        a=x

                    else:

                        b=x               

                funcoes.get(escolha)(a,b)

            elif(escolha==4):

                funcoes.get(escolha)()

            else:

                valor=escolha
        
        retorno()
        
    pass

def somar(a,b):

    res=a+b

    print('A soma de {} e {} da um total de {}'.format(a,b,res))

    pass

def multiplicar(a,b):

    res=a*b

    print('A multiplicação de {} e {} da um total de {}'.format(a,b,res))

    pass

def maior(a,b):

    if(a>b):

        print('O maior valor é {}'.format(a))
    
    else:

        print('O maior valor é {}'.format(b))

    pass

def novos_numeros():

    verificar()

    pass

def sair_sistema():

    print('Processo finalizado!')

    pass
    
verificar()