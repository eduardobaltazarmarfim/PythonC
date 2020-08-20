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

        cabecalho('Analisador Completo')

        num=int(input('Digite a quantidade que você quer analisar: '))
        
        soma=0
        media=0
        mulheres=0
        maior=0
        novoNome=''

        for i in range(1,num+1):
            
            print('----{}º Pessoa----'.format(i))
            nome=input('Nome: ')
            idade=int(input('Idade: '))
            sexo=input('Sexo [M/F]: ').upper()
        
            soma+=idade

            if(sexo=='F' and idade<20):

                mulheres+=1

            if(i==1 and sexo=='M'):

                maior=idade
                novoNome=nome

            else:

                if(sexo=='M' and idade>maior):
                    
                    maior=idade
                    novoNome=nome
                
        media=soma/num

        print('A média de idade do grupo é {:.2f}'.format(media))
        print('No grupo temos {} mulheres abaixo de 20 anos!'.format(mulheres))
        print('O homem mais velho do grupo é o {}.'.format(novoNome.upper()))   

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass

verificar()