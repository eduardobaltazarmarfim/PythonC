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

        cabecalho('Maior e Menor')

        resp='s'
        soma=0
        media=0
        cont=0
        maior=0
        menor=0

        while resp=='s':

            num=int(input('Digite um número: '))

            if(cont==0):

                maior=num

            elif(num>=maior):

                maior=num

            else:

                menor=num

            resp=input('Quer digitar um número?[s/n]: ').lower()

            soma+=num
            cont+=1
        
        media=soma/cont

        print('Você digitou {} números e a média foi {:.2f}'.format(cont,media))
        print('O maior valor foi {} e o menor foi {}.'.format(maior,menor))
        
        retorno()

    except:

        mensagem_erro()

        retorno()

    pass


verificar()