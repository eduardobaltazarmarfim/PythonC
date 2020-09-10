from os import system

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

        cabecalho('Calculo de Área')

        lar=float(input('Largumra (m): '))
        comp=float(input('Comprimento (m): '))

        area(lar,comp)

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


def area(l,c):

    res=l*c

    print('A área de um terreno {:.2f}x{:.2f} é de {:.2f} m²'.format(l,c,res))

    pass

verificar()