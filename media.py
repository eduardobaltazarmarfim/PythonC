def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        verificar()
            
    else:

        print('Processo finalizado!')

    pass
 
def cabecalho(texto):

    print('-'*40)

    print(' '*10+texto+' '*15)

    print('-'*40)

    pass


def verificar():

    try:

        cabecalho('Validação de Notas')

        notas=list()

        total=0

        x=0

        for i in range(0,4):

            x+=1
            
            valor=float(input('Digite a {} nota: '.format(x)))
            
            notas.append(valor)


    except:

        print('Dados inseridos são invalidos!')

        retorno()

    else:

        for i in range(0,4):

            total+=notas[i]

        media=total/len(notas)

        if(media>7):

            print('Aluno aprovado, a média final é {}'.format(media))

        elif(media>=4 and media<7):

            print('Aluno de recuperação, a média final é {}'.format(media))

        else:

            print('Aluno reprovado, a média final é {}'.format(media))

        retorno()

    pass

verificar()