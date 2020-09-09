from os import system
from datetime import date

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

        cabecalho('Cadastro de Funcionário')

        dados=dict()

        while True:

            nome=str(input('Nome: '))
            nascimento=int(input('Ano de nascimento: '))
            carteira=int(input('Número da CTPS (Caso não tenha digite 0): '))

            dados['nome']=nome
            dados['nascimento']=nascimento
            dados['carteira']=carteira           

            if(carteira==0):

                break

            else:

                contratacao=int(input('Ano de contratação: '))
                salario=float(input('Salário R$ '))
                idade=(date.today().year)-nascimento
                aposentado=((contratacao+35)-(date.today().year))+idade

                dados['contratacao']=contratacao
                dados['salario']=salario
                dados['idade']=idade
                dados['aposentado']=aposentado

                break

        print('-'*30)

    except:

        mensagem_erro()

        retorno()

    else:

        for t,d in dados.items():

            print('{} tem o valor {}'.format(t,d))

        print('-'*30)

        retorno()

    pass


verificar()