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

    system('cls')

    try:
        
        cabecalho('Boletim de Notas')

        dados=list()
        listaAlunos=list()
        
        while True:

            media=0
            soma=0

            nome=input('Nome: ')
            dados.append(nome)

            for i in range(0,2):

                nota=float(input('Nota {}: '.format(i+1)))

                while nota<0 or nota>10:

                    nota=float(input('Nota {}: '.format(i+1)))

                dados.append(nota)
                soma+=nota

            media=soma/2

            if(media>=7):

                status='Aprovado'

            elif(media>=4 and media<7):

                status='Recuperação'

            else:

                status='Reprovado'
            
            dados.append(media)

            dados.append(status)

            listaAlunos.append(dados[:])
            dados.clear()

            resp=input('Deseja continuar?[s/n]: ').lower()

            print('-'*30)

            if(resp!='s'):
                
                break
                
    except:

        mensagem_erro()

        retorno()

    else:

        print(f'{"Nº ":<4} {"Nome":^10} {"Média":^6} {"Status":^10}')

        for i,alunos in enumerate(listaAlunos):

            print('{:<4} {:^10} {:^6} {:^10}'.format(i,alunos[0],alunos[-2],alunos[-1]))

        print('-'*30)

        mostrarNotas=list()

        while True:
   
            nomeAluno=int(input('Mostrar notas de qual aluno? (999 interrompe): '))

            if(nomeAluno==999):

                break

            else:
                
                mostrarNotas=listaAlunos[nomeAluno]

                print('As notas do aluno {} são: [{:.2f}, {:.2f}]'.format(mostrarNotas[0],mostrarNotas[1],mostrarNotas[2]))

            mostrarNotas.clear()

        retorno()

    pass


verificar()