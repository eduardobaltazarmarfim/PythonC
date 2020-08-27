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

        cabecalho('Sequência Fibonacci')

        num=int(input('Quantos termos você quer mostrar? '))

    except:

        mensagem_erro()

        retorno()

    else:

        cont=0
        somar=0
        val1=0
        val2=0
        contagem=1

        while cont<num:

            if(contagem==1):

                val1=cont
                somar+=cont
                print('{} -> '.format(somar),end='')
                
            elif(contagem==2):

                val2=cont
                somar+=cont
                print('{} -> '.format(somar),end='')
                
            else:
                
                if(contagem<num):

                    somar=val1+val2
                    val1=val2
                    val2=somar
                    print('{} -> '.format(somar),end='')

                else:

                    somar=val1+val2
                    val1=val2
                    val2=somar
                    print('{} -> FIM\n'.format(somar),end='')                    

            cont+=1
            contagem+=1

        retorno()

    pass


verificar()