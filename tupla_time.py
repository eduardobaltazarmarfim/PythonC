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

    cabecalho('Time de Futebol')

    time=('corinthians','palmeiras','santos','Grêmio','curzeiro','flamengo','vasco','chapecoense','atlético','botafogo','atlético-PR','bahia','são paulo','fluminense','sport recife','EC vitória','coritiba','avaí','ponte preta','atlético-GO')

    print('-='*15)
    print(f'Lista de times do Brasileirão: {time}')

    print('-='*15)
    print(f'Os 5 primeiros são: {time[0:5]}')

    print('-='*15)
    print(f'Os 4 últimos são: {time[-4:]}')
    
    print('-='*15)
    print(f'Time em ordem alfabética: {sorted(time)}') 

    print('-='*15)
    print(f'Posição do Chapecoense: {time.index("chapecoense")+1}º posição')       

    pass



verificar()