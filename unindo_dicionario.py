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

        cabecalho('Unindo Dicionários e Listas')

        dados=dict()

        pessoa=list()

        soma=media=0

        while True:
    
            dados.clear()

            nome=str(input('Nome: ')).capitalize()
            idade=int(input('Idade: '))
            dados['nome']=nome
            dados['idade']=idade
            soma+=idade    
                
            while True:
                                    
                sexo=str(input('[M/F]: ')).upper()[0]
                    
                if(sexo in 'MF'):
            
                    break

                print('ERRO! - Digite apenas M ou F')

            dados['sexo']=sexo

            pessoa.append(dados.copy())
                
            while True:

                resp=str(input('Deseja continuar?[s/n]: ')).lower()[0]

                if resp in 'sn':

                    break

                print('ERRO! - Digite apenas s ou n')

            print('-'*30)
            
            if resp=='n':

                break

    except:

        mensagem_erro()

        retorno()

    else:

        media=soma/len(pessoa)
        print('Temos cadastradas {} pessoas'.format(len(pessoa)))
        print('A média de idade é {:.2f} anos'.format(media))

        print('As mulheres cadastradas foram: ',end='')

        for p in pessoa:

            if p['sexo'] in 'F':

                print('[{}] '.format(p['nome']),end='')

        print()

        print('Pessoas acima da média: ',end='')

        for i in pessoa:

            if i['idade']>=media:

                for k,p in i.items():

                    print('{} = {};'.format(k,p),end='')

        print()

        retorno()

    pass


verificar()