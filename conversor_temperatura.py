def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        verificar()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    medida=len(texto)

    cont=medida+30

    esquerda=35-medida

    direita=medida

    print('-'*cont)

    print(' '*esquerda+texto+' '*direita)

    print('-'*cont)

    pass

def mensagem_erro():

    print('Dados inseridos são invalidos!')

    pass

def menu():

    print('1-Celsius para Fahrenheit')
    print('2-Celsius para Kelvin')

    print('-'*30)
    
    print('3-Fahrenheit para Celsius')
    print('4-Fahrenheit para Kelvin')

    print('-'*30)

    print('5-Kelvin para Celsius')
    print('6-Kelvin para Fahrenheit')

    print('-'*30)

    pass

def verificar():

    try:

        cabecalho('Conversor de Temperatura')

        temperatura=float(input('Informe a Temperatura: '))

        cabecalho('Escolha as opções')

        menu()
        
        opcoes=int(input('Digite o número da opção para calcular a conversão: '))
        
    except:

        mensagem_erro()

        retorno()

    else:

        funcoes={1:celsus_fahrenheit,2:celsus_kelvin,3:fahrenheit_celsius,4:fahrenheit_Kelvin,5:Kelvin_celsius,6:Kelvin_fahrenheit}

        funcoes.get(opcoes)(temperatura)

        retorno()

    pass


def celsus_fahrenheit(x):

    formula=(x*(9/5))+32

    print('A temperatura de {:.2F}ºC corresponde a {:.2f}ºF!'.format(x,formula))

    pass

def celsus_kelvin(x):

    formula=x+273.15

    print('A temperatura de {:.2F}ºC corresponde a {:.2f}ºK!'.format(x,formula))

    pass

def fahrenheit_celsius(x):

    formula=(x-32)*(5/9)

    print('A temperatura de {:.2F}ºF corresponde a {:.2f}ºC!'.format(x,formula))

    pass

def fahrenheit_Kelvin(x):

    formula=((x-32)*(5/9))+273.15

    print('A temperatura de {:.2F}ºF corresponde a {:.2f}ºK!'.format(x,formula))

    pass

def Kelvin_celsius(x):

    formula=x-273.15

    print('A temperatura de {:.2F}ºK corresponde a {:.2f}ºC!'.format(x,formula))

    pass

def Kelvin_fahrenheit(x):

    formula=((x-273.15)*(9/5))+32

    print('A temperatura de {:.2F}ºK corresponde a {:.2f}ºF!'.format(x,formula))

    pass

verificar()