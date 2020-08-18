def retorno():

    res=input('Deseja executar o programa novamente?[s/n] ')

    if(res=='s' or res=='S'):
        
        verificar()
            
    else:

        print('Processo finalizado!')

    pass

def cabecalho(texto):

    print('-'*30)

    print(' '*10+texto+' '*15)

    print('-'*30)

    pass

def verificar():

    cabecalho('Principal')

    dados=input('Digite um valor: ')

    print('O tipo primitivo é {}'.format(type(dados)))
    print('Só tem espaço {}'.format(dados.isspace()))
    print('É um número {}'.format(dados.isnumeric()))
    print('É alfabetico {}.'.format(dados.isalpha()))
    print('É alfanumerico {}'.format(dados.isalnum()))
    print('É maíuscula {}'.format(dados.isupper()))
    print('É mínuscula {}'.format(dados.islower()))
    print('É capitalizada {}'.format(dados.istitle()))

    retorno()
    
    pass

verificar()