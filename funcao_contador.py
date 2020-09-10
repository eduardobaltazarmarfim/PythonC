from os import system
from time import sleep

def retorno():

    while True:

        resp=input('Deseja executar o programa novamente?[s/n]: ').lower()[0]

        if(resp in 'sn'):

            break
        
        print('Digite uma resposta valida S ou N')

    if(resp=='s'):

        verificar()

    else:

        print('Processo finalizado')

    pass


def cabecalho(titulo):

    tam=len(titulo)+4

    print('-'*tam)

    print('  {}'.format(titulo))

    print('-'*tam)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass


def verificar():
    
    try:

        system('cls')

        contador(1,10,1)
        contador(10,0,2)         

        cabecalho('Agora é a sua vez de personalizar a contagem!')

        Inicio=int(input('Início: '))
        Fim=int(input('Fim: '))
        Passo=int(input('Passo: '))

    except:

        mensagem_erro()

        retorno()

    else:

        contador(Inicio,Fim,Passo)

        retorno()

    pass


def contador(inicio,fim,passo):

    cabecalho(f'Contagem de {inicio} até {fim} {passo} em {passo}')

    if(inicio<fim):

        while inicio<=fim:
            
            print('{} -> '.format(inicio),end='',flush=True)
            sleep(0.5)
        
            inicio+=passo

        print('FIM')

    else:

        while inicio>=fim:

            print('{} -> '.format(inicio),end='',flush=True)
            sleep(0.5)

            inicio-=passo

        print('FIM')    
        
     
    pass

verificar()