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

        cabecalho('Lista de jogador')

        dados=dict()

        jogadores=list()

        gols=list()
        
        while True:
            
            soma=0
            dados.clear()
                        
            nome=str(input('Nome do jogador: ')).capitalize()
            dados['nome']=nome
            partida=int(input('Quantas partidas ele jogou: '))

            for i in range(0,partida):

                num=int(input('{:>5} Quantos gols na {}º partida: '.format('=>',i+1)))
                soma+=num
                gols.append(num)

            dados['gols']=gols[:]
            dados['total']=soma
            jogadores.append(dados.copy())
            
            gols.clear()

            while True:

                resp=str(input('Deseja continuar?[s/n]: ')).lower()[0]

                if resp in 'sn':

                    break

                print('Digite uma resposta valida S ou N')

            if resp=='n':

                break

            print('-'*30)

    except:

        mensagem_erro()

        retorno()

    else:

        cabecalho('Jogadores')

        print(f'{"cod":<7}',end='')

        for i in dados.keys():

            print(f'{i:<15}',end='')

        print()
        
        print('-'*30)

        for c,v in enumerate(jogadores):
            
            print(f'{c+1:<7}',end='')

            for x in v.values():

                print(f'{str(x):<15}',end='')
            
            print()

        cabecalho('Analise de dados')

        while True:

            num=int(input('Mostrar dados de qual jogador? (999 para parar): '))

            if num==999:

                break

            if (num-1)>=len(jogadores):

                mensagem_erro()

            else:

                print('Levantamento do Jogador  {}'.format(jogadores[num-1]['nome']))

                for i,c in enumerate(jogadores[num-1]['gols']):

                    print('Na {}º partida fez {} gols'.format(i+1,c))

                print('Total de {} gols'.format(jogadores[num-1]['total']))

                print('-'*30)
        
        retorno()
            
    pass


verificar()