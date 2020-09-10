from os import system
from time import sleep 

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

        maior(5,6,4,50,11,12)
        maior(4,9,8,7)
        maior(6)
        maior(5,45)
        maior(0)

    except:

        mensagem_erro()

        retorno()

    pass


def maior(*valores):

    cabecalho('Função Maior Valor')
    
    maior=0
    
    for i in range(0,len(valores)):

        print('{} -> '.format(valores[i]),end='',flush=True)
        sleep(1)

        if(i==0):

            maior=valores[i]
            
        else:

            if(valores[i]>=maior):

                maior=valores[i]

    print('FIM')

    print('Foram analisado {} valores'.format(len(valores)))

    print('O maior valor entre os dados apresentados é {}'.format(maior))
    
    pass

analisar()