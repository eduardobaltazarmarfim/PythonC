from os import system

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]: ').lower()[0]

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

        cabecalho('Analisando Dicionário')


        valores=list()

        while True:

            num=float(input('Digite um valor: '))

            valores.append(num)

            while True:

                resp=str(input('Deseja continuar?[s/n]: ')).lower()[0]

                if resp in 'sn':

                    break

                mensagem_erro()

            if resp=='n':

                break
        
    except:

        mensagem_erro()

        retorno()

    else:

        while True:

            opcao=str(input('Você quer saber a situação?[1 para verdadeiro/0 para falso]: '))

            if opcao in '10':

                opcao=int(opcao)

                break

            mensagem_erro()

        if opcao==1:

            opcao=True

        else:

            opcao=False

        dicionario(valores[:],sit=opcao)

        valores.clear()

        retorno()

    pass


def dicionario(*num,sit=True):

    cont=maior=menor=soma=media=0

    dados=dict()

    for i in num:

        for k in i:

            if cont==0:

                maior=k

            else:

                if k>=maior:

                    maior=k
                
                else:

                    menor=k

            cont+=1
            soma+=k
    
    media=soma/cont

    dados['total']=cont
    dados['maior']=maior
    dados['menor']=menor
    dados['média']=media

    if sit==True:

        if media>=7:

            dados['situação']='APROVADO'

        elif media>=4 and media<7:

            dados['situação']='REGULAR'

        else:

            dados['situação']='REPROVADO'
  
    print(dados)

    pass

analisar()