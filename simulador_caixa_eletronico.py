import math

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

        cabecalho('Caixa Eletrônico')

        num=int(input("Qual o valor que deseja sacar? R$ "))

    except:

        mensagem_erro()

        retorno()

    else:

        nota50=0
        nota20=0
        nota10=0
        nota05=0
        saque=0

        while num>0:

            if(num>=50):

                saque=num/50
                nota50=math.trunc(saque)
                num-=nota50*50
                print('Total de {} cédulas de R$ 50.00'.format(nota50))
                                  
            elif(num>=20 and num<50):

                saque=num/20
                nota20=math.trunc(saque)
                num-=nota20*20
                print('Total de {} cédulas de R$ 20.00'.format(nota20))
         
            elif(num>=10 and num<20):

                saque=num/10
                nota10=math.trunc(saque)
                num-=nota10*10
                print('Total de {} cédulas de R$ 10.00'.format(nota10))

            elif(num>=5 and num<10):

                saque=num/5
                nota05=math.trunc(saque)
                num-=nota05*5
                print('Total de {} cédulas de R$ 5.00'.format(nota05))
            
            else:

                print('O valor digitado não tem como ser saquado!')

                break
                
        print('Saque efetuado com sucesso volte sempre!')

        retorno()   

    pass


verificar()