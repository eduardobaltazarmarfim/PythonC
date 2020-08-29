import random

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n] ')

    if(resp=='S' or resp=='s'):

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass

def cabecalho(titulo):

    print('-'*30)

    print(' '*9+titulo+' '*15)

    print('-'*30)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def verificar():

    try:

        cabecalho('Analise de Dados do Grupo')

        resp='s'

        cont=0
        homem=0
        mulheres=0

        while resp=='s':

            cabecalho('Cadastre uma Pessoa')
            idade=int(input('Informe a idade: '))
            sexo=input('informe o sexo [M/F] ').upper()

            if(idade>18):

                cont+=1

            if(sexo=='M'):

                homem+=1

            elif(sexo=='F' and idade<20):

                mulheres+=1

            resp=input('Deseja continuar?[S/N] ').lower()

        print('Na base de dados temos {} mais de 18 anos.'.format(cont))
        print('Temos {} homens cadastrado.'.format(homem))
        print('E no programa tem {} mulheres com menos de 20 anos.'.format(mulheres))

        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


verificar()