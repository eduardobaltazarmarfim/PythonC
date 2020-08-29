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

        cabecalho('Número por Extenso')
        
        num=21

        while num<0 or num>20:

            num=int(input('Digite um número entre 0 e 20: '))

    except:

        mensagem_erro()

        retorno()


    else:

        valores=('zero','um','dois','três','quatro','cinco','seis','sete','oito','novo','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')      

        print('O valor por extenso do número é {}'.format(valores[num].upper()))

        retorno()

    pass


verificar()