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

        cabecalho('Conversor de Medidas')

        val=float(input('Digite um valor em metros: '))

    except:

        print('Dados inseridos são invalidos!')

        retorno()


    else:

        cent=val/100

        milim=val/1000

        print('O valor digitado é {} metros.\nO valor em centímetro é {}.\nE o valor em milímetro é {}'.format(val,cent,milim))

        retorno()

    pass

verificar()