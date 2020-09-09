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

        cabecalho('Cadastro de Jogador')

        jogos=list()

        dados=dict()

        gols=0

        nome=str(input('Nome do jogador: ')).capitalize()
        partidas=int(input('Quantas partidas {} jogou: '.format(nome)))

        for i in range(0,partidas):

            num=int(input('{:>5} Quantos gols na {}º partida: '.format('',i+1)))
            gols+=num
            jogos.append(num)

        dados['nome']=nome
        dados['gols']=jogos
        dados['total']=gols

        print('-'*30)

    except:

        mensagem_erro()

        retorno()

    else:

        print(dados)

        print('-'*30)

        for k,v in dados.items():

            print('O campo {} tem o valor: {}'.format(k,v))

        print('-'*30)

        print('O jogador {} jogou {} partidas'.format(nome,len(jogos)))

        for i,c in enumerate(jogos):

            print('{:>3} Na {}º partida, fez {} gols.'.format("=>",i+1,c))

        print('Foi um total de {} gols'.format(dados['total']))

        dados.clear()
        jogos.clear()

        retorno()
        
    pass

verificar()