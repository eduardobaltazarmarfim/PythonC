from os import system

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

        cabecalho('Dicionário')

        nome=input('Nome: ').upper()

        media=float(input('Média: '))

        if(media>=7):

            status='Aprovado'

        elif(media>=4 and media<7):

            status='Recuperação'

        else:

            status='Reprovado'

        dados={'aluno':nome,'nota':media,'situacao':status}

        print('-'*30)

        print(f'{" ":6} - nome é igual a {dados["aluno"]}')
        print(f'{" ":6} - nota é igual a {dados["nota"]}')
        print(f'{" ":6} - situação é {dados["situacao"]}')

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass

verificar()